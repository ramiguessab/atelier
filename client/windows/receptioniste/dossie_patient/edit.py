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


class EditPatient(Window):
    def __init__(self, data) -> None:
        super().__init__("Modifier Patient")
        self.data = data

    def build(self, root):
        root.title("Les Patiens")

        root.geometry("300x400")
        root.resizable(False, False)

        frame = customtkinter.CTkFrame(root)
        lbl1 = customtkinter.CTkLabel(
            root,
            text="Entrez les modifications que vous souhaitez",
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
        self.genre = customtkinter.StringVar(value=self.data["sexe"])
        customtkinter.CTkOptionMenu(
            master=frame, values=["Male", "Female"], variable=self.genre
        ).grid(row=4, column=0, padx=4, pady=8)

        customtkinter.CTkLabel(
            frame,
            text="Date de naissance:",
        ).grid(row=5, column=0, padx=4, pady=8)
        self.date_naissance = customtkinter.StringVar(value=self.data["date_naissance"])
        customtkinter.CTkEntry(
            textvariable=self.date_naissance,
            master=frame,
        ).grid(row=6, column=0, padx=4, pady=8)

        self.nomentr = customtkinter.StringVar(value=self.data["nom"])
        nomentr = customtkinter.CTkEntry(
            textvariable=self.nomentr,
            master=frame,
        )
        self.preentr = customtkinter.StringVar(value=self.data["prenom"])
        preentr = customtkinter.CTkEntry(
            master=frame,
            textvariable=self.preentr,
        )
        num = customtkinter.CTkLabel(frame, text="Num Telephone:")
        self.numentr = customtkinter.StringVar(value=self.data["phone"])
        numentr = customtkinter.CTkEntry(
            frame,
            textvariable=self.numentr,
            placeholder_text="07********",
        )

        enregistre = customtkinter.CTkButton(
            root, text="Enregistrer", command=self.edit_patient
        )

        lbl1.grid(row=0, column=1, padx=4, pady=8)
        nom.grid(row=1, column=0, padx=4, pady=8)
        pre.grid(row=1, column=1, padx=4, pady=8)
        nomentr.grid(row=2, column=0, padx=4, pady=8)
        preentr.grid(row=2, column=1, padx=4, pady=8)
        num.grid(row=3, column=1, padx=4, pady=8)
        numentr.grid(row=4, column=1, padx=4, pady=8)

        frame.grid(row=1, column=1, sticky="nsew", padx=4, pady=8)

        enregistre.grid(row=2, column=1, padx=4, pady=8)

    def edit_patient(self):
        nom = self.nomentr.get()
        prenom = self.preentr.get()
        sexe = self.genre.get()
        date_naissance = self.date_naissance.get()
        phone = self.numentr.get()
        if Client.socket:
            Message(
                "edit_patient",
                {
                    "id": self.data["id"],
                    "nom": nom,
                    "prenom": prenom,
                    "sexe": sexe,
                    "date_naissance": date_naissance,
                    "phone": phone,
                },
                Client.socket,
            ).send()
