import openai
import json
import Helpers.Prompts as Prompts
import Helpers.Functions as Functions
import Credentials.credentials as credentials
openai.organization = credentials.OPENAI_ORGANIZATION_ID
openai.api_key = credentials.OPENAI_API_KEY

def main(): 
    userInput = input("What is your query> ")
    print('Computing...')

    completion = openai.ChatCompletion.create(
        model=credentials.OPENAI_MODEL_ID,
        messages=[{"role": "user", "content": userInput}],
        functions=Prompts.All,
        function_call="auto",
    )
    required_function = completion.choices[0].message.function_call.name
    arguments = completion.choices[0].message.function_call.arguments
    reply_content = completion.choices[0].message
    args = reply_content.to_dict()['function_call']['arguments']
    args = json.loads(args)

    match required_function:
        case "get_current_weather":
            Functions.Functions.get_current_weather(
                locations = args['location'],
                required_aspect = args['required_aspect'],
            )
        case "add_to_calendar":
            Functions.Functions.add_to_calendar(
                title = args['title'],
                start_time = args['start_time'],
                end_time = args['end_time']
            )
        case "write_email":
            Functions.Functions.write_email(
                recipient = args['recipient'],
                subject = args['subject'],
                body = args['body']
            )
        case _:
            print("Function not found")

while True:
    main()