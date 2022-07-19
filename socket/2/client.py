import socket
import threading

HOST = '192.168.0.112'
PORT = 8080

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

def receive():
    while True:
        try:
            print(socket.recv(1024).decode('utf-8'))
        except:
            socket.close()
            break

def send():
    while True:
        socket.send(input('Send message: ').encode('utf-8'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()