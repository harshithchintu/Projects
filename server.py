import socket
import threading

# Define the server's address and port
HOST = '127.0.0.1'
PORT = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

# List to store client connections
clients = []

# Function to broadcast messages to all connected clients
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                # Remove the client if unable to send a message
                clients.remove(client)

# Function to handle client connections
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                # Remove the client if no data received
                clients.remove(client_socket)
                break
            broadcast(message, client_socket)
        except:
            # Remove the client if an error occurs
            clients.remove(client_socket)
            break

# Accept incoming connections and create threads for each client
print("Server is listening on {}:{}".format(HOST, PORT))
while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)
    print("New connection from {}".format(client_address))
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
