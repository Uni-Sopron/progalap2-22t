from concurrent.futures import thread
import socket
import threading

HOST = "127.0.0.1"  # The server's hostname or IP
PORT = 65432  # The port used by the server

def on_msg(sock):
    while True:
        data = sock.recv(1024).decode('utf-8')
        print('\t'+data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to the server")
    threading.Thread(target=on_msg, args=[s], daemon=True).start()
    while True:
        data = input()
        if not data:
            break
        s.sendall(data.encode('utf-8'))
