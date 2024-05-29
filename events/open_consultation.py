from socket import socket
from server_main import EventHandler
from client.windows.medecin.bienvenue import Consulter
from message import Message
from server.db.query import Query
from client.ui import Client


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_consultation")

    def handle(self, socket: socket, data):
        stock = Query(
            "SELECT bilan.id,patient.nom,patient.prenom,patient.sexe,patient.date_naissance,analysis.abreviation FROM bilan LEFT JOIN patient ON bilan.patient_id=patient.id LEFT JOIN analysis ON bilan.analysis_id=analysis.id WHERE bilan.consultation_id IS NULL;"
        ).getAll()
        Message("open_consultation", stock, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_consultation")

    def handle(self, socket, data):
        Client.open_new_window(Consulter(consultations=data))
