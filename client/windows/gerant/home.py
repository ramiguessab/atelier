import customtkinter
from client.ui import Client
from client.window import Window
from message import Message


class GerantHome(Window):
    def __init__(self) -> None:
        super().__init__("Gerant Home")

    def build(self, app):
        app.geometry("800x300")
        frame = customtkinter.CTkFrame(master=app)

        customtkinter.CTkLabel(master=frame, text="Bienvenue").pack(pady=8)

        customtkinter.CTkButton(
            master=frame, text="Employés", command=self.open_employe_screen
        ).pack(pady=4, padx=16, fill="both")
        customtkinter.CTkButton(
            master=frame, text="Comptabilité", command=self.open_comptabilite_screen
        ).pack(pady=4, padx=16, fill="both")
        customtkinter.CTkButton(
            master=frame, text="Stock", command=self.open_stock
        ).pack(pady=4, padx=16, fill="both")
        customtkinter.CTkButton(
            master=frame, text="Types d'analyses", command=self.open_analysis_type
        ).pack(pady=4, padx=16, fill="both")

        customtkinter.CTkButton(
            master=frame,
            text="Déconnecter",
            fg_color="red",
            hover_color="dark red",
            command=self.deconnecter,
        ).pack(pady=4, padx=16, fill="both")

        frame.pack(
            fill=customtkinter.BOTH,
            pady=16,
            padx=16,
            ipady=8,
            ipadx=16,
            anchor="center",
        )

    def open_employe_screen(self):
        if Client.socket:
            Message("open_gerant_employees", {}, Client.socket).send()

    def open_comptabilite_screen(self):
        if Client.socket:
            Message("open_contabilite_greant", {}, Client.socket).send()

    def open_analysis_type(self):
        if Client.socket:
            Message("open_analyse_types", {}, Client.socket).send()

    def open_stock(self):
        if Client.socket:
            Message("open_gerant_stock", {}, Client.socket).send()

    def deconnecter(self):
        Client.desconnect()
