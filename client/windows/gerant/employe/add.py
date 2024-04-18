from client.dialogs.desconnect_prompt import DesconnectPrompt
import customtkinter
from client.ui import Client
from client.window import Window


class AddEmploye(Window):
    def __init__(self) -> None:
        super().__init__()

    def build(self, app):
        app.title("Accueil Gerant")
        frame = customtkinter.CTkFrame(master=app)
        form_frame = customtkinter.CTkFrame(master=frame)
        actions_frame = customtkinter.CTkFrame(master=frame)

        customtkinter.CTkLabel(
            master=frame,
            text="Entrez les informations du nouvel employé",
        ).grid(row=0, pady=8)
        form_frame.grid(
            row=1,
        )
        actions_frame.grid(
            row=2,
        )

        customtkinter.CTkEntry(master=form_frame, placeholder_text="Nom").pack()
        customtkinter.CTkEntry(
            master=form_frame, placeholder_text="Nom d'utilisateur"
        ).pack()
        customtkinter.CTkEntry(
            master=form_frame, placeholder_text="Mot de passe"
        ).pack()
        customtkinter.CTkEntry(master=form_frame, placeholder_text="Specialite").pack()
        customtkinter.CTkEntry(master=form_frame, placeholder_text="Prénom").pack()
        customtkinter.CTkEntry(
            master=form_frame, placeholder_text="Numéro de téléphone"
        ).pack()
        customtkinter.CTkEntry(master=form_frame, placeholder_text="Salaire").pack()
        roles = ["Receptioniste", "Medicin", "Technicien", "Infermier"]
        customtkinter.CTkOptionMenu(master=form_frame, values=roles).pack()
        customtkinter.CTkEntry(
            master=form_frame, placeholder_text="Date de naissance (DD / MM / YYYY)"
        ).pack()
        customtkinter.CTkEntry(
            master=form_frame, placeholder_text="Date d'entrée (DD / MM / YYYY)"
        ).pack()

        customtkinter.CTkButton(master=actions_frame, text="Effacer").grid(
            row=0, column=0, padx=8
        )
        customtkinter.CTkButton(master=actions_frame, text="Enregistrer").grid(
            row=0, column=1, padx=8
        )

        frame.grid(row=0)

    def deconnecter(self):
        Client.open_as_dialog(DesconnectPrompt())
