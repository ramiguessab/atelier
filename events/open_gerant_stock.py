from socket import socket
from server_main import EventHandler
from client.windows.gerant.stock.home import Stock
from message import Message
from server.db.query import Query
from client.ui import Client


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_gerant_stock")

    def handle(self, socket: socket, data):
        stock = Query(
            "SELECT id,nom,quantite,prix_unitaire,date_peremption FROM stock ORDER BY id"
        ).getAll()
        Message("open_gerant_stock", stock, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_gerant_stock")

    def handle(self, socket, data):
        Client.open_new_window(Stock(stock=data))
