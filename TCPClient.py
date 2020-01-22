import socket

target_host = "127.0.0.1"
target_port = 9999

# create a socket object
# AF_INET: IPv4, SOCK_STREAM: TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the client
client.connect((target_host, target_port))

# send some data
# message = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
message = "AAABBC"
client.send(message.encode())

# receive some data
response = client.recv(4096)

print(response)