from http import client
from socket import *

client = socket(AF_INET, SOCK_STREAM)

client.connect((str(input('Enter IP address: ')), 1303))

data = client.recv(1024)

message = data.decode('utf-8')

print(message)

client.close()
