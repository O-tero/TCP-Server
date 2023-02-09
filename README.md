# TCP Server Implementation

This TCP server is designed to accept and hold a maximum of N clients, where N is configurable. The clients are assigned ranks based on first-come-first-serve, with whoever connects first receiving the next available high rank. Ranks are from 0 to N, where 0 is the highest rank.

Clients can send commands to the server, which the server distributes among the clients. Only a client with a lower rank can execute a command of a higher rank client, while higher rank clients cannot execute commands from lower rank clients. The command execution can be as simple as the client printing to the console that the command has been executed.

In case a client disconnects, the server adjusts the ranks and promotes any client that needs to be promoted to avoid gaps in the ranks.

## Requirements

- Python 3.x
- socket library

## Setup

To run the server, follow these steps:

1. Clone the repository
2. Open terminal and navigate to the directory containing the repository
3. Run the command `python server.py` to start the server
4. Connect clients to the server using a TCP client

##Configuration
The maximum number of clients that the server can hold can be adjusted by changing the value of `MAX_CLIENTS` in the code.

## Code Structure

The server code is structured as follows:

1. Importing the required libraries and defining the maximum number of clients.

2. Creating the server socket and binding it to the desired address and port.

3. Listening for incoming client connections and accepting them.

4. Assigning ranks to clients based on the order of their connection and storing the client information in a list.

5. Receiving commands from clients and distributing them to the appropriate client for execution.

6. Handling disconnection of clients and adjusting the ranks accordingly.

7. Closing the server socket and shutting down the server.

## Conclusion

This TCP server implementation provides a basic framework for managing multiple clients and distributing commands among them.
The ranks of the clients are assigned based on the order of their connection to the server, and the server adjusts the ranks when a client disconnects.
The server is implemented using the socket library in Python and can be easily extended or modified to meet specific requirements.
