import scratchattach as scratch3
import os
import requests
import time

# Set up OpenAI API credentials
API_KEY = "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"

# Define function to get response from OpenAI API
def ask_gpt(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "prompt": prompt,
        "max_tokens": 1024,
        "temperature": 0.7,
        "n": 1,
        "stop": None
    }

    response = requests.post(
        "https://api.openai.com/v1/engines/davinci/completions",
        headers=headers,
        json=data
    )

    response.raise_for_status()
    message = response.json()["choices"][0]["text"]
    return message.strip()

api_key = os.environ.get('TOKEN')
session = scratch3.Session(api_key, username="iegend-")
conn = session.connect_cloud("863807968") #replace with your project id

client = scratch3.CloudRequests(conn)
@client.request
def foo(argument1):
    print(f"server requested to run {argument1}")
    cmd = argument1
    return ask_gpt(cmd)

client.run()
