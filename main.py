import scratchattach as scratch3
import os
api_key = os.environ.get('TOKEN')
session = scratch3.Session(api_key, username="iegend-")
conn = session.connect_cloud("853976819") #replace with your project id

client = scratch3.CloudRequests(conn)
@client.request
def foo(argument1):
    print(f"server requested to run {argument1}")
    cmd = argument1
    return os.popen(cmd).read()

client.run()
