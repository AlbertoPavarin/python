import socket

HOST = '192.168.0.112'
PORT = 8080

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

message = input('Send message: ')

socket.send(message.encode('utf-8'))
print(socket.recv(1024).decode())