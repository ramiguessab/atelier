from socket import socket
from server_main import EventHandler
from tkinter import messagebox
from message import Message
from server.db.query import Query


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("add_bilan")

    def handle(self, socket: socket, data):
        analyse_id = data["analyse_id"]
        patient_id = data["patient_id"]
        date_visite = data["date_visite"]
        Query(
            f"INSERT INTO bilan (patient_id,analysis_id,date_visite) VALUES ('{patient_id}','{analyse_id}','{date_visite}');"
        ).commit()

        Message("add_bilan", {}, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("add_bilan")

    def handle(self, socket, data):
        messagebox.showinfo(message="Bilan Ajouter avec Success")
