from tkinter import messagebox
import customtkinter
from client.components.Table import CTkTable
from client.ui import Client
from client.window import Window
from client.windows.receptioniste.bilan.add import AddBilan
from client.windows.receptioniste.bilan.edit import EditBilan
from client.windows.receptioniste.bilan.search_patient import SearchPatient
from message import Message


class Bilan(Window):
    def __init__(self, data) -> None:
        super().__init__("Bilan")
        self.data = data

    def build(self, root):
        root.geometry("1000x490")
        root.resizable(False, False)

        frame = customtkinter.CTkFrame(root)

        customtkinter.CTkLabel(
            frame,
            text="Vous trouverez ici tous les bilans enregistrés dans ce laboratoire",
        ).pack(pady=8)

        self.bilan_table = CTkTable(
            master=frame,
            columns=[
                "Id",
                "Nom",
                "Prenom",
                "Genre",
                "Date de naissance",
                "Numero de telephone",
                "Date visite",
                "Analyse",
            ],
            rows=self.data,
        )

        self.bilan_table.pack(padx=8, pady=8)

        modbtn = customtkinter.CTkButton(
            root, text="Modifier", command=self.open_edit_bilan
        )
        ajtbtn = customtkinter.CTkButton(
            root, text="Ajouter", command=self.open_add_bilan
        )

        frame.pack(padx=8, pady=8, expand=True, fill="both")
        modbtn.pack(pady=8, padx=4, side="left")
        ajtbtn.pack(pady=8, padx=4, side="right")

    def open_edit_bilan(self):
        selected_bilan = self.bilan_table.selected_value.get()
        if not selected_bilan:
            messagebox.showerror(message="If faut selecter un bilan")
        elif Client.socket:
            Message("open_edit_bilan", {"id": selected_bilan}, Client.socket).send()

    def open_add_bilan(self):
        Client.open_as_dialog(SearchPatient())
