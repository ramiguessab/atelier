from socket import socket
from server_main import EventHandler

from client.windows.gerant.analysis_types.home import AnalysisType
from message import Message
from server.db.query import Query
from client.ui import Client


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_analyse_types")

    def handle(self, socket: socket, data):
        analyses = Query(
            "SELECT id,nom,abreviation,description,prix FROM analysis ORDER BY id"
        ).getAll()

        Message("open_analyse_types", analyses, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_analyse_types")

    def handle(self, socket, data):
        Client.open_new_window(AnalysisType(analyses=data))
