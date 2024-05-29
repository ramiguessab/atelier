from socket import socket
from server_main import EventHandler
from tkinter import messagebox
from message import Message
from server.db.query import Query


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("add_resultat")

    def handle(self, socket: socket, data):
        echantillon_id = data["echantillon_id"]
        contenu = data["contenu"]
        Query(
            f"INSERT INTO resultat (echantillon_id,contenu) VALUES ('{echantillon_id}','{contenu}');"
        ).commit()

        Message("add_resultat", {}, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("add_resultat")

    def handle(self, socket, data):
        messagebox.showinfo(
            "Succès",
            "Les résultats et observations ont été enregistrés avec succès.",
        )
