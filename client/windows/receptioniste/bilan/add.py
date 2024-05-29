from tkinter import messagebox
import customtkinter
from client.ui import Client
from client.window import Window
from message import Message


class AddBilan(Window):
    def __init__(self, data) -> None:
        super().__init__("Ajouter Bilan")
        self.data = data

    def build(self, root):
        root.geometry("400x500")
        root.resizable(False, False)
        self.patient = self.data["patient"][0]
        self.analysis_index = dict()
        for analyse in self.data["analyses"]:
            self.analysis_index[analyse["nom"]] = {
                "id": analyse["id"],
                "abreviation": analyse["abreviation"],
                "prix": analyse["prix"],
            }
        analyses = list(self.analysis_index.keys())
        root = customtkinter.CTkFrame(root)
        root.pack()
        self.prix = customtkinter.StringVar(
            value=self.analysis_index[analyses[0]]["prix"]
        )
        self.selected_analyse_id = self.analysis_index[analyses[0]]["id"]
        frame = customtkinter.CTkFrame(root)

        lbl1 = customtkinter.CTkLabel(
            root,
            text="Entrez modifications que vous souhaitez",
        )

        customtkinter.CTkLabel(frame, text="Nom:").grid(column=0, row=0, padx=8, pady=8)

        self.nom_patient = customtkinter.StringVar(value=self.patient["nom"])
        customtkinter.CTkEntry(
            frame, textvariable=self.nom_patient, state="disabled"
        ).grid(column=0, row=1, padx=8, pady=8)
        customtkinter.CTkLabel(
            frame,
            text="Prénom:",
        ).grid(column=1, row=0, padx=8, pady=8)
        self.prenom_patient = customtkinter.StringVar(value=self.patient["prenom"])
        customtkinter.CTkEntry(
            frame, textvariable=self.prenom_patient, state="disabled"
        ).grid(column=1, row=1, padx=8, pady=8)

        customtkinter.CTkLabel(frame, text="Nom d'analyse:").grid(
            column=0, row=2, padx=8, pady=8
        )

        self.selected_analysis = customtkinter.StringVar(value=analyses[0])
        customtkinter.CTkOptionMenu(
            frame,
            values=analyses,
            variable=self.selected_analysis,
            command=self.on_analysis_change,
        ).grid(column=0, row=3, padx=8, pady=8)

        customtkinter.CTkLabel(frame, text="Abreviation:").grid(
            column=1, row=2, padx=8, pady=8
        )

        self.abrv = customtkinter.StringVar(
            value=self.analysis_index[analyses[0]]["abreviation"]
        )
        customtkinter.CTkEntry(frame, textvariable=self.abrv, state="disabled").grid(
            column=1, row=3, padx=8, pady=8
        )

        customtkinter.CTkLabel(frame, text="Date de visite:").grid(
            column=1, row=4, padx=8, pady=8
        )
        self.date_visite = customtkinter.StringVar()
        customtkinter.CTkEntry(frame, textvariable=self.date_visite).grid(
            column=1, row=5, padx=8, pady=8
        )
        customtkinter.CTkLabel(frame, text="Prix:").grid(
            column=0, row=4, padx=8, pady=8
        )
        customtkinter.CTkEntry(frame, state="disabled", textvariable=self.prix).grid(
            column=0, row=5, padx=8, pady=8
        )

        enregistre = customtkinter.CTkButton(
            root, text="Enregistrer", command=self.add_bilan
        )

        lbl1.grid(row=0, column=1, padx=8, pady=8)

        frame.grid(row=1, column=1, sticky="nsew", padx=8, pady=8)

        enregistre.grid(row=2, column=1, padx=8, pady=8)

    def on_analysis_change(self, new_value):
        self.abrv.set(self.analysis_index[new_value]["abreviation"])
        self.prix.set(self.analysis_index[new_value]["prix"])
        self.selected_analyse_id = self.analysis_index[new_value]["id"]

    def add_bilan(self):
        date_visite = self.date_visite.get()
        if not date_visite:
            messagebox.showerror(message="Il faut remplire la date de visite")
        elif Client.socket:
            Message(
                "add_bilan",
                {
                    "analyse_id": self.selected_analyse_id,
                    "patient_id": self.patient["id"],
                    "date_visite": date_visite,
                },
                Client.socket,
            ).send()
