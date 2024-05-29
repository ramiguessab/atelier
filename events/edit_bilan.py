from socket import socket
from server_main import EventHandler
from message import Message
from server.db.query import Query
from tkinter import messagebox


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("edit_bilan")

    def handle(self, socket: socket, data):

        bilan_id = data["bilan_id"]
        analyse_id = data["analyse_id"]
        patient_id = data["patient_id"]
        date_visite = data["date_visite"]

        Query(
            f"UPDATE bilan SET analysis_id='{analyse_id}',patient_id='{patient_id}',date_visite='{date_visite}' WHERE id={bilan_id};"
        ).commit()

        Message("edit_bilan", {}, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("edit_bilan")

    def handle(self, socket, data):
        messagebox.showinfo(
            title="Success",
            message="La modification a été apportée au bilan que vous avez sélectionné",
        )
