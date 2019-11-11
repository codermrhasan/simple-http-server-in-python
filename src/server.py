import socket

HOST = '127.0.0.1'
PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Starting server at http://{HOST}:{PORT} ...")

while True:
    client_socket, client_address = server_socket.accept()

    request = client_socket.recv(1024).decode()
    print(request)

    headers = request.split('\n')
    filename = headers[0].split()[1]

    filename == '/index.html' if filename == '/' else filename

    try:
        # file inside public directory. ex. public/index.html
        client_file = open(f'public{filename}')
        file_content = client_file.read()
        client_file.close()

        response = f"HTTP/1.0 200 OK\n\n{file_content}"
    except FileNotFoundError:
        response = 'HTTP/1.0 404 NOT FOUND\n\n<h1>ERROR 404: File Not Found...</h1>'

    client_socket.sendall(response.encode())
    client_socket.close()

server_socket.close()
