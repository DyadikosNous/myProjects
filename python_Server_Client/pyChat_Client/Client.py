import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to communicate
port = 12345

# Connect to the server
s.connect(('localhost', port))

# Send and receive messages
while True:
    # Send a message to the server
    msg = input("Client: ")
    s.send(msg.encode())

    # Receive and print the response
    data = s.recv(1024).decode()
    print("From server: " + data)

# Close the connection
s.close()
