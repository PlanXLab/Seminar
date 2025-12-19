import socket

TICLE_IP = "192.168.100.122"  # Server IP Address
PORT = 5000                   # Server Port

sock = socket.socket()
sock.connect((TICLE_IP, PORT))
sock.send(b"LED OFF\n")

print(sock.recv(1024).decode().strip())
sock.close()
