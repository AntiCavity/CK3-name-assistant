import openai

API_KEY = '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'
openai.api_key = API_KEY

model = 'text-davinci-003'

response = openai.Completion.create(
    prompt='How would someone who speaks Arabic pronounce and spell Rome using the latin alphabet',
    model=model,
    max_tokens=1000,
    temperature=0,
    
)

for result in response.choices:
    print(result.text)
