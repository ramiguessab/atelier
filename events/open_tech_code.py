from socket import socket
from client.windows.gerant.analysis_types.edit import EditAnalysis
from server_main import EventHandler
from client.windows.technicien.main import Code
from message import Message
from server.db.query import Query
from client.ui import Client


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_tech_code")

    def handle(self, socket: socket, data):

        analyse = Query(f"SELECT id,abreviation FROM analysis").getAll()

        Message("open_tech_code", analyse, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_tech_code")

    def handle(self, socket, data):
        Client.open_new_window(Code(analyses=data))
