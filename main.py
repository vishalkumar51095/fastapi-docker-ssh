# main.py
from fastapi import FastAPI

app = FastAPI()

import paramiko


def ssh_into_container():
    # SSH connection details
    hostname = 'localhost'
    port = 2222
    username = 'docker'
    password = 'docker'

    # Create an SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the container
        ssh.connect(hostname, port, username, password)
        print("Connected to the container via SSH")

        # Execute a command inside the container
        stdin, stdout, stderr = ssh.exec_command('ls -l')
        print("Command output:\n", stdout.read().decode())

    except paramiko.SSHException as e:
        print(f"SSH connection failed: {e}")
    finally:
        # Close the connection
        ssh.close()
        print("SSH connection closed")


@app.get("/")
def read_root():
    return {"Hello": "World"}
