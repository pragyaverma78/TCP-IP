import socket

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server.bind(("127.0.0.1",8080))
server.listen()

print("Server is waiting...")

conn, addr = server.accept()

print("Connected:", addr)

data = conn.recv(1024)

print("Received:", data.decode())

conn.send("Hello Client".encode())

conn.close()
server.close()