import threading
import grpc
import argparse
import os

import werewolves_pb2 as chat
import werewolves_pb2_grpc as rpc

address = 'localhost'
port = 11912


class Client:

    def __init__(self, u: str, p: str):
        self.username = u
        self.password = p
        channel = grpc.insecure_channel(f'{address}:{port}')
        self.conn = rpc.ChatServerStub(channel)
        threading.Thread(target=self.__listen_for_messages, daemon=True).start()

    def __listen_for_messages(self):
        for note in self.conn.ChatStream(chat.Name(name=self.username)):
            results = ["Townspeople Win", "Werewolves Win"]
            print(f"[{note.name}] {note.message}")
            if note.message in results: os._exit(1)
            if note.message.split()[0] == self.username: os._exit(1)

    def send_message(self, message):
        if message:
            n = chat.Message()
            n.name = self.username
            n.message = message
            self.conn.HandleMessage(n)

    def connect(self):
        c = chat.Credentials()
        c.username = self.username
        c.password = self.password
        res = self.conn.Connect(c)
        return res.message

    def run(self):
        res = self.connect()
        if not res == "Connected successfully":
            print(res)
            return
        print("Client connected, game will start soon...")
        try:
            while True:
                message = input()
                if message.lower() == 'quit':
                    print("Exiting chat...")
                    break
                self.send_message(message)
        except KeyboardInterrupt:
            print("Exited by user")



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Connect to Werewolves server")
    parser.add_argument('username', type=str, help="Username for connection")
    parser.add_argument('password', type=str, help="Password for connection")
    args = parser.parse_args()
    client = Client(args.username, args.password)
    client.run()
