import socket
import threading
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8080
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen()
clients = []
def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.send(message.encode())
def handle_client(client_socket, client_address):
    clients.append(client_socket)
    print(f"New connection from {client_address}")
    while True:
        message = client_socket.recv(1024)
        if not message:
            break
        broadcast(message.decode(), client_address)
    clients.remove(client_socket)
    print(f"Disconnected from {client_address}")
    client_socket.close()
def start_server():
    print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}")
    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client,
                                         args=(client_socket, client_address))
        client_thread.start()
start_server()