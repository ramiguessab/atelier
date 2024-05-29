from socket import socket
from server_main import EventHandler
from message import Message
from server.db.query import Query
from tkinter import messagebox


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("edit_patient")

    def handle(self, socket: socket, data):
        id = data["id"]
        nom = data["nom"]
        prenom = data["prenom"]
        sexe = data["sexe"]
        date_naissance = data["date_naissance"]
        phone = data["phone"]

        Query(
            f"UPDATE patient SET nom='{nom}',prenom='{prenom}',sexe='{sexe}',date_naissance='{date_naissance}',phone='{phone}' WHERE id={id};"
        ).commit()

        Message("edit_patient", {}, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("edit_patient")

    def handle(self, socket, data):
        messagebox.showinfo(
            title="Success",
            message="La modification a été apportée au patient que vous avez sélectionné",
        )
