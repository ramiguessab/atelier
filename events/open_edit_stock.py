from socket import socket
from server_main import EventHandler
from client.windows.gerant.stock.edit import EditStock
from message import Message
from server.db.query import Query
from client.ui import Client


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_edit_stock")

    def handle(self, socket: socket, data):

        stock_id = data["id"]

        stock = Query(
            f"SELECT id,nom,quantite,prix_unitaire,date_peremption FROM stock WHERE stock.id={stock_id}"
        ).getAll()

        Message("open_edit_stock", stock, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_edit_stock")

    def handle(self, socket, data):
        Client.open_as_dialog(window=EditStock(data=data[0]))
