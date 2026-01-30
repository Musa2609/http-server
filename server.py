import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


HOST = "127.0.0.1"
PORT = 8080
server_socket.bind((HOST, PORT))


server_socket.listen(5)
print(f"Server running on http://{HOST}:{PORT}")


while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

   
    request = client_socket.recv(1024).decode("utf-8")
    print("----- REQUEST -----")
    print(request)

    if not request:
        client_socket.close()
        continue

    # 6. Parse request line
    request_line = request.splitlines()[0]
    method, path, version = request_line.split()

    # 7. Routing
    if path == "/":
        body = "<h1>Hello from my HTTP Server</h1>"
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n"
            f"Content-Length: {len(body)}\r\n"
            "\r\n"
            f"{body}"
        )

    elif path == "/health":
        body = '{"status": "running"}'
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: application/json\r\n"
            f"Content-Length: {len(body)}\r\n"
            "\r\n"
            f"{body}"
        )

    else:
        body = "404 Not Found"
        response = (
            "HTTP/1.1 404 Not Found\r\n"
            "Content-Type: text/plain\r\n"
            f"Content-Length: {len(body)}\r\n"
            "\r\n"
            f"{body}"
        )

    # 8. Send response
    client_socket.sendall(response.encode("utf-8"))

    # 9. Close connection
    client_socket.close()
