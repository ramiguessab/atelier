from socket import socket
from server_main import EventHandler
from client.windows.medecin.bienvenue import AnalysSup
from message import Message
from server.db.query import Query
from client.ui import Client


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_medecin_analyse_sup")

    def handle(self, socket: socket, data):
        analysis = Query("SELECT nom FROM analysis ORDER BY nom").getAll()
        Message("open_medecin_analyse_sup", analysis, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_medecin_analyse_sup")

    def handle(self, socket, data):
        analyses = []

        for analyse in data:
            analyses.append(analyse["nom"])

        Client.open_new_window(AnalysSup(analyses_disponible=analyses))
