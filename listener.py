import socket

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 8080))
sock.listen(1)

print("Listening for TCP connections on port 8080...")

while True:
    conn, addr = sock.accept() # Accept the connection
    print(f"Connected by {addr}")
    data = conn.recv(4096)
    print(f"Received data: {data}")
    conn.close()
