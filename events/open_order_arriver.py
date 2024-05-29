from socket import socket
from server_main import EventHandler
from client.windows.receptioniste.filedattente.ordreariv import OrderArriver
from message import Message
from server.db.query import Query
from client.ui import Client


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_order_arriver")

    def handle(self, socket: socket, data):
        analyses = Query("SELECT abreviation FROM analysis").getAll()
        Message("open_order_arriver", analyses, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_order_arriver")

    def handle(self, socket, data):
        analysis = list()
        for analyse in data:
            analysis.append(analyse["abreviation"])
        Client.open_new_window(OrderArriver(analyses=analysis))
