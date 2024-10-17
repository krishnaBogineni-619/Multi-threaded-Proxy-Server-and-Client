import socket
from datetime import datetime

# Proxy server configuration
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000
BUFFER_SIZE = 4096

# Send a URL request to the proxy server
def send_request(url):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the proxy server
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    # Send the URL to the server
    client_socket.sendall(url.encode('utf-8'))

    # Receive and print the response from the server
    response = client_socket.recv(BUFFER_SIZE).decode('utf-8')
    print(response)

    # Save the request details to a file
    with open('requests.log', 'a') as log_file:
        log_file.write(f"Time: {datetime.now()}\nURL: {url}\nResponse: {response}\n\n")

    # Close the socket connection
    client_socket.close()

# Send a request to the proxy server
def make_request():
    url = input("Enter the URL: ")
    send_request(url)

# Make requests until the user decides to quit
# Make requests until the user decides to quit
while True:
    make_request()
    choice = input("Do you want to make another request? (y/n): ")
    if choice.lower() != 'y':
        break
