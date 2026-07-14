import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('0.0.0.0', 8080)
sock.bind(server_address)

print("Listening for UDP packets on port 8080...")

while True:
    data, address = sock.recvfrom(4096)
    print(f"Received {len(data)} bytes from {address}/n")
    print(f"Data: {data}/n/n/n")
