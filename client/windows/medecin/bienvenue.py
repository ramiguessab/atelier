from tkinter import messagebox
import customtkinter
from client.components.Table import CTkTable
from client.ui import Client
from client.window import Window
from message import Message


class Bienvenue(Window):
    def __init__(self) -> None:
        super().__init__("Resultats")

    def build(self, app):
        app.geometry("800x200")
        app.resizable(False, False)

        label = customtkinter.CTkLabel(
            app,
            text="Bienvenue dans vos tâches",
        )
        label.pack(pady=4, padx=16, fill="both")

        bt1 = customtkinter.CTkButton(
            app,
            text="Consulter les résultats",
            command=self.F1,
        )
        bt1.pack(pady=4, padx=16, fill="both")

        bt2 = customtkinter.CTkButton(
            app,
            text="Demander des analyses supplémentaires",
            command=self.F2,
        )
        bt2.pack(pady=4, padx=16, fill="both")

        bt3 = customtkinter.CTkButton(
            app,
            text="Déconnecter",
            command=self.deconnecter,
            fg_color="red",
            hover_color="dark red",
        )
        bt3.pack(pady=4, padx=16, fill="both")

    def F1(self):
        if Client.socket:
            Message("open_consultation", {}, Client.socket).send()

    def F2(self):
        if Client.socket:
            Message("open_medecin_analyse_sup", {}, Client.socket).send()

    def F3(self):
        Client.open_new_window(Recherche())

    def deconnecter(self):
        Client.desconnect()


class Consulter(Window):
    def __init__(self, consultations) -> None:
        super().__init__("Consulter")
        self.consultations = consultations

    def build(self, app):
        app.title("Consulter Les Resultat")
        app.geometry("800x400")
        app.resizable(False, False)

        customtkinter.CTkLabel(
            app,
            text="vous trouverez ici tous les bilans enregistrés dans ce laboratoire",
        ).pack(
            pady=4,
            padx=16,
        )

        self.consultations_table = CTkTable(
            app,
            columns=[
                "Id",
                "Nom",
                "Prenom",
                "Genre",
                "Date Naissance",
                "Type Analyse",
            ],
            rows=self.consultations,
        )
        self.consultations_table.pack(pady=4, padx=16)

        customtkinter.CTkButton(app, text="Consulter Resultat", command=self.F4).pack(
            pady=4, padx=16
        )

    def F4(self):
        selected_consultation = self.consultations_table.selected_value.get()
        if not selected_consultation:
            messagebox.showerror(
                message="Il faut selectionner un bilan pour le consulter"
            )
        elif Client.socket:
            Message(
                "open_ajouter_consultation",
                {"selected_bilan": selected_consultation},
                Client.socket,
            ).send()


class Recherche(Window):
    def __init__(self) -> None:
        super().__init__("Recherche")

    def build(self, app):
        app.title("Recherche")
        app.geometry("600x310")
        app.resizable(False, False)

        Label1 = customtkinter.CTkLabel(
            app,
            text="Entrez la date de l'analyse et le code du d'analyse",
        )
        Label1.pack(pady=4, padx=16)

        customtkinter.CTkLabel(app, text="Code :").pack(pady=4, padx=16)

        self.code = customtkinter.StringVar()
        customtkinter.CTkEntry(app, textvariable=self.code).pack(pady=4, padx=16)

        # Boutons
        actions_frame = customtkinter.CTkFrame(app)
        actions_frame.pack(pady=4, padx=16)
        bt1 = customtkinter.CTkButton(
            actions_frame, text="Afficher", command=self.afficher
        )
        bt1.grid(column=1, row=0, pady=4, padx=16)

    def afficher(self):
        if self.code.get() == "":
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
        else:
            Client.open_as_dialog(AncienResultats())


class AncienResultats(Window):
    def __init__(self) -> None:
        super().__init__("Ancien Resultats")

    def build(self, app):
        app.geometry("600x1000")
        info_label = customtkinter.CTkLabel(
            app,
            text=f"Code:",
        )
        info_label.pack(pady=20)


class AnalysSup(Window):
    def __init__(self, analyses_disponible) -> None:
        super().__init__("Analyse Supplémentaire")
        self.analyses_disponible = analyses_disponible

    def build(self, app):
        app.geometry("500x500")
        app.resizable(False, False)

        # Create and pack a label above the frames
        self.Label1 = customtkinter.CTkLabel(
            app,
            text="Entrez les analyses supplémentaires nécessaires avec le code du patient",
        )
        self.Label1.pack(
            pady=4,
            padx=16,
        )

        horizental_frame = customtkinter.CTkFrame(app, fg_color="transparent")
        horizental_frame.pack(
            pady=4,
            padx=16,
        )

        # Create and pack frame1
        self.frame1 = customtkinter.CTkFrame(horizental_frame)
        self.frame1.grid(
            column=0,
            row=0,
            pady=4,
            padx=16,
        )

        # Label and Entry widgets inside frame1
        customtkinter.CTkLabel(self.frame1, text="Nom:").pack(
            pady=4,
            padx=16,
        )
        self.nom = customtkinter.StringVar()
        customtkinter.CTkEntry(self.frame1, textvariable=self.nom).pack(
            pady=4,
            padx=16,
        )

        customtkinter.CTkLabel(self.frame1, text="Prenom:").pack(
            pady=4,
            padx=16,
        )
        self.prenom = customtkinter.StringVar()
        customtkinter.CTkEntry(self.frame1, textvariable=self.prenom).pack(
            pady=4,
            padx=16,
        )
        self.Label3 = customtkinter.CTkLabel(self.frame1, text="Nom d'analyse:")
        self.Label3.pack(
            pady=4,
            padx=16,
        )

        self.combo = customtkinter.CTkComboBox(
            self.frame1,
            values=self.analyses_disponible,
        )
        self.combo.pack(
            pady=4,
            padx=16,
        )

        # Create and pack frame2
        self.frame2 = customtkinter.CTkFrame(horizental_frame)
        self.frame2.grid(
            column=1,
            row=0,
            pady=4,
            padx=16,
        )

        # Label and Entry widgets inside frame2
        self.Label4 = customtkinter.CTkLabel(self.frame2, text="La Demande:")
        self.Label4.pack(
            pady=4,
            padx=16,
        )

        self.code2 = customtkinter.CTkTextbox(self.frame2)
        self.code2.pack(
            pady=4,
            padx=16,
        )
        actions_frame = customtkinter.CTkFrame(app)
        # Buttons
        self.bt1 = customtkinter.CTkButton(
            actions_frame,
            text="Envoyer",
            command=self.check_empty_fields,
        )
        self.bt1.grid(
            column=1,
            row=0,
            pady=8,
            padx=16,
        )

        actions_frame.pack(
            pady=4,
            padx=16,
        )

    def check_empty_fields(self):
        prenom = self.prenom.get()
        nom = self.nom.get()
        type_analyse = self.combo.get()
        contenu = self.code2.get(1.0, customtkinter.END)
        if not prenom or not nom or not type_analyse or not contenu:
            messagebox.showerror(
                "Error",
                "Il y a une erreur. Veuillez remplir tous les champs.",
            )
        else:
            messagebox.showinfo(
                "Success",
                "La demande est envoyer au receptioniste",
            )


class AjouterConsultation(Window):
    def __init__(self, contenu_resultat) -> None:
        super().__init__("Ajouter")
        self.resultat = contenu_resultat

    def build(self, app):
        app.title(" " * 60 + "Analyser les résultats")
        app.geometry("800x400")
        app.resizable(False, False)

        frame = customtkinter.CTkFrame(app)
        frame.pack(padx=8, pady=8)
        customtkinter.CTkLabel(frame, text="Resultat d'echantillon").grid(
            column=0, row=0, pady=8, padx=16
        )
        customtkinter.CTkLabel(frame, text="Votre Consultation").grid(
            column=1, row=0, pady=8, padx=16
        )
        resultat = customtkinter.CTkTextbox(frame)
        resultat.grid(column=0, row=1, pady=8, padx=16)

        resultat.insert(customtkinter.END, text=self.resultat["contenu"])
        self.consultation = customtkinter.CTkTextbox(frame)
        self.consultation.grid(column=1, row=1, pady=8, padx=16)

        actions_frame = customtkinter.CTkFrame(app)
        actions_frame.pack(pady=4, padx=16)
        bt1 = customtkinter.CTkButton(
            actions_frame,
            text="Imprimer",
            command=self.print,
        )

        bt2 = customtkinter.CTkButton(
            actions_frame,
            text="Enregistrer",
            command=self.save,
        )
        bt1.grid(column=0, row=0, pady=8, padx=16)
        bt2.grid(column=1, row=0, pady=8, padx=16)

    def print(self):

        messagebox.showinfo(
            "Success",
            "Impression de dossier en cours...",
        )

    def save(self):
        if Client.socket:
            consultation = self.consultation.get("1.0", customtkinter.END)
            Message(
                "add_consultation",
                {"contenu": consultation, "bilan_id": self.resultat["bilan_id"]},
                Client.socket,
            ).send()
