from message import Message
from tkinter import messagebox
import customtkinter
from client.ui import Client
from client.window import Window
from client.windows.gerant.employe.add import AddEmploye

from client.components.Table import CTkTable


class Employe(Window):
    def __init__(self, employes=[]) -> None:
        super().__init__("Employees")
        self.employes = employes

    def build(self, app):
        app.title("Accueil Gerant")
        app.geometry("1300x400")
        frame = customtkinter.CTkFrame(master=app)

        customtkinter.CTkLabel(
            master=frame,
            text="Vous trouverez ici tous les employés qui ont travaillé dans le laboratoire",
        ).pack(pady=8)

        self.employees_tables = CTkTable(
            master=frame,
            columns=[
                "Id",
                "Poste",
                "Nom",
                "Prenom",
                "Nom d'utilisateur",
                "Date D'entrie",
                "Date de Sortie",
                "Mot de passe",
                "Date de naissance",
                "Numero de telephone",
                "Specialite",
                "Salerie",
            ],
            rows=self.employes,
        )

        self.employees_tables.pack(pady=4, padx=16)

        actions_frame = customtkinter.CTkFrame(master=frame, fg_color="transparent")
        actions_frame.pack(pady=8, padx=8)

        customtkinter.CTkButton(
            master=actions_frame, text="Modifier", command=self.edit_employe
        ).grid(row=0, column=0, padx=8)
        customtkinter.CTkButton(
            master=actions_frame, text="Ajouter", command=self.open_add_employe
        ).grid(row=0, column=1, padx=8)

        frame.pack()

    def open_add_employe(self):
        Client.open_as_dialog(window=AddEmploye())

    def edit_employe(self):
        selected_employee = self.employees_tables.selected_value.get()
        if not selected_employee:
            messagebox.showwarning(
                title="Selectionner employee",
                message="Il faut spécifier un employé",
            )
        else:
            if Client.socket:
                Message(
                    "open_edit_employee", {"id": selected_employee}, Client.socket
                ).send()
