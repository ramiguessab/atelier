from client.dialogs.desconnect_prompt import DesconnectPrompt
import customtkinter
from client.ui import Client
from client.window import Window


class GerantHome(Window):
    def __init__(self) -> None:
        super().__init__()

    def build(self, app):
        app.title("Accueil Gerant")
        app.geometry("800x300")
        frame = customtkinter.CTkFrame(master=app)

        customtkinter.CTkLabel(master=frame, text="Bienvenue").pack(pady=8)

        customtkinter.CTkButton(master=frame, text="Employés").pack(
            pady=4, padx=16, fill="both"
        )
        customtkinter.CTkButton(master=frame, text="Comptabilité").pack(
            pady=4, padx=16, fill="both"
        )
        customtkinter.CTkButton(master=frame, text="Types d'analyses").pack(
            pady=4, padx=16, fill="both"
        )
        customtkinter.CTkButton(master=frame, text="Rapports").pack(
            pady=4, padx=16, fill="both"
        )

        customtkinter.CTkButton(
            master=frame,
            text="Déconnecter",
            fg_color="#990000",
            hover_color="#660000",
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

    def deconnecter(self):
        Client.open_as_dialog(DesconnectPrompt())
