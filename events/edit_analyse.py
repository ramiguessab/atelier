from socket import socket
from server_main import EventHandler
from message import Message
from server.db.query import Query
from tkinter import messagebox


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("edit_analyse")

    def handle(self, socket: socket, data):
        
        analyse_id = data["id"]

        Query(
            f"UPDATE analysis SET nom='{data["nom"]}',abreviation='{data["arbv"]}',prix='{data["prix"]}',description='{data["description"]}' WHERE analysis.id={analyse_id};"
        ).commit()

        Message("edit_analyse", {}, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("edit_analyse")

    def handle(self, socket, data):
        messagebox.showinfo(
            title="Success",
            message="La modification a été apportée à l'analyse que vous avez sélectionné",
        )
