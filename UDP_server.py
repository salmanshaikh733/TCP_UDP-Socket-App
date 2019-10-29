#import libraries
import socket
import datetime

#define ip address and port
UDP_IP_Server = "127.0.0.1"
UDP_PORT_Server = 5004

#define socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#bind socket to ipaddress and port
s.bind((UDP_IP_Server, UDP_PORT_Server))

#get date and time
x = datetime.datetime.now().strftime("%m/%d/%Y %I:%M:%S")

#connect to client
print("Server Address:", UDP_IP_Server)
print("Waiting to Receive Message...")
message = "What is the current date and time?"
correctReturn = "Current date and time is - " + x
incorrectReturn = "ERROR Invalid request try again"

#get data from client
data, addr = s.recvfrom(1024)
data = data.decode()

#acknowledge and send request back
if data == message:
    s.sendto(correctReturn.encode(), (UDP_IP_Server, 5005))
else:
    s.sendto(incorrectReturn.encode(), (UDP_IP_Server, 5005))

