#import libraries
import socket

#define address and time
TCP_IP = '127.0.0.1'
TCP_PORT = 5005

#define socket and connect to server
print("Attempting to contact server at ", TCP_IP, ":", TCP_PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

#get user input for request
print("Connection to Server Established....")
message = 'What is the current date and time?'
val = input("Waiting for request...\n")

#determine if input is valid
if val == message:
    s.sendall(message.encode())
    print(s.recv(1024).decode())

else:
    s.sendall(val.encode())
    print(s.recv(1024).decode())

#close the socket
s.close()
