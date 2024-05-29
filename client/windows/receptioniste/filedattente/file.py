# from filedattente.priserdv import priserdv
# from filedattente.ordreariv import ordrarv

import customtkinter
from client.ui import Client
from client.window import Window
from client.windows.receptioniste.filedattente.ordreariv import OrderArriver
from client.windows.receptioniste.filedattente.priserdv import PriseRendezVous
from message import Message


class FileAttente(Window):
    def __init__(self) -> None:
        super().__init__("File D'attente")

    def build(self, root):
        root.title("File d'attente")
        root.geometry("800x250")
        root.resizable(False, False)
        frame = customtkinter.CTkFrame(root)

        lbl1 = customtkinter.CTkLabel(root, text="Bienvenue dans vos tâches")

        prise = customtkinter.CTkButton(
            root,
            text="Prise de rendez-vous",
            command=self.open_prise_de_rendez,
        )
        ordr = customtkinter.CTkButton(
            root,
            text="Met l'ordre d'arrivé des patients",
            command=self.open_order_de_rendez,
        )

        lbl1.pack(padx=8, pady=8)
        prise.pack(padx=8, pady=8, fill="both")
        ordr.pack(padx=8, pady=8, fill="both")

    def open_prise_de_rendez(self):
        Client.open_new_window(PriseRendezVous())

    def open_order_de_rendez(self):
        if Client.socket:
            Message("open_order_arriver", {}, Client.socket).send()
        # Client.open_new_window(OrderArriver(analyses=["HFL"]))
