import socket
from playsound import playsound

server_ip = ''
port = 65535
alarm = 'path/to/alarm'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_ip, port))
print('connected to server!')

while True:
    try:
        message = sock.recv(1024).decode()
        print(message)
        if message != 'Nothing, just normal console preorder message':
            while True:
                playsound(alarm)
    except KeyboardInterrupt:
        sock.send('DISCONNECTING'.encode())
        break