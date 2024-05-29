from datetime import datetime
import datetime
from struct import pack
import customtkinter
from client.components.Table import CTkTable
from client.ui import Client
from client.window import Window
from tkinter import messagebox
import re

from message import Message


class Bienvenue(Window):
    def __init__(self) -> None:
        super().__init__("Technicien Home")

    def build(self, app):
        app.title("Gestion de laboratoire")
        app.geometry("800x250")
        app.resizable(False, False)

        self.label = customtkinter.CTkLabel(app, text="Bienvenue")
        self.label.pack(pady=16)

        self.bt1 = customtkinter.CTkButton(
            app, text="Ajouter Resultats", command=self.ouvrir_fenetre_analyse
        )
        self.bt1.pack(
            pady=4,
            padx=16,
            fill="both",
        )

        self.bt2 = customtkinter.CTkButton(
            app, text="Stock", command=self.ouvrir_fenetre_stock
        )
        self.bt2.pack(pady=4, padx=16, fill="both")

        self.bt5 = customtkinter.CTkButton(
            app,
            text="Code",
            command=self.code,
        )
        self.bt5.pack(
            pady=4,
            padx=16,
            fill="both",
        )

        self.bt4 = customtkinter.CTkButton(
            app,
            text="Déconnecter",
            command=self.deconnecter,
            fg_color="red",
            hover_color="dark red",
        )
        self.bt4.pack(pady=4, padx=16, fill="both")

    def deconnecter(self):
        Client.desconnect()

    def ouvrir_fenetre_analyse(self):
        Client.open_new_window(AjouterResultat())

    def ouvrir_fenetre_stock(self):
        if Client.socket:
            Message("open_tech_stock", {}, Client.socket).send()

    def code(self):
        if Client.socket:
            Message("open_tech_code", {}, Client.socket).send()


class Stock(Window):
    def __init__(self, stock) -> None:
        super().__init__("Stock")
        self.stock = stock

    def build(self, app):
        app.geometry("500x420")
        app.resizable(False, False)

        self.stock_index = dict()

        for stock in self.stock:
            self.stock_index[stock["nom"]] = {
                "quantite": stock["quantite"],
                "date_peremption": stock["date_peremption"],
                "id": stock["id"],
            }

        stocks = list(self.stock_index.keys())

        self.selected_stock_id = customtkinter.StringVar(
            value=self.stock_index[stocks[0]]["id"]
        )

        self.label = customtkinter.CTkLabel(
            app,
            text="Sélectionnez un réactif, un consommable ou un appareil",
        )
        self.label.pack(
            pady=4,
            padx=8,
        )
        self.choix = customtkinter.StringVar(value=stocks[0])
        customtkinter.CTkOptionMenu(
            app, values=stocks, variable=self.choix, command=self.on_choix
        ).pack(pady=4, padx=8)

        self.label = customtkinter.CTkLabel(
            app, text="La quantité disponible en stock:"
        )
        self.label.pack(pady=4, padx=8)
        self.quantity = customtkinter.StringVar(
            value=self.stock_index[stocks[0]]["quantite"]
        )
        customtkinter.CTkEntry(app, state="disabled", textvariable=self.quantity).pack(
            pady=4, padx=8
        )

        customtkinter.CTkLabel(app, text="La date de peremption:").pack(pady=4, padx=8)
        self.date_peremption = customtkinter.StringVar(
            value=self.stock_index[stocks[0]]["date_peremption"]
        )
        customtkinter.CTkEntry(
            app, state="disabled", textvariable=self.date_peremption
        ).pack(pady=4, padx=8)

        customtkinter.CTkLabel(app, text="La quantité vous voulez prendre:").pack(
            pady=4, padx=8
        )
        self.demenu = customtkinter.StringVar()
        customtkinter.CTkEntry(app, textvariable=self.demenu).pack(pady=4, padx=8)

        self.bt1 = customtkinter.CTkButton(
            app,
            command=self.enregistrer,
            text="Enregistrer",
        )
        self.bt1.pack(pady=4, padx=8)

    def on_choix(self, new_value):
        self.selected_stock_id = self.stock_index[new_value]["id"]
        self.quantity.set(self.stock_index[new_value]["quantite"])
        self.date_peremption.set(self.stock_index[new_value]["date_peremption"])

    def enregistrer(self):
        if not self.demenu.get():
            messagebox.showerror(
                message="If faut specifie la quantite vous voulez prendre"
            )
        elif Client.socket:
            Message(
                "take_stock",
                {
                    "stock_id": self.selected_stock_id.get(),
                    "quantite": self.demenu.get(),
                },
                Client.socket,
            ).send()


class AjouterResultat(Window):
    def __init__(self) -> None:
        super().__init__("Analyses")

    def build(self, app):
        app.title("Analyses")
        app.geometry("400x300")
        app.resizable(False, False)

        customtkinter.CTkLabel(app, text="Le Code:").pack(padx=8, pady=8)
        self.code = customtkinter.StringVar()
        customtkinter.CTkEntry(app, textvariable=self.code).pack(padx=8, pady=8)

        customtkinter.CTkButton(app, text="Afficher", command=self.open_resultats).pack(
            padx=8, pady=8
        )

    def open_resultats(self):
        code = self.code.get()
        if not code:
            messagebox.showerror(message="Entrez Le code d'echantillion")
        elif Client.socket:
            Message(
                "open_tech_resultat_observation",
                {"code": code},
                Client.socket,
            ).send()


class ResultatObservation(Window):
    def __init__(self, code) -> None:
        super().__init__("Resultat Observation")
        self.code = code

    def build(self, app):
        app.title("")
        app.geometry("500x400")
        app.resizable(False, False)

        CTkTable(
            app,
            columns=["Id", "Code", "Nom", "Prenom", "Date Visite"],
            rows=[self.code],
        ).pack(padx=8, pady=8)

        self.entrme = customtkinter.CTkTextbox(app, height=150, width=750)
        self.entrme.pack(padx=16, pady=8)

        button = customtkinter.CTkButton(app, text="Enregistrer", command=self.test)
        button.pack(padx=16, pady=8, anchor=customtkinter.E)

    def test(self):
        if self.entrme.get("1.0", "end-1c") == "":
            messagebox.showerror(
                "Erreur",
                "Veuillez remplir le champ des résultats et observations.",
            )
        elif Client.socket:

            Message(
                "add_resultat",
                {
                    "echantillon_id": self.code["id"],
                    "contenu": self.entrme.get("1.0", "end-1c"),
                },
                Client.socket,
            ).send()


class Code(Window):
    def __init__(self, analyses) -> None:
        super().__init__("Codes")
        self.analyses = analyses

    def build(self, app):
        app.title("Générateur de Code")
        app.geometry("700x300")

        self.analyse_index = dict()

        for analyse in self.analyses:
            self.analyse_index[analyse["abreviation"]] = {"id": analyse["id"]}

        analysis = list(self.analyse_index.keys())

        self.selected_analyse = self.analyse_index[analysis[0]]["id"]

        app = customtkinter.CTkFrame(app)
        app.pack()

        self.frame = customtkinter.CTkFrame(app)
        self.frame.grid(
            column=0,
            row=1,
            pady=4,
            padx=16,
        )

        self.lbl1 = customtkinter.CTkLabel(
            app,
            text="Entrez les informations du patient et le nom de l'analyse",
        )

        self.lbl1.grid(
            row=0,
            column=0,
            pady=4,
            padx=16,
        )

        self.nom = customtkinter.CTkLabel(self.frame, text="Nom:")
        self.pre = customtkinter.CTkLabel(self.frame, text="Prénom:")
        self.nomentr = customtkinter.CTkEntry(
            self.frame,
        )
        self.preentr = customtkinter.CTkEntry(self.frame)

        self.frame2 = customtkinter.CTkFrame(app)
        self.frame2.grid(
            column=1,
            row=1,
            pady=4,
            padx=16,
        )

        self.abrv = customtkinter.CTkLabel(self.frame2, text="L'abréviation du nom:\n")
        self.abrventr = customtkinter.CTkOptionMenu(
            self.frame2, values=analysis, command=self.on_analyse_choix
        )
        self.generer = customtkinter.CTkButton(
            app,
            text="Rechercher de bilan",
            command=self.generer_code,
        )

        self.nom.grid(
            row=1,
            column=0,
            pady=4,
            padx=16,
        )
        self.nomentr.grid(
            row=1,
            column=1,
            pady=4,
            padx=16,
        )
        self.pre.grid(
            row=2,
            column=0,
            pady=4,
            padx=16,
        )
        self.preentr.grid(
            row=2,
            column=1,
            pady=4,
            padx=16,
        )

        self.abrv.pack(
            pady=4,
            padx=16,
        )
        self.abrventr.pack(
            pady=4,
            padx=16,
        )
        self.generer.grid(
            row=2,
            column=0,
            pady=4,
            padx=16,
        )

    def on_analyse_choix(self, new_value):
        self.selected_analyse = self.analyse_index[new_value]["id"]

    def generer_code(self):
        nom_patient = self.nomentr.get()
        prenom_patient = self.preentr.get()
        analyse_id = self.selected_analyse

        if not nom_patient or not prenom_patient:
            messagebox.showerror(
                f"Voullez Remplir tout les champs",
            )
        elif Client.socket:
            Message(
                "open_tech_code_bilans",
                {
                    "nom": nom_patient,
                    "prenom": prenom_patient,
                    "analyse_id": analyse_id,
                },
                Client.socket,
            ).send()


class BilansCode(Window):
    def __init__(self, bilans) -> None:
        super().__init__("Bilan")
        self.bilans = bilans

    def build(self, app):
        app.geometry("1300x400")

        customtkinter.CTkLabel(
            app, text="Choisez le bilan vous voullez associer avec cette echantillion"
        ).pack(padx=8, pady=8)

        self.bilan_table = CTkTable(
            app,
            columns=[
                "Id",
                "Nom",
                "Prenom",
                "Date Naissance",
                "Abreviation",
                "Date Visite",
            ],
            rows=self.bilans,
        )

        self.bilan_table.pack(padx=8, pady=8)

        customtkinter.CTkButton(
            app, text="Generer Code", command=self.add_echantillion
        ).pack(padx=8, pady=8)

    def add_echantillion(self):
        bilan_id = self.bilan_table.selected_value.get()
        if not bilan_id:
            messagebox.showerror(message="You need to select a bilan")
        elif Client.socket:
            abrv = ""
            for bilan in self.bilans:
                if int(bilan["id"]) == int(bilan_id):
                    abrv = bilan["abreviation"]

            age = (
                datetime.datetime.now().year
                - datetime.datetime.strptime(
                    self.bilans[0]["date_naissance"], "%Y-%m-%d %H:%M:%S"
                ).year
            )

            nom = self.bilans[0]["nom"]
            prenom = self.bilans[0]["prenom"]
            code = f"{bilan_id}{nom[0]}{prenom[0]}{age}{abrv}"
            Message(
                "add_echantillon", {"bilan_id": bilan_id, "code": code}, Client.socket
            ).send()
