from socket import socket
from server_main import EventHandler
from client.dialogs.authentication_failed import NoUserFound
from message import Message
from server.db.query import Query
from client.ui import Client


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("no_user")

    def handle(self, socket, data):
        no_user = NoUserFound()
        Client.open_as_dialog(no_user)
