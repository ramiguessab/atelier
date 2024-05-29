from tkinter import messagebox
import customtkinter
from client.window import Window
from message import Message
from client.ui import Client

roles = ["Receptioniste", "Medecin", "Technicien"]


class AddEmploye(Window):
    def __init__(self) -> None:
        super().__init__("Add new Employee")

    def build(self, app):
        app.title("Ajouter Employe")
        frame = customtkinter.CTkFrame(master=app)
        form_frame = customtkinter.CTkFrame(master=frame, fg_color="transparent")
        actions_frame = customtkinter.CTkFrame(master=frame)

        ##
        self.name = customtkinter.StringVar()
        self.username = customtkinter.StringVar()
        self.role = customtkinter.StringVar(value=roles[0])
        self.password = customtkinter.StringVar()
        self.speciality = customtkinter.StringVar(value="")
        self.lastname = customtkinter.StringVar()
        self.phone_number = customtkinter.StringVar()
        self.birthdate = customtkinter.StringVar()
        self.enrtydate = customtkinter.StringVar()
        self.salery = customtkinter.StringVar()
        ##

        customtkinter.CTkLabel(
            master=frame,
            text="Entrez les informations du nouvel employé",
        ).grid(row=0)
        form_frame.grid(row=1, padx=16)
        actions_frame.grid(row=2, pady=8, padx=8)

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

        birthdate_frame = customtkinter.CTkFrame(
            master=form_frame, fg_color="transparent"
        )
        birthdate_frame.grid(row=2, column=1, pady=2)
        customtkinter.CTkLabel(master=birthdate_frame, text="Date de naissance:").pack(
            padx=8, pady=2
        )
        customtkinter.CTkEntry(
            master=birthdate_frame,
            placeholder_text="Date de naissance (DD / MM / YYYY)",
            textvariable=self.birthdate,
        ).pack(padx=8, pady=8)

        entrydate_frame = customtkinter.CTkFrame(
            master=form_frame, fg_color="transparent"
        )
        entrydate_frame.grid(row=3, column=1, pady=2)
        customtkinter.CTkLabel(master=entrydate_frame, text="Date d'entrée:").pack(
            padx=8, pady=2
        )
        customtkinter.CTkEntry(
            master=entrydate_frame,
            placeholder_text="Date d'entrée (DD / MM / YYYY)",
            textvariable=self.enrtydate,
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
            master=actions_frame, text="Effacer", command=self.reset
        ).grid(row=0, column=0, padx=8, pady=8)
        customtkinter.CTkButton(
            master=actions_frame, text="Enregistrer", command=self.add_employe
        ).grid(row=0, column=1, padx=8, pady=8)

        frame.grid(row=0, pady=8, padx=8)

    def add_employe(self):
        nom = self.name.get()
        lastname = self.lastname.get()
        role = self.role.get()
        username = self.username.get()
        salery = self.salery.get()
        phone_number = self.phone_number.get()
        birthdate = self.birthdate.get()
        entrydate = self.enrtydate.get()
        speciality = self.speciality.get()
        password = self.password.get()

        if (
            not nom
            or not lastname
            or not role
            or not username
            or not salery
            or not phone_number
            or not birthdate
            or not entrydate
            or not password
        ):
            messagebox.showerror(message="Il faut completer les champs")

        elif role == "Medecin" and speciality == "":
            messagebox.showerror(message="Il faut specifie la specialite")
        else:

            if Client.socket != None:
                Message(
                    "new_employe_data",
                    {
                        "nom": nom,
                        "lastname": lastname,
                        "role": role,
                        "username": username,
                        "salery": salery,
                        "phone_number": phone_number,
                        "birthdate": birthdate,
                        "entrydate": entrydate,
                        "speciality": speciality,
                        "password": password,
                    },
                    Client.socket,
                ).send()

    def reset(self):
        self.name.set("")
        self.lastname.set("")
        self.role.set(roles[0])
        self.username.set("")
        self.salery.set("")
        self.phone_number.set("")
        self.birthdate.set("")
        self.enrtydate.set("")
        self.speciality.set("")
        self.password.set("")
