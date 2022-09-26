from socket import *
import datetime as dt

server = socket(
    AF_INET, SOCK_STREAM
)
time = dt.datetime.now()

server.bind(('', 1303))

while True:
    server.listen()
    user, addr = server.accept()
    user.send(str(time.strftime("%Y.%m.%d %H:%M")).encode('utf-8'))
    user.close()
    
