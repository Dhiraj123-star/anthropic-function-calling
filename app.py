import json
import os

from dotenv import load_dotenv
from anthropic import Anthropic

# load environment variables
load_dotenv()

# Read API Key
api_key = os.getenv("ANTHROPIC_API_KEY")

# Anthropic Client
client = Anthropic(api_key=api_key)

# ----------------------
# Local Tool function
# ----------------------

def get_weather(city:str):
    return {
        "city":city,
        "temperature":"32°C",
        "condition":"Sunny"
    }

# -----------------
# Tool Definition
# -----------------

tools = [
    {
        "name":"get_weather",
        "description":"Get current weather for a city",
        "input_schema":{
            "type":"object",
            "properties":{
                "city":{
                    "type":"string",
                    "description":"City name"
                }
            },
            "required":["city"]
        }
    }
]

# --------------------
# Initial request
# --------------------
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens= 1024,
    tools=tools,
    messages=[
        {
            "role":"user",
            "content":"What is weather in New Delhi?"
        }
    ]
)

# -----------------
# Tool execution
# -----------------
for content in response.content:
    if content.type=="tool_use":
        tool_name = content.name
        tool_input=content.input

        print(f"\nTool called:{tool_name}")
        print(tool_input)

        if tool_name=="get_weather":
            result = get_weather(tool_input["city"])

            # Send tool result back
            final_response= client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=1024,
                tools=tools,
                messages =[
                    {
                        "role":"user",
                        "content":"What is the weather in New Delhi?",

                    },
                    {
                        "role":"assistant",
                        "content":response.content
                    },
                    {
                        "role":"user",
                        "content":[
                            {
                                "type":"tool_result",
                                "tool_use_id":content.id,
                                "content":json.dumps(result)
                            }
                        ]
                    }
                ]
            )
            print("\nFinal Response:\n")
            print(final_response.content[0].text)