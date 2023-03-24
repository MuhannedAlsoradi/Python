import os
import openai

openai.api_key = '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'
model_engine = 'text-davinci-003'
prompt = input('Write your message here:')

completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=200, 
    n=1, 
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)
