import openai
import creds

openai.api_key = creds.API_KEY

model = 'text-davinci-003'

language = input('What language does your character speak? ')

location = input('What location do you wish to rename? ')

prompt = 'How would someone who speaks %s pronounce and spell %s using the latin alphabet?' %(language, location)

#print(prompt)

response = openai.Completion.create(
    prompt=prompt,
    model=model,
    max_tokens=1000,
    temperature=0,
    
)

for result in response.choices:
    print(result.text)