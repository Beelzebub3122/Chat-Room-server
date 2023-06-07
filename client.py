import time
import socket

print('Client Server...')
time.sleep(1)

soc = socket.socket()

# Specify the server's IP address and port number
server_host = "127.0.0.1"
port = 1234

print('Trying to connect to the server: {}, ({})'.format(server_host, port))
time.sleep(1)
soc.connect((server_host, port))
print("Connected...\n")

name = input('Enter Client\'s name: ')
soc.send(name.encode())

server_name = soc.recv(1024)
server_name = server_name.decode()
print('{} has joined...'.format(server_name))
print('Enter [bye] to exit.')

while True:
  message = soc.recv(1024)
  message = message.decode()
  print(server_name, ">", message)

  message = input(str("Me > "))

  if message == "[bye]":
    message = "Leaving the Chat room"
    soc.send(message.encode())
    print("\n")
    break

  soc.send(message.encode())

