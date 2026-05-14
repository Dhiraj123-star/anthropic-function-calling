from config.settings import MODEL_NAME
from services.anthropic_service import client
from services.weather_service import get_current_weather
from tools.tools import TOOLS


class AnthropicChatbot:

    def __init__(self):
        self.messages = []

    def chat(self, user_input: str):

        # Add user message
        self.messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        # -----------------------------
        # Streaming API Call
        # -----------------------------
        print("\nClaude: ", end="", flush=True)

        web_search_notified = False

        with client.messages.stream(
            model=MODEL_NAME,
            max_tokens=8096,
            tools=TOOLS,
            messages=self.messages
        ) as stream:

            # -----------------------------
            # Catch server_tool_use BEFORE text streams
            # by listening to raw stream events
            # -----------------------------
            for event in stream:

                # Notify web search as soon as block starts
                if (
                    event.type == "content_block_start"
                    and hasattr(event.content_block, "type")
                    and event.content_block.type == "server_tool_use"
                    and not web_search_notified
                ):
                    print("\n🌐 Claude is searching the web...\n")
                    print("Claude: ", end="", flush=True)
                    web_search_notified = True

                # Stream text chunks live
                elif event.type == "content_block_delta":
                    if hasattr(event.delta, "text"):
                        print(event.delta.text, end="", flush=True)

            response = stream.get_final_message()

        print()  # newline after streaming ends

        # Save assistant response
        self.messages.append(
            {
                "role": "assistant",
                "content": response.content
            }
        )

        # -----------------------------
        # Handle Custom Tool Calls
        # -----------------------------
        for content in response.content:

            if content.type == "tool_use":

                tool_name = content.name
                tool_input = content.input

                print(f"\n🔧 Tool Called: {tool_name}")
                print(tool_input)

                if tool_name == "get_current_weather":

                    result = get_current_weather(tool_input["city"])

                    self.messages.append(
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "tool_result",
                                    "tool_use_id": content.id,
                                    "content": result
                                }
                            ]
                        }
                    )

                    print("\nClaude: ", end="", flush=True)

                    with client.messages.stream(
                        model=MODEL_NAME,
                        max_tokens=8096,
                        tools=TOOLS,
                        messages=self.messages
                    ) as final_stream:

                        for text in final_stream.text_stream:
                            print(text, end="", flush=True)

                        final_response = final_stream.get_final_message()

                    print()

                    self.messages.append(
                        {
                            "role": "assistant",
                            "content": final_response.content
                        }
                    )