import openai, os, sys

# Access the key from the .env file on the root
openai.api_key = sys.argv[1]


# Make a completion request to the OpenAI API
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Give a funny, weird or curious fact about programming",
  temperature=0.7,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

fact = response['choices'][0]['text'].replace('\n', '  \n')



header = '''
# openai-random-fact
 A fact about programming by OpenAI

[![fact](https://github.com/MarioVidoni/openai-daily-fact/actions/workflows/main.yml/badge.svg)](https://github.com/MarioVidoni/openai-daily-fact/actions/workflows/main.yml)

### today's fact'''

f = open('README.md', 'w')
f.write(header + "###" + fact)
f.close()

