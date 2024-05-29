from socket import socket
from server_main import EventHandler
from message import Message
from server.db.query import Query


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("authentication_data")

    def handle(self, socket: socket, data):

        poste = data["poste"]
        username = data["username"]
        password = data["password"]
        poste = data["poste"]

        query = Query(
            f"""SELECT * FROM utilisateur WHERE 
                        username='{username}'
                        AND password='{password}' 
                        AND poste='{poste}'""",
        )
        query_result = query.getAll()

        if len(query_result) >= 1:
            Message("auth_success", query_result[0], socket).send()
        else:
            Message("no_user", {}, socket).send()
