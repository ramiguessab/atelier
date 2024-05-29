from socket import socket
from server_main import EventHandler
from client.windows.gerant.employe.edit import EditEmploye
from message import Message
from server.db.query import Query
from client.ui import Client


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_edit_employee")

    def handle(self, socket: socket, data):

        employee_id = data["id"]

        employees = Query(
            f"SELECT employe.utilisateur_id AS id,poste, utilisateur.nom AS nom ,prenom,username,date_entree,date_sortie,password,date_naissance,phone,specialite.nom AS specialite,salaire FROM employe LEFT JOIN utilisateur ON employe.utilisateur_id = utilisateur.id LEFT JOIN specialite ON specialite.utilisateur_id = utilisateur.id WHERE employe.utilisateur_id={employee_id}"
        ).getAll()

        Message("open_edit_employee", employees, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_edit_employee")

    def handle(self, socket, data):
        Client.open_as_dialog(window=EditEmploye(data=data[0]))
