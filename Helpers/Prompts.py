All = [
    {
        "name": "get_current_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. San Francisco, CA",
                },
                "required_aspect":{
                    "type": "string",
                    "description": "The aspect of the weather you want to know, e.g. temperature, humidity, wind speed"
                },
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
            },
            "required": ["location", "required_aspect"],
        },
    },
    {
        "name": "add_to_calendar",
        "description": "Add an event to user's calendar",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {"type": "string", "description": "The title of the event"},
                "start_time": {
                    "type": "string",
                    "description": "The start time of the event",
                },
                "end_time": {
                    "type": "string",
                    "description": "The end time of the event",
                },
            },
            "required": ["title", "start_time", "end_time"],
        },
    },
    {
        "name": "write_email",
        "description": "Write an email to a given recipient, signed by me, Thenu Kaluarachchi.",
        "parameters": {
            "type": "object",
            "properties": {
                "recipient": {
                    "type": "string",
                    "description": "The email address of the recipient",
                },
                "subject": {"type": "string", "description": "The subject of the email"},
                "body": {"type": "string", "description": "The body of the email"},
            },
            "required": ["recipient", "subject", "body"],
        },
    }
]