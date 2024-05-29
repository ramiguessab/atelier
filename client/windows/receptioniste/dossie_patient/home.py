from message import Message
import customtkinter
from tkinter import messagebox
from client.ui import Client
from client.window import Window
from client.windows.receptioniste.dossie_patient.edit import EditPatient
from client.windows.receptioniste.dossie_patient.add import AddPatient
from client.components.Table import CTkTable

# from patientpatadd.patientpatientajouter import patpatadd


class PatientFile(Window):
    def __init__(self, data) -> None:
        super().__init__("Patients")
        self.data = data

    def build(self, root):
        root.geometry("800x490")
        root.resizable(False, False)

        frame = customtkinter.CTkFrame(root)

        frame.pack(padx=4, pady=16, expand=True, fill="both")

        customtkinter.CTkLabel(
            frame,
            text="Vous trouverez ici tous les patients enregistrés dans ce laboratoire",
        ).pack(padx=4, pady=16)

        self.patient_table = CTkTable(
            master=frame,
            columns=[
                "Id",
                "Nom",
                "Prenom",
                "Genre",
                "Date de naissance",
                "Numero Telephone",
            ],
            rows=self.data,
        )

        self.patient_table.pack(padx=4, pady=16)

        action_frame = customtkinter.CTkFrame(root)
        action_frame.pack(padx=4, pady=16)

        customtkinter.CTkButton(
            action_frame, text="Ajouter", command=self.open_add_patient
        ).grid(row=0, column=0, padx=4, pady=16)

        customtkinter.CTkButton(
            action_frame,
            text="Modifier",
            command=self.open_edit_patient,
        ).grid(row=0, column=1, padx=4, pady=16)

    def open_edit_patient(self):
        id = self.patient_table.selected_value.get()
        if not id:
            messagebox.showerror(message="If faut specifie un patient")
        elif Client.socket:
            Message("open_edit_patient", {"id": id}, Client.socket).send()

    def open_add_patient(self):
        Client.open_as_dialog(AddPatient())
