import socket
import threading

HOST = "127.0.0.1"  #  (localhost)
PORT = 65432  # Port to listen on

clients = set()

def handle(conn, addr):
    try:
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                #conn.sendall(data)
                for c in clients:
                    if c != conn:
                        c.sendall(data)
    except:
        pass
    print(f"{addr} disconnected")
    clients.remove(conn)


def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server started on port {PORT}")
        while True:
            conn, addr = s.accept()
            clients.add(conn)
            th = threading.Thread(target=handle, args=[conn, addr], daemon=True)
            th.start()

threading.Thread(target=server, daemon=True).start()
# main thread
input()
