from openai import OpenAI
import sys

#
client = OpenAI(
    api_key = sys.argv[1]
)

try:
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a creative and knowledgeable assistant that shares fun and interesting programming facts."},
            {"role": "user", "content": "Give me a unique fact or curiosity about any engineering discipline that hasn’t been shared before and please don't greet me, just give me the fact"}
        ],
        temperature=1.0, 
        max_tokens=100,  
        presence_penalty=1.0, 
        frequency_penalty=0.5,  
        n=1, 
    )

    fact = completion.choices[0].message.content

except Exception as e:
    fact = "There seems to be an issue with the OpenAI API configuration. We're working on fixing it—thanks for your patience! 😊"

header = '''
    # Openai-random-fact
    A fact about Engineering by OpenAI

    [![fact](https://github.com/MarioVidoni/openai-daily-fact/actions/workflows/main.yml/badge.svg)](https://github.com/MarioVidoni/openai-daily-fact/actions/workflows/main.yml)

    ### Today's fact
    # 
    '''

f = open('README.md', 'w')
f.write(header + fact)
f.close()

