#
from socket import socket
from server_main import EventHandler
from tkinter import messagebox
from message import Message
from server.db.query import Query


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("take_stock")

    def handle(self, socket: socket, data):

        stock_id = data["stock_id"]
        quantite = data["quantite"]

        print(data)

        Query(
            f"UPDATE stock SET quantite = quantite - {quantite} WHERE id='{stock_id}';"
        ).commit()

        Message("take_stock", {}, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("take_stock")

    def handle(self, socket, data):
        messagebox.showinfo(
            "Enregistrement", "Les données ont été enregistrées avec succès!"
        )
