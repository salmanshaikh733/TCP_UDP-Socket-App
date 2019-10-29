#import libraries
import socket

#define ip and port for client
UDP_IP_Client = "127.0.0.1"
UDP_PORT_Client = 5005

#define ip and port for server
UDP_IP_Server = "127.0.0.1"
UDP_PORT_Server = 5004

#connect to the server
print("Attemping to contact server at, ", UDP_IP_Client, ":", UDP_PORT_Server)
#define socket and bind to ip address and port
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1",5005))

#get user input
print("Connection Established...")
message = "What is the current date and time?"

val = input("Waiting for request...\n")

#determine if message is valid and send it and print out what was received from the server
if val == message:
    s.sendto(message.encode(), (UDP_IP_Client, 5004))
    data, addr = s.recvfrom(1024)
    data = data.decode()
    print(data)
else:
    s.sendto(val.encode(), (UDP_IP_Client, 5004))
    data, addr = s.recvfrom(1024)
    data = data.decode()
    print(data)



