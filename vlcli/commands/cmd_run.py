import click
import socket
import webbrowser

@click.command()
@click.argument("filename", type=str)
def cli(filename):
    SERVER_HOST = '0.0.0.0'
    SERVER_PORT = 8000
    if filename.endswith('.html'):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((SERVER_HOST, SERVER_PORT))
        server_socket.listen(1)
        print('Listening on port %s ...' % SERVER_PORT)
        webbrowser.open('http://localhost:8000/'+filename, new=2)
        while True:    
    # Wait for client connections
            client_connection, client_address = server_socket.accept()
            
    # Get the client request
            request = client_connection.recv(1024).decode()
            print(request)
            file_name = open(filename)
            content = file_name.read()
            file_name.close()
            
    # Send HTTP response
            response = 'HTTP/1.0 200 OK\n\n' + content
            client_connection.sendall(response.encode())
            client_connection.close()
    else: 
        print("Invalid file format")


 
