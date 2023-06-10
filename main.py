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

api_key = ".eJxVj09LxDAQxb9Lzru1adP82ZvCIoIoKyKsl5I0s21sm6xtSkHxuzuBXvY2vN-8N29-yTLD5PUI5ECeoAVv92RHar3Erk6odhaJLBitFFWIIsyxCaF3ybGGqQd7azC66TEGadLAR9fo6ILPNjBnb3AdNvFhW8bcgEMyGW5yLqlgcGHCKJVLxS0wWQpmBdOHs_-0r8d39_Eou-9n6tyyxuMp8lM3Y8wQWuf37opJtMxoXmVMZVSVqeOgfbvoNhXHUztiv1AIdXQj_ASf5PsRJmx29wJrfcbfbj_r9NzhEq8ELXKry8pyqS9SGKBc5rIoKBeSScsFGF0y8vcPFb9wDQ:1q0MP5:DkmPc69uXm8-Z1d64NWZaTaGNfo"
session = scratch3.Session(api_key, username="iegend-")
conn = session.connect_cloud("863807968") #replace with your project id

client = scratch3.CloudRequests(conn)
@client.request
def foo(argument1):
    print(f"server requested to run {argument1}")
    cmd = argument1
    return ask_gpt(cmd)

client.run()
