import socket
import threading
import requests
from datetime import datetime


SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000
BUFFER_SIZE = 4096


def handle_client(client_socket):
 
    url = client_socket.recv(BUFFER_SIZE).decode('utf-8')
    try:
        response = requests.get(url)
        valid = True
    except requests.exceptions.RequestException:
        valid = False

    response_data = f"URL: {url}\nValid: {valid}\n"

    with open('requests.log', 'a') as log_file:
        log_file.write(f"Time: {datetime.now()}\nIP Address: {client_socket.getpeername()[0]}\nURL: {url}\n\n")


    client_socket.sendall(response_data.encode('utf-8'))
    client_socket.close()

def start_proxy_server():
   
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    server_socket.bind((SERVER_HOST, SERVER_PORT))

   
    server_socket.listen(5)
    print(f"Proxy server listening on {SERVER_HOST}:{SERVER_PORT}")

    while True:
        
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address[0]}:{client_address[1]}")


        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()


start_proxy_server()





Aim:
The aim of this project is to develop a multi-threaded proxy server and client system that allows the client to request any URL, fetch the corresponding web content using the server, and save the output as an HTML page with an appropriate name. The system aims to provide an efficient and streamlined approach to fetching web content while ensuring concurrent handling of multiple client connections.

discription:
This project is a simple implementation of a proxy server in Python. The proxy server acts as an intermediary between a client and a remote server, allowing the client to send HTTP requests to the server through the proxy.

The project consists of two parts: the proxy server and the client.

The proxy server:

The server listens on a specified host and port (in this case, '127.0.0.1' and port 8000).
It creates a socket object and binds it to the host and port.
The server listens for incoming connections and accepts client connections.
For each client connection, a new thread is created to handle the client.
The client's URL is received, and a request is made to the URL using the requests library.
The server determines if the request is valid or not and prepares a response containing the URL and validity.
The server logs the request details to a file and sends the response back to the client.
The client:

The client prompts the user to enter a URL.
It creates a socket object and connects to the proxy server.
The client sends the URL to the proxy server.
It receives the response from the proxy server and prints it.
The client logs the request details to a file.
The client repeats the process until the user decides to quit.

Libraries: The code utilizes several Python libraries, including socket, threading, requests, and datetime

Overall, this project demonstrates the basic functionality of a proxy server, allowing clients to access web resources through the server and logging the details of each request.



Implement caching mechanism to store and retrieve frequently accessed web resources, reducing response time.
Add support for handling different types of requests (e.g., POST, PUT, DELETE) in addition to GET requests.
Implement support for handling HTTPS requests by incorporating SSL/TLS encryption and decryption.
Enhance logging functionality to include additional information such as response status codes, request headers, and client user-agent.
Implement authentication and access control mechanisms to restrict access to the proxy server.
Improve error handling by providing detailed error messages and gracefully handling exceptions.



In conclusion, this proxy server project provides a basic implementation of a proxy server in Python. It demonstrates the functionality of handling client requests, making requests to remote servers, and logging request details.

Although the code serves as a starting point, there are several potential enhancements that can be implemented to further improve the proxy server's capabilities, such as caching, handling different types of requests, and implementing security measures.

Client Handling.
Server Setup.

With further development and customization, this proxy server can be expanded to meet specific requirements and provide a more robust and feature-rich solution for proxying and managing web traffic

In conclusion, this Python proxy server project provides a basic implementation of a proxy server that facilitates client requests to remote servers. It demonstrates socket programming, threading, and handling HTTP requests using the requests library. The server logs request details and sends responses back to the clients. It offers potential for further enhancements, such as caching, SSL/TLS support, and access control. Overall, this project serves as a starting point for building more robust and feature-rich proxy server applications.





This code implements a basic proxy server using the Python socket and threading modules. It allows clients to connect to it and fetch the contents of a given URL through the server.

The code can be divided into two main parts: the client handling and the server setup.

Client Handling:

The handle_client function is responsible for processing client requests.
It receives the client socket as a parameter, representing the connection between the server and the client.
It receives the URL from the client using recv and decodes it as a UTF-8 string.
It then uses the requests library to fetch the output of the provided URL.
If the request is successful (no RequestException is raised), it sets the valid flag to True; otherwise, it sets it to False.
It prepares a response string containing the URL and validity status.
It appends the request details (timestamp, client IP address, and URL) to a log file.
It sends the response back to the client using sendall and closes the client socket.
Server Setup:

The start_proxy_server function is responsible for setting up the proxy server.
It creates a socket object using socket.socket and specifies the address family (socket.AF_INET) and socket type (socket.SOCK_STREAM).
It binds the socket to a specific host and port using bind, using the values of SERVER_HOST and SERVER_PORT variables.
It starts listening for incoming connections using listen, with a maximum backlog of 5 pending connections.
It enters an infinite loop to continuously accept client connections.
When a client connection is accepted using accept, it prints the client's address.
It creates a new thread using threading.Thread and passes the handle_client function and the client socket as arguments.
The new thread is started with start, allowing the server to handle multiple clients concurrently.
Overall, this code sets up a simple proxy server that receives client connections, fetches the contents of a URL provided by the client, and returns the result back to the client. It also logs the request details in a file


This code block implements a simple proxy server that allows users to send URL requests through it.

The code defines the server host, port, and buffer size for communication.
The send_request() function creates a socket, connects to the proxy server, sends a URL request, receives and prints the response, and saves the request details to a log file.
The make_request() function prompts the user to enter a URL and calls send_request() to send the request.
The code then enters a loop where it repeatedly makes requests based on user input and asks if the user wants to make another request.
The loop continues until the user enters 'n' to quit, at which point the program breaks out of the loop and terminates.