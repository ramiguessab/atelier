from socket import socket
from server_main import EventHandler
from tkinter import messagebox
from message import Message
from server.db.query import Query


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("delete_analyse")

    def handle(self, socket: socket, data):
        Query(
            f"DELETE FROM analysis WHERE id={data["id"]}"
        ).commit()

        Message("delete_analyse", {}, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("delete_analyse")

    def handle(self, socket, data):
        messagebox.showinfo(message="Suppresion Success")
