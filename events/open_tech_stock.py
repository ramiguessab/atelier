from socket import socket
from server_main import EventHandler
from client.windows.technicien.main import Stock
from message import Message
from server.db.query import Query
from client.ui import Client


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_tech_stock")

    def handle(self, socket: socket, data):
        stock = Query(f"SELECT * FROM stock").getAll()

        Message("open_tech_stock", stock, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_tech_stock")

    def handle(self, socket, data):
        Client.open_new_window(Stock(stock=data))
