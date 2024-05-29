import socket
from event_handler import EventHandler
from importlib import import_module
from message import Message
from thread import Thread
import os
import json


class Server:
    events = dict[str, EventHandler]()

    sockets: list[socket.socket] = []

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((self.host, self.port))
            s.listen()
            while True:
                skt = s.accept()
                self.handle_connection(skt)

    @Thread.convert_multi_thread
    def handle_connection(self, skt: tuple[socket.socket, str]):
        conn, addr = skt
        Server.sockets.append(conn)
        with conn:
            print(f"Connected by {addr}")
            while True:
                client_data = conn.recv(1024 * 500)
                if client_data:
                    name, data = client_data.decode().split("|;")
                    if name == "disconnect":
                        Message("disconnect", {}, conn)
                        break
                    handler = Server.events[name]
                    handler.handle(socket=conn, data=json.loads(data))
            print(f"{addr} Disconnected")

    @staticmethod
    def register_handler(event: EventHandler):
        Server.events[event.name] = event


if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 8080
    server_main = Server(HOST, PORT)

    for filename in os.listdir("./events"):
        if "__" not in filename:
            try:
                event_name = filename[:-3]
                event = import_module(f"events.{event_name}")
                Server.register_handler(event.InServer())
            except AttributeError:
                print(f"{filename} event not present in server")
    server_main.start()
