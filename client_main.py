import socket
from message import Message
from thread import Thread
from event_handler import EventHandler
import json
import os
from importlib import import_module
from client.ui import Client


class ClientSocket(Thread):
    events = dict[str, EventHandler]()

    def __init__(self, host, port, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))

    def run(self):
        while not self.stopped():
            server_data = self.socket.recv(1024 * 500)
            if server_data:
                name, json_data = server_data.decode().split("|;")
                if name == "disconnect":
                    break
                if json_data:
                    data = json.loads(json_data)
                    if name in ClientSocket.events:
                        handler = ClientSocket.events[name]
                        handler.handle(socket=self.socket, data=data)

    @staticmethod
    def register_handler(event: EventHandler):
        ClientSocket.events[event.name] = event


if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 8080

    for filename in os.listdir("./events"):
        if "__" not in filename:
            event_name = filename[:-3]
            try:
                event = import_module(f"events.{event_name}")
                ClientSocket.register_handler(event.InClient())
            except AttributeError:
                print(f"{event_name} event not implemented in client side")

    main_socket = ClientSocket(HOST, PORT)
    main_socket.start()
    Client(main_socket.socket)
    Message("disconnect", {}, main_socket.socket).send()
    main_socket.stop()
