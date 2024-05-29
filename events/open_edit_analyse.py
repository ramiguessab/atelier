from socket import socket
from client.windows.gerant.analysis_types.edit import EditAnalysis
from server_main import EventHandler
from client.windows.gerant.employe.edit import EditEmploye
from message import Message
from server.db.query import Query
from client.ui import Client


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_edit_analyse")

    def handle(self, socket: socket, data):

        analyse_id = data["id"]

        analyse = Query(
            f"SELECT id,nom,abreviation,prix,description FROM analysis WHERE analysis.id={analyse_id}"
        ).getAll()

        Message("open_edit_analyse", analyse, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_edit_analyse")

    def handle(self, socket, data):
        Client.open_as_dialog(window=EditAnalysis(data=data[0]))
