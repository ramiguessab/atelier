from socket import socket
from server_main import EventHandler
from message import Message
from server.db.query import Query
from tkinter import messagebox


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("payee_bilan")

    def handle(self, socket: socket, data):
        bilan_id = data["id"]

        Query(f"UPDATE bilan SET payee=TRUE WHERE id={bilan_id};").commit()

        Message("payee_bilan", {}, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("payee_bilan")

    def handle(self, socket, data):
        messagebox.showinfo(
            title="Success",
            message="Bilan Payee avec success",
        )
