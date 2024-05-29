from socket import socket
from client.windows.gerant.analysis_types.edit import EditAnalysis
from server_main import EventHandler
from client.windows.receptioniste.dossie_patient.edit import EditPatient
from message import Message
from server.db.query import Query
from client.ui import Client


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_edit_patient")

    def handle(self, socket: socket, data):
        patient_id = data["id"]

        analyse = Query(f"SELECT * FROM patient WHERE id={patient_id}").getAll()

        Message("open_edit_patient", analyse, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_edit_patient")

    def handle(self, socket, data):
        Client.open_as_dialog(window=EditPatient(data=data[0]))
