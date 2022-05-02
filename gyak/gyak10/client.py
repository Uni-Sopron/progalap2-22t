import tkinter
import socket
from threading import Thread

HOST = input('Please enter server address: ')
PORT = input('Please enter server port: ')

if not HOST:
    HOST = "localhost"

if not PORT:
    PORT = 1234
else:
  PORT = int(PORT)

CC = "utf-8"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

NAME = input('Please enter your name: ')

if not NAME:
  NAME = 'Anonymous'

def send(*args):
    message = message_text.get()
    clear()
    client_socket.send(message.encode(CC))
    if message == 'disconnect':
      client_socket.close()
      window.quit()


def receive():
    while True:
        try:
          message = client_socket.recv(1024).decode(CC).rstrip('\r\n')
          if message != '[ACK]':
            messages.insert(tkinter.END, message)
        except:
          break

def clear(*args):
  message_text.set("")


def close():
  message_text.set("disconnect")
  send()

window = tkinter.Tk()
window.title('Simple Chat App')
window.geometry('600x600')

message_frame = tkinter.Frame(window)
scrollbar = tkinter.Scrollbar(message_frame)
messages = tkinter.Listbox(message_frame, yscrollcommand=scrollbar.set, font="large")
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
messages.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=tkinter.YES)
message_frame.pack(fill=tkinter.BOTH, expand=tkinter.YES)

message_text = tkinter.StringVar(value='Enter your message here')
message_input = tkinter.Entry(window, textvariable=message_text)
message_input.pack(fill=tkinter.X)

message_input.bind('<FocusIn>', clear)
message_input.bind('<Return>', send)

send_button = tkinter.Button(window, text="Send", command=send)
send_button.pack()

Thread(target=receive).start()
client_socket.send(NAME.encode(CC))

window.mainloop()

close()
