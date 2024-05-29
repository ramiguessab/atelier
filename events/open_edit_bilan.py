from socket import socket
from server_main import EventHandler
from client.windows.receptioniste.bilan.edit import EditBilan
from message import Message
from server.db.query import Query
from client.ui import Client


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_edit_bilan")

    def handle(self, socket: socket, data):

        bilan_id = data["id"]

        bilan = Query(
            f"SELECT bilan.id AS bilan_id,analysis.id AS analysis_id, patient.id AS patient_id,analysis.nom AS analyse_nom,analysis.abreviation AS analyse_abreviation,analysis.prix AS analyse_prix,patient.nom,patient.prenom,date_visite FROM bilan LEFT JOIN analysis ON analysis.id=bilan.analysis_id LEFT JOIN patient ON patient.id=bilan.patient_id WHERE bilan.id={bilan_id}"
        ).getAll()

        analyses = Query(f"SELECT * FROM analysis").getAll()

        Message(
            "open_edit_bilan", {"bilan": bilan[0], "analyses": analyses}, socket
        ).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_edit_bilan")

    def handle(self, socket, data):
        Client.open_as_dialog(window=EditBilan(data=data))
