from socket import socket
from client.ui import Client
from client.windows.receptioniste.bilan.add import AddBilan
from server_main import EventHandler
from tkinter import messagebox
from message import Message
from server.db.query import Query


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("search_bilan_patient")

    def handle(self, socket: socket, data):

        nom = data["nom"]
        prenom = data["prenom"]
        patient = Query(
            f"SELECT * FROM patient WHERE nom='{nom}' AND prenom='{prenom}'"
        ).getAll()

        analyses = Query(f"SELECT * FROM analysis").getAll()
        Message(
            "search_bilan_patient",
            {"patient": patient, "analyses": analyses},
            socket,
        ).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("search_bilan_patient")

    def handle(self, socket, data):
        if len(data["patient"]) == 0:
            messagebox.showwarning(message="Aucun patient avec ces informations")
        else:
            Client.open_new_window(AddBilan(data=data))
