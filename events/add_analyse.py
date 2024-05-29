from socket import socket
from server_main import EventHandler
from tkinter import messagebox
from message import Message
from server.db.query import Query


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("add_analyse")

    def handle(self, socket: socket, data):
        nom = data["nom"]
        abrv = data["arbv"]
        description = data["description"]
        prix = data["prix"]
        Query(
            f"INSERT INTO analysis (nom,abreviation,description,prix) VALUES ('{nom}','{abrv}','{description}',{prix});"
        ).commit()

        Message("add_analyse", {}, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("add_analyse")

    def handle(self, socket, data):
        messagebox.showinfo(message="Analyse Ajouter avec Success")
