import customtkinter
from client.window import Window
from message import Message
from client.ui import Client

roles = ["Receptioniste", "Medicin", "Technicien", "Infermier"]


class EditStock(Window):
    def __init__(self, data) -> None:
        super().__init__("Ajouter au stock")
        self.data = data

    def build(self, app):
        app = customtkinter.CTkFrame(master=app)
        app.pack(padx=16, pady=16)
        ##
        self.name = customtkinter.StringVar(value=self.data["nom"])
        self.quantity = customtkinter.StringVar(value=self.data["quantite"])
        self.prix_unitaire = customtkinter.StringVar(value=self.data["prix_unitaire"])
        self.date_peremption = customtkinter.StringVar(
            value=self.data["date_peremption"]
        )
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
        if Client.socket != None:
            Message(
                "edit_stock",
                {
                    "id": self.data["id"],
                    "nom": nom,
                    "quantite": quantity,
                    "prix_unitaire": prix_unitaire,
                    "date_peremption": date_peremption,
                },
                Client.socket,
            ).send()
