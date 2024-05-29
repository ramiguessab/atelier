from socket import socket
from server_main import EventHandler
from tkinter import messagebox
from message import Message
from server.db.query import Query


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("add_stock")

    def handle(self, socket: socket, data):
        Query(
            f"INSERT INTO stock (nom,quantite,prix_unitaire,date_peremption) VALUES ('{data["nom"]}',{data["quantity"]},{data["prix_unitaire"]},'{data["date_peremption"]}')"
        ).commit()

        Message("add_stock", {}, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("add_stock")

    def handle(self, socket, data):
        messagebox.showinfo(message="Stock Ajouter avec Success")
