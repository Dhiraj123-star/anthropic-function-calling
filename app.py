import json
import os
import urllib.parse
import urllib.request

from dotenv import load_dotenv
from anthropic import Anthropic

# load environment variables
load_dotenv()

# Read API Key
api_key = os.getenv("ANTHROPIC_API_KEY")

# Anthropic Client
client = Anthropic(api_key=api_key)

# ----------------------
# Weather Function
# ----------------------

def get_current_weather(city:str,unit:str="celsius") ->str:

    try: 
        # ----------------
        # Geocoding API
        # ----------------
        geo_url = (
            "https://geocoding-api.open-meteo.com/v1/search"
            f"?name={urllib.parse.quote(city)}&count=1"
        )

        with urllib.request.urlopen(geo_url) as response:
            geo_data= json.loads(response.read().decode())
        
        if "results" not in geo_data:
            return f"City not found: {city}"

        lat= geo_data["results"][0]["latitude"]
        lon= geo_data["results"][0]["longitude"]

        # ----------------
        # Weather API
        # ----------------

        weather_url =  (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={lat}&longitude={lon}&current=temperature_2m"
        )
        with urllib.request.urlopen(weather_url)as response:
            weather_data = json.loads(response.read().decode())

        temp = weather_data["current"]["temperature_2m"]

        return f"Weather in {city}: {temp}°C"
    
    except Exception as ex:
        return f"Error: {ex}"




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
            result = get_current_weather(tool_input["city"])

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