#import libraries
import socket
import datetime

#define address and port
TCP_IP = '127.0.0.1'
TCP_PORT = 5005

#define socket and set it to listen
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
#get date and format accordingly
x = datetime.datetime.now()
x=x.strftime("%m/%d/%Y %I:%M:%S")

#get connection and address
conn, addr = s.accept()

print('Server Address:', TCP_IP)
print('Client Address:', addr)
print("Connection to Client Established, Waiting to Receive Message...")
message = 'What is the current date and time?'
correctReturn ="Current date and time is - "+x
incorrectReturn="ERROR Invalid request try again"
s.listen(1)
#get data from client
data = conn.recv(1024).decode()

#acknowledge request and send a message back
if data == message:
    conn.send(correctReturn.encode())

else:
    conn.send(incorrectReturn.encode())


