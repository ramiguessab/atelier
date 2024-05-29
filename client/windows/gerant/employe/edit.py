import datetime
import customtkinter

from client.window import Window
from message import Message
from client.ui import Client

roles = ["Receptioniste", "Medicin", "Technicien", "Infermier"]


class EditEmploye(Window):
    def __init__(self, data) -> None:
        super().__init__("Modifier Employee")
        self.data = data

    def build(self, app):
        app.title("Modifier Employe")
        frame = customtkinter.CTkFrame(master=app)
        form_frame = customtkinter.CTkFrame(master=frame, fg_color="transparent")

        ##
        exit_date: datetime.datetime | None = self.data["date_sortie"]

        self.name = customtkinter.StringVar(value=self.data["nom"])
        self.username = customtkinter.StringVar(value=self.data["username"])
        self.role = customtkinter.StringVar(value=self.data["poste"])
        self.password = customtkinter.StringVar(value=self.data["password"])
        self.speciality = customtkinter.StringVar(value=self.data["specialite"])
        self.lastname = customtkinter.StringVar(value=self.data["prenom"])
        self.phone_number = customtkinter.StringVar(value=self.data["phone"])
        self.exitdate = customtkinter.StringVar(
            value=(
                f"{exit_date.year}-{exit_date.month}-{exit_date.day}"
                if exit_date != None
                else ""
            )
        )
        self.salery = customtkinter.StringVar(value=self.data["salaire"])
        ##

        customtkinter.CTkLabel(
            master=frame,
            text="Entrez les modifications que vous souhaitez",
        ).grid(row=0)
        form_frame.grid(row=1, padx=16)

        name_frame = customtkinter.CTkFrame(master=form_frame, fg_color="transparent")
        name_frame.grid(row=0, column=0, pady=2)
        customtkinter.CTkLabel(master=name_frame, text="Nom:").pack(padx=8, pady=2)
        customtkinter.CTkEntry(
            master=name_frame, placeholder_text="Nom", textvariable=self.name
        ).pack(padx=8, pady=2)

        role_frame = customtkinter.CTkFrame(master=form_frame, fg_color="transparent")
        role_frame.grid(row=1, column=0, pady=2)
        customtkinter.CTkLabel(master=role_frame, text="Role:").pack(padx=8, pady=2)

        customtkinter.CTkOptionMenu(
            master=role_frame, values=roles, variable=self.role
        ).pack(padx=8, pady=2)

        username_frame = customtkinter.CTkFrame(
            master=form_frame, fg_color="transparent"
        )
        username_frame.grid(row=2, column=0, pady=2)
        customtkinter.CTkLabel(master=username_frame, text="Nom d'utilisateur:").pack(
            padx=8, pady=2
        )
        customtkinter.CTkEntry(
            master=username_frame,
            placeholder_text="Nom d'utilisateur",
            textvariable=self.username,
        ).pack(padx=8, pady=2)

        password_frame = customtkinter.CTkFrame(
            master=form_frame, fg_color="transparent"
        )
        password_frame.grid(row=3, column=0, pady=2)
        customtkinter.CTkLabel(master=password_frame, text="Mot de passe:").pack(
            padx=8, pady=2
        )
        customtkinter.CTkEntry(
            master=password_frame,
            placeholder_text="Mot de passe",
            textvariable=self.password,
        ).pack(padx=8, pady=2)

        speciality_frame = customtkinter.CTkFrame(
            master=form_frame, fg_color="transparent"
        )
        speciality_frame.grid(row=4, column=0, pady=2)
        customtkinter.CTkLabel(master=speciality_frame, text="Specialite:").pack(
            padx=8, pady=2
        )
        customtkinter.CTkEntry(
            master=speciality_frame,
            placeholder_text="Specialite",
            textvariable=self.speciality,
        ).pack(padx=8, pady=2)
        ####

        lastname_frame = customtkinter.CTkFrame(
            master=form_frame, fg_color="transparent"
        )
        lastname_frame.grid(row=0, column=1, pady=2)
        customtkinter.CTkLabel(master=lastname_frame, text="Prénom:").pack(
            padx=8, pady=2
        )
        customtkinter.CTkEntry(
            master=lastname_frame, placeholder_text="Prenom", textvariable=self.lastname
        ).pack(padx=8, pady=8)

        phone_frame = customtkinter.CTkFrame(master=form_frame, fg_color="transparent")
        phone_frame.grid(row=1, column=1, pady=2)

        customtkinter.CTkLabel(master=phone_frame, text="Numero de Telephone:").pack(
            padx=8, pady=2
        )
        customtkinter.CTkEntry(
            master=phone_frame,
            placeholder_text="Numéro de téléphone",
            textvariable=self.phone_number,
        ).pack(padx=8, pady=8)

        entrydate_frame = customtkinter.CTkFrame(
            master=form_frame, fg_color="transparent"
        )
        entrydate_frame.grid(row=3, column=1, pady=2)
        customtkinter.CTkLabel(master=entrydate_frame, text="Date de sortie:").pack(
            padx=8, pady=2
        )
        customtkinter.CTkEntry(
            master=entrydate_frame,
            placeholder_text="Date de sortie (DD / MM / YYYY)",
            textvariable=self.exitdate,
        ).pack(padx=8, pady=8)

        salery_frame = customtkinter.CTkFrame(
            master=form_frame,
            fg_color="transparent",
        )
        salery_frame.grid(row=4, column=1, pady=2)
        customtkinter.CTkLabel(master=salery_frame, text="Salaire:").pack(
            padx=8, pady=2
        )
        customtkinter.CTkEntry(
            master=salery_frame, placeholder_text="Salaire", textvariable=self.salery
        ).pack(padx=8, pady=8)

        customtkinter.CTkButton(
            master=frame, text="Enregistrer", command=self.edit_employe
        ).grid(row=2, padx=8, pady=8)

        frame.grid(row=0, pady=8, padx=8)

    def edit_employe(self):
        nom = self.name.get()
        lastname = self.lastname.get()
        role = self.role.get()
        username = self.username.get()
        salery = self.salery.get()
        phone_number = self.phone_number.get()
        exitdate = self.exitdate.get()
        speciality = self.speciality.get()
        password = self.password.get()

        if Client.socket != None:
            Message(
                "edit_employee",
                {
                    "id": self.data["id"],
                    "nom": nom,
                    "prenom": lastname,
                    "role": role,
                    "username": username,
                    "salery": salery,
                    "phone_number": phone_number,
                    "exit_date": exitdate,
                    "speciality": speciality,
                    "password": password,
                },
                Client.socket,
            ).send()
