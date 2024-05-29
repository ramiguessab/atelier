from tkinter import messagebox
import customtkinter
from client.ui import Client
from client.window import Window
from message import Message


class SearchPatient(Window):
    def __init__(self) -> None:
        super().__init__("Rechercher Bilan a payer")

    def build(self, root):
        root.geometry("200x300")
        root.resizable(False, False)
        frame = customtkinter.CTkFrame(root)

        customtkinter.CTkLabel(
            root,
            text="Nom:",
        ).pack(pady=4, padx=8)

        self.nom = customtkinter.StringVar()
        customtkinter.CTkEntry(root, textvariable=self.nom).pack(pady=4, padx=8)

        customtkinter.CTkLabel(
            root,
            text="Prenom:",
        ).pack(pady=4, padx=8)

        self.prenom = customtkinter.StringVar()
        customtkinter.CTkEntry(root, textvariable=self.prenom).pack(pady=4, padx=8)

        customtkinter.CTkButton(root, text="Rechercher", command=self.search).pack(
            pady=8, padx=8
        )

        frame.grid(row=1, column=0, padx=20)

    def search(self):
        nom = self.nom.get()
        prenom = self.prenom.get()
        if not nom or not prenom:
            messagebox.showerror("Completer les Champs")
        elif Client.socket:
            Message(
                "search_bilan_patient",
                {"nom": nom, "prenom": prenom},
                Client.socket,
            ).send()
