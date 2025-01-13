import openai

from dotenv import load_dotenv
import os
load_dotenv()
key=os.getenv("key")
def MOM(data):
    API_KEY = key
    api_key = key

    # Set the API key
    openai.api_key = api_key
    with open(data,'rb') as f:
        data=f.read()

    from openai import OpenAI
    keyclient = OpenAI(api_key=api_key)
    MODEL="gpt-4o"
    completion = keyclient.chat.completions.create( 
        model=MODEL,  messages=[    {"role": "system", "content": f"You are a helpful assistant that create  Minutes of Meeting based on the conversation"},    
                        {"role": "user", "content": f"create minutes of meeting for this conversation in proper way{data} "}  ])
    # print("Assistant: " + completion.choices[0].message.content)
    data=completion.choices[0].message.content
    with open('MoM.txt','w') as m:
        m.write(data)




