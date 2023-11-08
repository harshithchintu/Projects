import socket
import threading

# Define the server's address and port
HOST = '127.0.0.1'
PORT = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Function to send messages to the server
def send_message():
    while True:
        message = input()
        client_socket.send(message.encode())

# Function to receive messages from the server
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            print("An error occurred. Disconnecting from the server.")
            client_socket.close()
            break

# Create two threads for sending and receiving messages
send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_messages)

# Start the threads
send_thread.start()
receive_thread.start()
