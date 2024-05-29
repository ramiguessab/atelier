from tkinter import messagebox
import customtkinter
from client.window import Window
from message import Message
from client.ui import Client

roles = ["Receptioniste", "Medicin", "Technicien", "Infermier"]


class AddStock(Window):
    def __init__(self) -> None:
        super().__init__("Ajouter au stock")

    def build(self, app):

        app = customtkinter.CTkFrame(master=app)
        app.pack(padx=16, pady=16)
        ##
        self.name = customtkinter.StringVar()
        self.quantity = customtkinter.StringVar()
        self.prix_unitaire = customtkinter.StringVar()
        self.date_peremption = customtkinter.StringVar()
        ##

        customtkinter.CTkLabel(
            master=app,
            text="Entrez les informations de produit",
        ).pack(padx=8, pady=4)

        customtkinter.CTkLabel(master=app, text="Nom:").pack(padx=8, pady=4)
        customtkinter.CTkEntry(
            master=app, placeholder_text="Nom", textvariable=self.name
        ).pack(padx=8, pady=4)

        customtkinter.CTkLabel(master=app, text="Quantite:").pack(padx=8, pady=4)

        customtkinter.CTkEntry(
            master=app,
            placeholder_text="Quantite",
            textvariable=self.quantity,
        ).pack(padx=8, pady=4)

        customtkinter.CTkLabel(master=app, text="Unite Price:").pack(padx=8, pady=4)
        customtkinter.CTkEntry(
            master=app,
            placeholder_text="Unit Price",
            textvariable=self.prix_unitaire,
        ).pack(padx=8, pady=4)

        customtkinter.CTkLabel(master=app, text="Date Peremption:").pack(padx=8, pady=4)
        customtkinter.CTkEntry(
            master=app,
            placeholder_text="Date Peremption",
            textvariable=self.date_peremption,
        ).pack(padx=8, pady=4)

        customtkinter.CTkButton(
            master=app, text="Enregistrer", command=self.add_stock
        ).pack(padx=8, pady=4)

    def add_stock(self):
        nom = self.name.get()
        quantity = self.quantity.get()
        prix_unitaire = self.prix_unitaire.get()
        date_peremption = self.date_peremption.get()
        if not nom or not quantity or not prix_unitaire or not date_peremption:
            messagebox.showerror(message="Il faut remplit touts les champs")
        elif Client.socket != None:
            Message(
                "add_stock",
                {
                    "nom": nom,
                    "quantity": quantity,
                    "prix_unitaire": prix_unitaire,
                    "date_peremption": date_peremption,
                },
                Client.socket,
            ).send()
