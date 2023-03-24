import socket
import os
import time

HOST = 'B8:27:EB:BD:F7:9A'
PORT = 8

sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)


sock.connect((HOST, PORT))
print("Connected Successfully")
#except:
 #   print("Unable to connect")
 #   exit(0)
    
#sock.listen(5)
#client, addr = sock.accept()
    

file_path = '/home/lab4pi/python_practice/pumpjack1.wav'
file_name = 'pumpjack1.wav'
file_size = os.path.getsize('/home/lab4pi/python_practice/pumpjack1.wav')

#send file details
sock.send(file_name.encode())
sock.send(str(file_size).encode())

#open file and send data
with open(file_path, "rb") as file:
    c = 0;
    #start time capturre
    
    start_time = time.time()
    
    #running loop
    while c <= file_size:
        data = file.read(1024)
        if not (data):
            break
        sock.sendall(data)
        c += len(data)
        
    #end time capture
    end_time = time.time()
    
print("File transfer complete. Total time: ", end_time - start_time)

sock.close