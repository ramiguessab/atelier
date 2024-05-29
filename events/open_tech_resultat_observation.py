from socket import socket
from tkinter import messagebox
from client.windows.gerant.analysis_types.edit import EditAnalysis
from server_main import EventHandler
from client.windows.technicien.main import ResultatObservation
from message import Message
from server.db.query import Query
from client.ui import Client


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_tech_resultat_observation")

    def handle(self, socket: socket, data):

        code = Query(
            f"SELECT echantillon.id AS id,code,patient.nom,patient.prenom,date_visite FROM echantillon LEFT JOIN bilan ON bilan.id=echantillon.bilan_id LEFT JOIN patient ON patient.id=bilan.patient_id WHERE code='{data["code"]}'"
        ).getAll()

        Message("open_tech_resultat_observation", code, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_tech_resultat_observation")

    def handle(self, socket, data):
        if len(data)>0:
          Client.open_new_window(ResultatObservation(code=data[0]))
        else:
            messagebox.showerror(message="Code n'existe pas")
        
