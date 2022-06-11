import socket
from telethon.sync import TelegramClient
from telethon.events import NewMessage
import threading

# config
api_id = 'api_id here as an int'
api_hash = 'api_hash here'
host = ''
port = 65535

conns = []

def socket_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    
    def conn_listener(conn, addr):
        msg = conn.recv(1024).decode()
        if msg == "DISCONNECTING":
            conns.remove(conn)
            print(f'{addr} has left the server')

    while True:
        sock.listen()
        print('listening for client...')
        conn, addr = sock.accept()
        print(f'{addr} connected to this server')
        conns.append(conn)
        connthread = threading.Thread(target=conn_listener, args=(conn, addr))
        connthread.start()

client = TelegramClient('ps5checker', api_id, api_hash)

@client.on(NewMessage(chats='test'))
async def event_hander(event):
    for conn in conns:
        if event.text == "Console Preorder: https://www.nowinstock.net/gett57919":
            conn.send('Nothing, just normal console preorder message'.encode())
        else:
            conn.send(f'PS5 IN STOCK!\nMessage:\n{event.text}'.encode())

t1 = threading.Thread(target=socket_server)
t1.start()
client.start()
client.run_until_disconnected()