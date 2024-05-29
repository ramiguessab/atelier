from socket import socket
from server_main import EventHandler
from tkinter import messagebox
from message import Message
from server.db.query import Query


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("add_patient")

    def handle(self, socket: socket, data):
        nom = data["nom"]
        prenom = data["prenom"]
        sexe = data["sexe"]
        date_naissance = data["date_naissance"]
        phone = data["phone"]

        Query(
            f"INSERT INTO patient (nom,prenom,sexe,date_naissance,phone) VALUES ('{nom}','{prenom}','{sexe}','{date_naissance}','{phone}');"
        ).commit()

        Message("add_patient", {}, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("add_patient")

    def handle(self, socket, data):
        messagebox.showinfo(message="Patient Ajouter avec Success")
