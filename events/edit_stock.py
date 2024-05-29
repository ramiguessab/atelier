from socket import socket
from server_main import EventHandler
from message import Message
from server.db.query import Query
from tkinter import messagebox


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("edit_stock")

    def handle(self, socket: socket, data):
        stock_id = data["id"]

        Query(
            f"UPDATE stock SET nom='{data["nom"]}',quantite='{data["quantite"]}',prix_unitaire='{data["prix_unitaire"]}',date_peremption='{data["date_peremption"]}' WHERE stock.id={stock_id};"
        ).commit()

        Message("edit_stock", {}, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("edit_stock")

    def handle(self, socket, data):
        messagebox.showinfo(
            title="Success",
            message="La modification a été apportée au stock que vous avez sélectionné",
        )
