import socket
import threading


class Server:
    def __init__(self, host, port, max_clients):
        self.host = host
        self.port = port
        self.max_clients = max_clients
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()
        self.clients = []
        self.ranks = {}

    def broadcast(self, message, client):
        for c in self.clients:
            if c != client:
                c.send(message)

    def handle(self, client):
        name = client.recv(1024).decode("utf-8")
        print(f"Connected client: {name}")
        client.send(bytes(f"Welcome {name}!", "utf-8"))
        rank = len(self.clients)
        self.ranks[client] = rank
        message = bytes(f"{name} has joined the chat! (Rank {rank})", "utf-8")
        self.broadcast(message, client)
        self.clients.append(client)
        while True:
            message = client.recv(1024)
            if not message:
                print(f"Disconnected client: {name}")
                self.clients.remove(client)
                del self.ranks[client]
                broadcast_message = bytes(
                    f"{name} has left the chat!", "utf-8")
                self.broadcast(broadcast_message, client)
                break
            else:
                message = message.decode("utf-8")
                rank_received = int(message.split()[-1])
                rank_client = self.ranks[client]
                if rank_received > rank_client:
                    client.send(bytes(
                        "Command rejected. Higher rank clients cannot execute lower rank client's commands.", "utf-8"))
                elif rank_received < rank_client:
                    self.broadcast(
                        bytes(f"{name} executed command: {message}", "utf-8"), client)
                else:
                    client.send(
                        bytes("Command rejected. Clients cannot execute their own commands.", "utf-8"))

    def receive(self):
        while True:
            client, address = self.server.accept()
            print(f"Accepted connection from {str(address)}")
            client.send(bytes("Enter your name:", "utf-8"))
            client.send(bytes(str(self.ranks), "utf-8"))
            client_thread = threading.Thread(
                target=self.handle, args=(client,))
            client_thread.start()

    def start(self):
        print("Starting server...")
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()


server = Server("0.0.0.0", 8080, 3)
server.start()
