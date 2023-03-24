import os
import socket
import time

# Creating a bluetooth server socket.
HOST = 'B8:27:EB:BD:F7:9A'
PORT = 8

sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
sock.bind((HOST,PORT))
sock.listen(5)
print("Host Name: ", sock.getsockname())

# Accepting the connection.
client, addr = sock.accept()

#Send File Details
file_name = client.recv(100).decode()
file_size = client.recv(100).decode()

#  Opening and reading file.
with open("/home/pi/Downloads/" + file_name, "wb") as file:
    c = 0
    #Starting the time capture.
    start_time = time.time()
    
    # Running the loop while file is recieved.
    while c <= int(file_size):
        data = client.recv(1024)
        if not (data):
            break
        file.write(data)
        c += len(data)
        
    # Ending the time capture.
    end_time = time.time()
    
print("File transfer Complete.Total time: ", end_time - start_time)

#closing the socket.
sock.close()
