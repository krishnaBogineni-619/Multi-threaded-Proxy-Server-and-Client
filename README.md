**Multi-threaded Proxy Server and Client**

This project implements a simple proxy server in Python, which intermediates between a client and a remote server. It enables the client to send HTTP requests via the proxy.


**Features**


**Proxy Server:**

Listens on the specified host (127.0.0.1) and port (8000).
Creates a socket object and binds it to the host and port.
Listens for incoming connections and accepts client connections.
For each client, spawns a new thread to handle requests concurrently.
Receives the client’s URL and makes a request to the URL using the requests library.
Verifies if the request is valid and prepares a response with the URL and validity status.
Logs the request details to a file.
Sends the response back to the client.

**Client:**
Prompts the user to input a URL.
Creates a socket object and connects to the proxy server.
Sends the URL to the proxy server.
Receives and prints the server's response.
Logs the request details to a file.
Repeats the process until the user opts to quit.
