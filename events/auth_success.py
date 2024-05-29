from socket import socket
from server_main import EventHandler
from client.windows.gerant.home import GerantHome
from client.windows.receptioniste.bienvenue import ReciptionisteHome
from client.windows.medecin.bienvenue import Bienvenue as MedecinHome
from client.windows.technicien.main import Bienvenue as TechnicienHome
from message import Message
from server.db.query import Query
from client.ui import Client


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("auth_success")

    def handle(self, socket, data):
        match (data["poste"]):
            case "Gerant":
                gerant_home = GerantHome()
                Client.role = "Gerant"
                Client.open_new_window(gerant_home)
            case "Receptioniste":
                receptioniste_home = ReciptionisteHome()
                Client.role = "Receptioniste"
                Client.open_new_window(receptioniste_home)
            case "Medecin":
                medecin_home = MedecinHome()
                Client.role = "Medecin"
                Client.open_new_window(medecin_home)
            case "Technicien":
                technicien_home = TechnicienHome()
                Client.role = "Technicien"
                Client.open_new_window(technicien_home)
