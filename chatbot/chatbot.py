import json
from config.settings import MODEL_NAME
from services.anthropic_service import client
from services.weather_service import get_current_weather
from tools.tools import TOOLS


class AnthropicChatbot:

    def __init__(self):
        self.messages = []

    def chat_stream(self, user_input: str):
        """
        Generator that yields SSE-formatted JSON strings.

        Event types:
          {"type": "status",  "content": "..."}   — system notices (web search, tool call)
          {"type": "text",    "content": "..."}   — streamed assistant text chunks
          {"type": "done"}                        — signals end of response
        """

        self.messages.append({"role": "user", "content": user_input})

        # ── First streaming call ──────────────────────────────────────────────
        web_search_notified = False

        with client.messages.stream(
            model=MODEL_NAME,
            max_tokens=8096,
            tools=TOOLS,
            messages=self.messages,
        ) as stream:

            for event in stream:

                # Detect web search server tool
                if (
                    event.type == "content_block_start"
                    and hasattr(event.content_block, "type")
                    and event.content_block.type == "server_tool_use"
                    and not web_search_notified
                ):
                    yield json.dumps({"type": "status", "content": "🌐 Searching the web…"})
                    web_search_notified = True

                # Stream text deltas
                elif event.type == "content_block_delta":
                    if hasattr(event.delta, "text"):
                        yield json.dumps({"type": "text", "content": event.delta.text})

            response = stream.get_final_message()

        self.messages.append({"role": "assistant", "content": response.content})

        # ── Handle custom tool calls ──────────────────────────────────────────
        for content in response.content:
            if content.type != "tool_use":
                continue

            tool_name = content.name
            tool_input = content.input

            yield json.dumps({"type": "status", "content": f"🔧 Calling tool: {tool_name}"})

            if tool_name == "get_current_weather":
                result = get_current_weather(tool_input["city"])

                self.messages.append({
                    "role": "user",
                    "content": [{
                        "type": "tool_result",
                        "tool_use_id": content.id,
                        "content": result,
                    }],
                })

                # Second streaming call after tool result
                with client.messages.stream(
                    model=MODEL_NAME,
                    max_tokens=8096,
                    tools=TOOLS,
                    messages=self.messages,
                ) as final_stream:

                    for text in final_stream.text_stream:
                        yield json.dumps({"type": "text", "content": text})

                    final_response = final_stream.get_final_message()

                self.messages.append({"role": "assistant", "content": final_response.content})

        yield json.dumps({"type": "done"})