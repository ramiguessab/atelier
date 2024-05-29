from socket import socket
from client.ui import Client
from client.windows.receptioniste.bilan.add import AddBilan
from client.windows.receptioniste.revenue.pay_bilan import PayBilan
from server_main import EventHandler
from tkinter import messagebox
from message import Message
from server.db.query import Query


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("search_bilan")

    def handle(self, socket: socket, data):

        nom = data["nom"]
        prenom = data["prenom"]
        bilans = Query(
            f"SELECT bilan.id AS id,patient.nom AS nom,patient.prenom AS prenom,patient.sexe AS sexe,patient.date_naissance AS date_naissance,patient.phone AS phone,bilan.date_visite AS date_visite,analysis.nom AS analysis_name FROM bilan LEFT JOIN patient ON patient.id=bilan.patient_id LEFT JOIN analysis ON analysis.id=bilan.analysis_id WHERE patient.nom='{nom}' AND patient.prenom='{prenom}' AND bilan.payee=FALSE"
        ).getAll()

        Message(
            "search_bilan",
            bilans,
            socket,
        ).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("search_bilan")

    def handle(self, socket, data):
        if len(data) == 0:
            messagebox.showwarning(
                message="Aucun bilan non payee avec ces informations"
            )
        else:
            Client.open_new_window(PayBilan(data=data))
