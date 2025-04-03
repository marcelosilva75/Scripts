import socket

IP = "192.x.x.x"  # Your Linux IP
PORT = 443

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP, PORT))
    print("Connected successfully!")
    while True:
        pass  # Keeps the connection open
except Exception as e:
    print(f"Connection failed: {e}")
