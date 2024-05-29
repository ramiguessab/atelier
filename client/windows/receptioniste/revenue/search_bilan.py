from message import Message
from tkinter import messagebox
import customtkinter
from client.ui import Client
from client.window import Window


class SearchBilan(Window):
    def __init__(self) -> None:
        super().__init__("Rechercher Bilan a payer")

    def build(self, root):
        root.geometry("200x300")
        root.resizable(False, False)
        frame = customtkinter.CTkFrame(root)
        frame.pack(padx=20)
        self.nom = customtkinter.StringVar()
        self.prenom = customtkinter.StringVar()
        customtkinter.CTkLabel(
            root,
            text="Nom:",
        ).pack(pady=4, padx=8)

        customtkinter.CTkEntry(root, textvariable=self.nom).pack(pady=4, padx=8)

        customtkinter.CTkLabel(
            root,
            text="Prenom:",
        ).pack(pady=4, padx=8)

        customtkinter.CTkEntry(root, textvariable=self.prenom).pack(pady=4, padx=8)

        customtkinter.CTkButton(
            root, text="Rechercher", command=self.search_bilan
        ).pack(pady=8, padx=8)

        frame.grid(row=1, column=0, padx=20)

    def search_bilan(self):
        nom = self.nom.get()
        prenom = self.prenom.get()
        if not nom or not prenom:
            messagebox.showerror(message="Entrez le nom et le prenom")
        elif Client.socket:
            Message(
                "search_bilan", {"nom": nom, "prenom": prenom}, Client.socket
            ).send()
