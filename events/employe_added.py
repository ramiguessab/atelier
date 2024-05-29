from socket import socket
from server_main import EventHandler
from client.windows.gerant.home import GerantHome
from message import Message
from server.db.query import Query
from tkinter import messagebox
from client.ui import Client


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("employe_added")

    def handle(self, socket, data):

        messagebox.showinfo(title="Success", message="Employee Ajouter avec success")
