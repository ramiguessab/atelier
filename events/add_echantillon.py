from socket import socket
from server_main import EventHandler
from tkinter import messagebox
from message import Message
from server.db.query import Query


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("add_echantillon")

    def handle(self, socket: socket, data):
        bilan_id = data["bilan_id"]
        code = data["code"]
        # SELECT * FROM bilan LEFT JOIN patient ON bilan.patient_id=patient.id WHERE bilan.analysis_id=2 AND patient.nom='khelifa' AND patient.prenom='abdelkayoum='
        Query(
            f"INSERT INTO echantillon (bilan_id,code) VALUES ('{bilan_id}','{code}');"
        ).commit()

        Message("add_echantillon", {"code": code}, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("add_echantillon")

    def handle(self, socket, data):
        messagebox.showinfo(message=f"Votre Code {data["code"]}")
