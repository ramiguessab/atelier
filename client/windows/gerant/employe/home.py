from client.dialogs.desconnect_prompt import DesconnectPrompt
import customtkinter
from client.ui import Client
from client.window import Window
from client.windows.gerant.employe.add import AddEmploye


class Employe(Window):
    def __init__(self) -> None:
        super().__init__()

    def build(self, app):
        app.title("Accueil Gerant")
        frame = customtkinter.CTkFrame(master=app)

        customtkinter.CTkLabel(
            master=frame,
            text="Vous trouverez ici tous les employés qui ont travaillé dans le laboratoire",
        ).pack(pady=8)

        customtkinter.CTkButton(
            master=frame, text="Ajouter", command=self.open_add_employe
        ).pack(padx=8)

        frame.pack()

    def open_add_employe(self):
        Client.open_as_dialog(window=AddEmploye())

    def deconnecter(self):
        Client.open_as_dialog(DesconnectPrompt())
