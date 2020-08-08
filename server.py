# server socket
#first, you have to import the modules that will allow you work with sockets

import socket  #(allows you work with sockets)
import sys     #(allows you access cmd commands in your python program)

#create your socket
def create_socket():

#use try excet (like if/else) to try the first and if it has an error, do except
    try:

#create global variables for ip address, port number and your socket variable
        global server_socket
        global host
        global port

#assign your socket to a variable. (you will use this variable to access the multiple functions available in the socket module)
#and assign values to your global variables
        server_socket = socket.socket()
        hostname = socket.gethostname()
        host = socket.gethostbyname(hostname)
        port = 1025
        print('Socket successfully created!')

#if there is an error the program moves to except
    except socket.error as creation_error:
        print(str(creation_error))

#bind the socket
def bind_socket():
    try:
        #import your global variables
        global server_socket
        global host
        global port
        print('Binding to port ' +str(port))
        server_socket.bind((host, port))
        server_socket.listen()

        #create an except condition
    except socket.error as msg:
        print(str(msg))
        bind_socket()

#accept a connection
def accept_client():
    client_socket, client_address = server_socket.accept()
    print(client_address[0], ' Successfully created.' )
    send_commands(client_socket)
    client_socket.close()

#communicate with server
def send_commands(client_socket):
    while True:
        cmd = input('server: ')
        if cmd == 'quit':
            client_socket.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            client_socket.send(str.encode(cmd))
            client_response = str(client_socket.recv(1024), 'utf-8')
            print(client_response, end='')

def main():
    create_socket()
    bind_socket()
    accept_client()

main()





