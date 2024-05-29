from socket import socket
from server_main import EventHandler
from tkinter import messagebox
from message import Message
from server.db.query import Query


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("add_consultation")

    def handle(self, socket: socket, data):
        contenu = data["contenu"]
        bilan_id = data["bilan_id"]
        Query(
            f"INSERT INTO consultation (contenu,bilan_id) VALUES ('{contenu}','{bilan_id}');"
        ).commit()

        Message("add_consultation", {}, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("add_consultation")

    def handle(self, socket, data):
        messagebox.showinfo(message="Consultation Ajouter avec Success")
