from socket import socket
from tkinter import messagebox
from server_main import EventHandler
from client.windows.gerant.contability.home import Comptabilite
from message import Message
from server.db.query import Query
from client.ui import Client


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_contabilite_greant")

    def handle(self, socket: socket, data):
        somme = Query(
            "SELECT SUM(analysis.prix) AS somme FROM bilan LEFT JOIN analysis ON bilan.analysis_id=analysis.id WHERE bilan.payee IS TRUE AND date_trunc('month', bilan.date_visite) = date_trunc('month', current_timestamp)"
        ).getAll()
        Message("open_contabilite_greant", somme, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_contabilite_greant")

    def handle(self, socket, data):
        if not data[0]["somme"]:
            messagebox.showwarning(message="Vous avez aucun revenues cet mois")
        else:
            Client.open_new_window(Comptabilite(somme=data[0]))
