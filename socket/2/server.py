import socket
import threading

HOST = '192.168.0.112'
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket internet in TCP, solo per accettare connessioni
server.bind((HOST, PORT)) # assegna ip e porta ad un'istanza socket
server.listen()

def receive(client):
    #while True:
        try:  
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            client.close()
            print('Disconnected')
            #break

def accept():
    while True:
        com_socket, address = server.accept() # .accept ritorna un nuovo oggetto socket, che viene usata per la comunicazione
        print(f'Connected to {address}')

        recive_thread = threading.Thread(target=receive, args=(com_socket,))
        recive_thread.start()

print('Server is waiting for connections\n')
accept()