TOOLS = [
    {
        "name" : "get_current_weather",
        "description": "Get current weather for a city.",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {
                    "type":"string",
                    "description": "City Name"
                }
            },
            "required": ["city"]
        }
    },
    # Anthropic Built-in Web tool
    {
        "type": "web_search_20250305",
        "name": "web_search"
    }
]