from socket import socket
from server_main import EventHandler
from client.windows.gerant.home import GerantHome
from message import Message
from server.db.query import Query
from client.ui import Client


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("auth_success")

    def handle(self, socket, data):
        gerant_home = GerantHome()
        Client.open_new_window(gerant_home)
