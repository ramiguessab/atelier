from socket import socket
from tkinter import messagebox
from client.windows.gerant.analysis_types.edit import EditAnalysis
from server_main import EventHandler
from client.windows.medecin.bienvenue import AjouterConsultation
from message import Message
from server.db.query import Query
from client.ui import Client


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_ajouter_consultation")

    def handle(self, socket: socket, data):

        bilan_id = data["selected_bilan"]

        resultat_contenu = Query(
            f"SELECT contenu,bilan_id FROM echantillon LEFT JOIN resultat ON resultat.echantillon_id=echantillon.id WHERE echantillon.bilan_id={bilan_id}"
        ).getAll()

        Message("open_ajouter_consultation", resultat_contenu, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("open_ajouter_consultation")

    def handle(self, socket, data):
        if len(data) == 0:
            messagebox.showerror(
                message="Ce bilan n'est pas consulter par le technicien"
            )
        else:
            Client.open_as_dialog(AjouterConsultation(contenu_resultat=data[0]))
