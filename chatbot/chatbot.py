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

        # Claude API call
        response = client.messages.create(
            model=MODEL_NAME,
            max_tokens=8096,
            tools=TOOLS,
            messages=self.messages
        )

        # Save assistant response
        self.messages.append(
            {
                "role": "assistant",
                "content": response.content
            }
        )

        # -----------------------------
        # Handle Response Blocks
        # -----------------------------
        text_parts = []
        custom_tool_called = False

        for content in response.content:

            # -----------------------------
            # Custom Tool Calls
            # -----------------------------
            if content.type == "tool_use":

                custom_tool_called = True
                tool_name = content.name
                tool_input = content.input

                print(f"\n🔧 Tool Called: {tool_name}")
                print(tool_input)

                # Weather Tool
                if tool_name == "get_current_weather":

                    result = get_current_weather(tool_input["city"])

                    # Add tool result
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

                    # Final Claude response
                    final_response = client.messages.create(
                        model=MODEL_NAME,
                        max_tokens=8096,
                        tools=TOOLS,
                        messages=self.messages
                    )

                    # Save final assistant response
                    self.messages.append(
                        {
                            "role": "assistant",
                            "content": final_response.content
                        }
                    )

                    # Return final text
                    for block in final_response.content:
                        if block.type == "text":
                            return block.text

            # -----------------------------
            # Built-in Web Search
            # Anthropic handles server-side — just notify
            # -----------------------------
            elif content.type == "server_tool_use":
                print("🌐 Claude is searching the web...")

            # -----------------------------
            # Collect ALL text blocks
            # (web search may produce multiple text blocks)
            # -----------------------------
            elif content.type == "text":
                text_parts.append(content.text)

        # -----------------------------
        # Return combined full response
        # (only if no custom tool was called)
        # -----------------------------
        if text_parts and not custom_tool_called:
            return "\n".join(text_parts)

        return "No response generated."