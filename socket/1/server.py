import socket

HOST = '192.168.0.112'
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket internet in TCP, solo per accettare connessioni
server.bind((HOST, PORT)) # assegna ip e porta ad un'istanza socket

server.listen(3)

while True:
    com_socket, address = server.accept() # .accept ritorna un nuovo oggetto socket, che viene usata per la comunicazione
    print(f'Connected to {address}')
    message = com_socket.recv(1024).decode() # riceve il messaggio trasmesso, recv --> accetta un numero di byte da leggere
    print(f"Message from client {address}: {message}")
    com_socket.send('Message received'.encode('utf-8'))
    com_socket.close()
    print(f'Connection with client {address} ended\n')