from socket import socket
from server_main import EventHandler
from client.windows.receptioniste.dossie_patient.home import PatientFile
from message import Message
from server.db.query import Query
from client.ui import Client


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_receptioniste_patients")

    def handle(self, socket: socket, data):
        patients = Query(
            "SELECT id,nom,prenom,sexe,date_naissance,phone FROM patient ORDER BY id"
        ).getAll()
        Message("open_receptioniste_patients", patients, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_receptioniste_patients")

    def handle(self, socket, data):

        Client.open_new_window(PatientFile(data=data))
