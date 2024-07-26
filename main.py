import openai, sys

# Access the key from the .env file on the root
openai.api_key = sys.argv[1]

response = openai.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "system", "content": "You are a curious assistant."},
        {"role": "user", "content": "Give a funny, weird, curious or random fact about programming that could be actual or historical."}
    ],
    temperature=0.95,
    n=1
)

fact = response.choices[0].message.content

header = '''
# Openai-random-fact
 A fact about programming by OpenAI

[![fact](https://github.com/MarioVidoni/openai-daily-fact/actions/workflows/main.yml/badge.svg)](https://github.com/MarioVidoni/openai-daily-fact/actions/workflows/main.yml)

### Today's fact
# 
'''

f = open('README.md', 'w')
f.write(header + fact)
f.close()
