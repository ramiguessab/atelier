from socket import socket
from server_main import EventHandler
from client.windows.receptioniste.bilan.bilan import Bilan
from message import Message
from server.db.query import Query
from client.ui import Client


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_receptioniste_bilan")

    def handle(self, socket: socket, data):
        bilans = Query(
            "SELECT bilan.id AS id,patient.nom AS nom,patient.prenom AS prenom,patient.sexe AS sexe,patient.date_naissance AS date_naissance,patient.phone AS phone,bilan.date_visite AS date_visite,analysis.nom AS analysis_name FROM bilan LEFT JOIN patient ON patient.id=bilan.patient_id LEFT JOIN analysis ON analysis.id=bilan.analysis_id"
        ).getAll()
        Message("open_receptioniste_bilan", bilans, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_receptioniste_bilan")

    def handle(self, socket, data):

        Client.open_new_window(Bilan(data=data))
