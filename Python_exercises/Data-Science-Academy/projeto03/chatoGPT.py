import openai
import json


def getChatoGptResponse(prompt, maxTokens=150, amountOfConclusions=5, temperature=0.8):
    response = client.chat.completions.create(
        messages=[
             {
                  "role": "user",
                  "contet": prompt,
             }
        ],
        model="gpt-3.5-turbo",

        max_tokens = maxTokens,
        n = amountOfConclusions,
        stop= None,
        temperature = temperature
    )

    return response.choices[0].text.strip()


with open("./projeto03/secrets.json") as secrets:
    client = openai.OpenAI(
         api_key=json.load(secrets)["openAi"]
    )

print("Welcome travaler! To -- ChatoGPT --, a uninspired and honestly pretty useless use for the ChatGPT API.")
print("Type 'exit or press ctrl+c to close the application.'")

while True:
    user_input = input('\nYou: ')

    if user_input.lower() == "exit":
            break
    
    prompt = f'\nUser: {user_input}\nChatoGPT:'
    chatogpt_response = getChatoGptResponse(prompt)

    print(f"\nChatoGPT: {chatogpt_response}")

