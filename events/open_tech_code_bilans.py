from socket import socket
from client.windows.technicien.main import BilansCode
from server_main import EventHandler
from message import Message
from server.db.query import Query
from client.ui import Client


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_tech_code_bilans")

    def handle(self, socket: socket, data):
        nom = data["nom"]
        prenom = data["prenom"]
        analyse_id = data["analyse_id"]

        bilans = Query(
            f"SELECT bilan.id AS id,patient.nom AS nom,patient.prenom AS prenom,patient.date_naissance AS date_naissance,analysis.abreviation AS abreviation,bilan.date_visite AS date_visite FROM bilan LEFT JOIN patient ON bilan.patient_id=patient.id LEFT JOIN analysis ON bilan.analysis_id=analysis.id WHERE bilan.analysis_id={analyse_id} AND patient.nom='{nom}' AND patient.prenom='{prenom}'"
        ).getAll()
        Message("open_tech_code_bilans", bilans, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_tech_code_bilans")

    def handle(self, socket, data):
        Client.open_new_window(BilansCode(bilans=data))
