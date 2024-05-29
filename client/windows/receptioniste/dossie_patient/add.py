import customtkinter
from tkinter import messagebox
from client.ui import Client
from client.window import Window
from message import Message

# from patientpatadd.patientpatientajouter import patpatadd

analyse = [
    "NFS",
    "ALAT",
    "ASLO",
    "CREA",
    "GPP",
    "VDRL",
    "BILI.INDIRECTE",
    "CALCIUM",
    "GGT",
    "HDL",
    "MAGAN",
    "TP",
    "TRIGLYCERIDES",
    "ACIDE URIQUE",
    "ASAT",
    "BILI DIRECTE",
    "BILI.TOTAL",
    "CHOL.TOTAL",
    "CRP",
    "GAP",
    "GROUPAGE",
    "LDL",
    "TCK",
    "TPHO",
    "UREE",
    "VS",
]


class AddPatient(Window):
    def __init__(self) -> None:
        super().__init__("Ajouter Patient")

    def build(self, root):
        root.title("Les Patiens")

        root.geometry("300x400")
        root.resizable(False, False)

        frame = customtkinter.CTkFrame(root)

        lbl1 = customtkinter.CTkLabel(
            root,
            text="Entrez les informations de patient",
        )

        nom = customtkinter.CTkLabel(
            frame,
            text="Nom:",
        )
        pre = customtkinter.CTkLabel(
            frame,
            text="Prénom:",
        )

        customtkinter.CTkLabel(
            frame,
            text="Genre:",
        ).grid(row=3, column=0, padx=4, pady=8)
        self.genre = customtkinter.StringVar(value="Male")
        customtkinter.CTkOptionMenu(
            master=frame, values=["Male", "Female"], variable=self.genre
        ).grid(row=4, column=0, padx=4, pady=8)

        customtkinter.CTkLabel(
            frame,
            text="Date de naissance:",
        ).grid(row=5, column=0, padx=4, pady=8)
        self.date_naissance = customtkinter.StringVar(value="")
        customtkinter.CTkEntry(
            textvariable=self.date_naissance,
            master=frame,
        ).grid(row=6, column=0, padx=4, pady=8)

        self.nomentr = customtkinter.StringVar(value="")
        nomentr = customtkinter.CTkEntry(
            textvariable=self.nomentr,
            master=frame,
        )
        self.preentr = customtkinter.StringVar(value="")
        preentr = customtkinter.CTkEntry(
            master=frame,
            textvariable=self.preentr,
        )
        num = customtkinter.CTkLabel(frame, text="Num Telephone:")
        self.numentr = customtkinter.StringVar(value="")
        numentr = customtkinter.CTkEntry(
            frame,
            textvariable=self.numentr,
            placeholder_text="07********",
        )

        efface = customtkinter.CTkButton(
            root,
            text="Effacer",
            command=self.reset,
        )
        enregistre = customtkinter.CTkButton(
            root,
            text="Enregistrer",
            command=self.add_patient,
        )

        lbl1.grid(row=0, column=1, padx=4, pady=8)
        nom.grid(row=1, column=0, padx=4, pady=8)
        pre.grid(row=1, column=1, padx=4, pady=8)
        nomentr.grid(row=2, column=0, padx=4, pady=8)
        preentr.grid(row=2, column=1, padx=4, pady=8)
        num.grid(row=3, column=1, padx=4, pady=8)
        numentr.grid(row=4, column=1, padx=4, pady=8)

        frame.grid(row=1, column=1, sticky="nsew", padx=4, pady=8)

        efface.grid(row=2, column=1, padx=4, pady=8)
        enregistre.grid(row=2, column=1, padx=4, pady=8)

    def reset(self):

        self.nomentr.set("")
        self.preentr.set("")
        self.numentr.set("")

    def add_patient(self):
        nom = self.nomentr.get()
        prenom = self.preentr.get()
        sexe = self.genre.get()
        date_naissance = self.date_naissance.get()
        phone = self.numentr.get()
        if not nom or not prenom or not sexe or not date_naissance or not phone:
            messagebox.showerror(message="Il faut completer tout les champs")
        elif Client.socket:
            Message(
                "add_patient",
                {
                    "nom": nom,
                    "prenom": prenom,
                    "sexe": sexe,
                    "date_naissance": date_naissance,
                    "phone": phone,
                },
                Client.socket,
            ).send()
