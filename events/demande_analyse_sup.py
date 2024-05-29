from socket import socket
from client.ui import Client
from server_main import EventHandler, Server
from tkinter import messagebox
from message import Message
from server.db.query import Query


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("demande_analyse_sup")

    def handle(self, socket: socket, data):
        prenom = data["prenom"]
        nom = data["nom"]
        type_analyse = data["type_analyse"]
        contenu = data["contenu"]
        for broadcasted_socket in Server.sockets:
            Message(
                "demande_analyse_sup",
                {
                    "prenom": prenom,
                    "nom": nom,
                    "type_analyse": type_analyse,
                    "contenu": contenu,
                },
                broadcasted_socket,
            ).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("demande_analyse_sup")

    def handle(self, socket, data):
        if Client.role and Client.role == "Receptioniste":
            prenom = data["prenom"]
            nom = data["nom"]
            type_analyse = data["type_analyse"]
            contenu = data["contenu"]
            messagebox.showinfo(message="Analyse Suplementaire demander")
