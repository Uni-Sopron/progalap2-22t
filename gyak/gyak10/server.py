import socket
import threading
import sys

HOST = ""
PORT = int(sys.argv[1])
CC = 'utf-8'

clients = {}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

def broadcast_message(sender, message):
    for client in clients:
        if client != sender:
            clients[client].sendall(f'{sender} >>> {message}\n'.encode(CC))


def message_handler(name):
    while True:
      message = clients[name].recv(1024)
      if not message:
          break
      message = message.decode(CC).rstrip('\r\n')
      clients[name].sendall('[ACK]\n'.encode(CC))
      broadcast_message(name, message)
      if message == "disconnect":
        clients[name].close()
        break
    del clients[name]
    broadcast_message('[SYS]', f'{name} disconnected')



def initialize_connection(conn, addr):
    conn.sendall('[SYS] Welcome\n[SYS] What is your name?\n'.encode(CC))
    name = conn.recv(1024).decode(CC).rstrip('\r\n')
    conn.sendall(f'[SYS] Hello {name} . Others are: {list(clients.keys())}\n'.encode(CC))
    broadcast_message('[SYS]', f'{name} joined')
    clients[name] = conn
    message_handler(name)

while len(clients) < 5:
    conn, addr = s.accept()
    threading.Thread(target=initialize_connection, args=(conn, addr)).start()


for (conn, addr) in clients:
  conn.close()


s.close()
