import scratchattach as scratch3

session = scratch3.login("Iegend-", "kitloin")
conn = session.connect_cloud("853976819") #replace with your project id

client = scratch3.CloudRequests(conn)

@client.request
def foo(argument1):
    print(f"server requested to run {argument1}")
    cmd = argument1
    return eval(cmd)

client.run()
