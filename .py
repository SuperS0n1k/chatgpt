import scratchattach as scratch3
import os
session = scratch3.Session(".eJxVj09LxDAQxb9Lzru1adP82ZvCIoIoKyKsl5I0s21sm6xtSkHxuzuBXvY2vN-8N29-yTLD5PUI5ECeoAVv92RHar3Erk6odhaJLBitFFWIIsyxCaF3ybGGqQd7azC66TEGadLAR9fo6ILPNjBnb3AdNvFhW8bcgEMyGW5yLqlgcGHCKJVLxS0wWQpmBdOHs_-0r8d39_Eou-9n6tyyxuMp8lM3Y8wQWuf37opJtMxoXmVMZVSVqeOgfbvoNhXHUztiv1AIdXQj_ASf5PsRJmx29wJrfcbfbj_r9NzhEq8ELXKry8pyqS9SGKBc5rIoKBeSScsFGF0y8vcPFb9wDQ:1q0MP5:DkmPc69uXm8-Z1d64NWZaTaGNfo", username="iegend-")
conn = session.connect_cloud("853976819") #replace with your project id

client = scratch3.CloudRequests(conn)
@client.request
def foo(argument1):
    print(f"server requested to run {argument1}")
    cmd = argument1
    return os.popen(cmd).read()

client.run()
