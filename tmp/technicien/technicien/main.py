import customtkinter
from client.ui import Client
from client.window import Window
from tkinter import messagebox
import re


class Bienvenue(Window):
    def build(self, app):
        app.title("Gestion de laboratoire")
        app.geometry("600x340")
        app.resizable(False, False)

        self.label = customtkinter.CTkLabel(
            app, text="Bienvenue", text_color="blue", font=("Arial", 30, "bold")
        )
        self.label.pack(pady=20)

        self.bt1 = customtkinter.CTkButton(
            app,
            text="Analyses",
            command=self.ouvrir_fenetre_analyse,
            hover_color="black",
            width=400,
            font=("Arial", 13, "bold"),
        )
        self.bt1.pack(pady=10)

        self.bt2 = customtkinter.CTkButton(
            app,
            text="Stock",
            command=self.ouvrir_fenetre_stock,
            hover_color="black",
            width=400,
            font=("Arial", 13, "bold"),
        )
        self.bt2.pack(pady=10)

        self.bt5 = customtkinter.CTkButton(
            app,
            text="Code",
            command=self.code,
            hover_color="black",
            width=400,
            font=("Arial", 13, "bold"),
        )
        self.bt5.pack(pady=10)

        self.bt3 = customtkinter.CTkButton(
            app,
            text="Plaintes",
            command=self.plaint,
            hover_color="black",
            width=400,
            font=("Arial", 13, "bold"),
        )
        self.bt3.pack(pady=10)

        self.bt4 = customtkinter.CTkButton(
            app,
            text="Déconnecter",
            command=self.deconnecter,
            fg_color="red",
            hover_color="black",
            width=400,
            font=("Arial", 13, "bold"),
        )
        self.bt4.pack(pady=10)

    def deconnecter(self):
        Client.desconnect()

    def ouvrir_fenetre_analyse(self):
        Client.open_new_window(Analyse())

    def ouvrir_fenetre_stock(self):
        Client.open_new_window(Stock())

    def plaint(self):
        Client.open_new_window(Plaintes())

    def code(self):
        Client.open_new_window(Code())


class Stock(Window):
    def build(self, app):
        app.title("Gestion de laboratoire")
        app.geometry("600x430")
        # self.resizable(False, False)

        self.label = customtkinter.CTkLabel(
            app,
            text="Sélectionnez un réactif, un consommable ou un appareil",
            font=("Arial", 12, "bold"),
        )
        self.label.pack(pady=10, padx=15, anchor=customtkinter.W)

        self.analyse = ["Les tubes d'analyse", "rachid", "badis"]
        self.choix = customtkinter.CTkComboBox(
            app, values=self.analyse, border_color="light blue", width=190
        )
        self.choix.pack(padx=15, pady=15, anchor=customtkinter.W)

        self.label = customtkinter.CTkLabel(
            app, text="La quantité disponible en stock", font=("Arial", 12, "bold")
        )
        self.label.pack(pady=5, padx=15, anchor=customtkinter.W)

        self.frame1 = customtkinter.CTkFrame(app, height=20, width=500)
        self.frame1.pack(anchor=customtkinter.W, padx=20)

        self.code2 = customtkinter.CTkEntry(self.frame1, border_color="light blue")
        self.code2.pack(padx=20, side=customtkinter.LEFT)

        self.bt1 = customtkinter.CTkButton(
            self.frame1,
            text="Afficher",
            hover_color="black",
            font=("Arial", 12, "bold"),
        )
        self.bt1.pack(pady=15, padx=95, side=customtkinter.LEFT)

        frame2 = customtkinter.CTkFrame(app, height=500, width=60)
        frame2.pack(padx=20, pady=30, anchor=customtkinter.W)

        Label3 = customtkinter.CTkLabel(
            frame2,
            text="Entrez la date à laquelle vous souhaitez\n vérifier la péremption des produits utilisés:",
        )
        Label3.pack(side=customtkinter.TOP, anchor=customtkinter.W, pady=10, padx=10)

        jour = [str(i) for i in range(1, 32)]
        self.combo1 = customtkinter.CTkComboBox(
            frame2,
            values=jour,
            width=70,
            border_width=2,
            border_color="light blue",
            dropdown_hover_color="blue",
        )
        self.combo1.pack(side=customtkinter.LEFT, padx=5)

        mois = [
            "Janvier",
            "Février",
            "Mars",
            "Avril",
            "Mai",
            "Juin",
            "Juillet",
            "Août",
            "Septembre",
            "Octobre",
            "Novembre",
            "Décembre",
        ]
        self.combo2 = customtkinter.CTkComboBox(
            frame2,
            values=mois,
            width=90,
            border_width=2,
            border_color="light blue",
            dropdown_hover_color="blue",
        )
        self.combo2.pack(side=customtkinter.LEFT, padx=5)

        annee = [str(i) for i in range(2020, 2061)]
        self.combo3 = customtkinter.CTkComboBox(
            frame2,
            values=annee,
            width=80,
            border_width=2,
            border_color="light blue",
            dropdown_hover_color="blue",
        )
        self.combo3.pack(side=customtkinter.LEFT, padx=5)

        self.bt1 = customtkinter.CTkButton(
            frame2,
            text="Afficher",
            hover_color="black",
            font=("Arial", 12, "bold"),
            command=self.show_message,
        )
        self.bt1.pack(pady=15, padx=50, side=customtkinter.LEFT)

        self.bt1 = customtkinter.CTkButton(
            app,
            text="Enregistrer",
            hover_color="black",
            font=("Arial", 12, "bold"),
            command=self.enregistrer,
        )
        self.bt1.pack(padx=15, anchor=customtkinter.E)

    def enregistrer(self):
        if self.choix.get() == "" or self.choix.get() == "Les tubes d'analyse":
            messagebox.showerror(
                "Erreur",
                "Veuillez sélectionner un réactif, un consommable ou un appareil.",
            )
        elif not self.entre.get().isdigit():
            messagebox.showerror("Erreur", "La quantité doit être un nombre entier.")
        else:
            # You can add your save functionality here
            messagebox.showinfo(
                "Enregistrement", "Les données ont été enregistrées avec succès!"
            )

    def show_message(self):
        new_window = customtkinter.CTk()
        new_window.title(" " * 50 + "Stock")
        new_window.geometry("500x300")

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        label = customtkinter.CTkLabel(
            new_window,
            text="Les produits dont la péremption est prévue\n à la date que vous avez spécifiée ",
        )
        label.pack(pady=10)

        ok_button = customtkinter.CTkButton(
            new_window, text="OK", command=new_window.destroy
        )
        ok_button.pack(
            pady=20, side=customtkinter.BOTTOM, anchor=customtkinter.E, padx=20
        )

        new_window.mainloop()


class Analyse(Window):
    def build(self, app):
        self.title(" " * 100 + "Analyses")
        self.geometry("750x490")
        self.resizable(False, False)

        self.frame1 = customtkinter.CTkFrame(self, height=20, width=500)
        self.frame1.pack(anchor=customtkinter.W, pady=15, padx=20)

        self.lb1 = customtkinter.CTkLabel(self.frame1, text="Le Code:")
        self.lb1.pack(anchor=customtkinter.W, padx=20)

        self.code2 = customtkinter.CTkEntry(self.frame1, border_color="light blue")
        self.code2.pack(padx=20, side=customtkinter.LEFT)

        self.bt1 = customtkinter.CTkButton(
            self.frame1,
            text="Afficher",
            hover_color="black",
            font=("Arial", 12, "bold"),
        )
        self.bt1.pack(pady=15, padx=50, side=customtkinter.LEFT)

        self.frame2 = customtkinter.CTkFrame(self, height=400, width=200)
        self.frame2.pack(anchor=customtkinter.W, padx=20)

        # Labels and entry boxes on the left side of frame2
        self.lb2 = customtkinter.CTkLabel(self.frame2, text="Nom du patient:")
        self.lb2.grid(row=0, column=0, padx=20, pady=5, sticky=customtkinter.W)

        self.entry2 = customtkinter.CTkEntry(self.frame2, state="readonly")
        self.entry2.grid(row=1, column=0, padx=20, pady=5, sticky=customtkinter.W)

        self.lb3 = customtkinter.CTkLabel(self.frame2, text="Sexe du patient:")
        self.lb3.grid(row=2, column=0, padx=20, pady=5, sticky=customtkinter.W)

        self.entry3 = customtkinter.CTkEntry(self.frame2, state="readonly")
        self.entry3.grid(row=3, column=0, padx=20, pady=5, sticky=customtkinter.W)

        self.lb4 = customtkinter.CTkLabel(self.frame2, text="Nom d'analyse:")
        self.lb4.grid(row=4, column=0, padx=20, pady=5, sticky=customtkinter.W)

        self.entry4 = customtkinter.CTkEntry(self.frame2, state="readonly")
        self.entry4.grid(row=5, column=0, padx=20, pady=5, sticky=customtkinter.W)

        self.lb5 = customtkinter.CTkLabel(
            self.frame2, text="Les résultats et les observations:"
        )
        self.lb5.grid(row=6, column=0, padx=20, pady=5, sticky=customtkinter.W)

        self.bt2 = customtkinter.CTkButton(
            self.frame2,
            text="Ajouter",
            hover_color="black",
            font=("Arial", 12, "bold"),
            command=self.open,
        )
        self.bt2.grid(row=7, column=0, padx=20, pady=5, sticky=customtkinter.W)

        # Labels and entry boxes on the right side of frame2
        self.lb6 = customtkinter.CTkLabel(self.frame2, text="Prénom du patient:")
        self.lb6.grid(row=0, column=1, padx=90, pady=5, sticky=customtkinter.W)

        self.entry6 = customtkinter.CTkEntry(self.frame2, state="readonly")
        self.entry6.grid(row=1, column=1, padx=90, pady=5, sticky=customtkinter.W)

        self.lb7 = customtkinter.CTkLabel(self.frame2, text="Age du patient:")
        self.lb7.grid(row=2, column=1, padx=90, pady=5, sticky=customtkinter.W)

        self.entry7 = customtkinter.CTkEntry(self.frame2, state="readonly")
        self.entry7.grid(row=3, column=1, padx=90, pady=5, sticky=customtkinter.W)

        self.lb9 = customtkinter.CTkLabel(
            self.frame2, text="Le prénom et le nom du médecin:"
        )
        self.lb9.grid(row=4, column=1, padx=90, pady=5, sticky=customtkinter.W)

        self.entry9 = customtkinter.CTkEntry(self.frame2, border_color="light blue")
        self.entry9.grid(row=5, column=1, padx=90, pady=10, sticky=customtkinter.W)

        self.bt3 = customtkinter.CTkButton(
            self,
            text="Envoyer",
            hover_color="black",
            font=("Arial", 12, "bold"),
            command=self.send_analysis,
        )
        self.bt3.pack(pady=10, padx=250, anchor=customtkinter.W)

    def open(self):
        me = customtkinter.CTk()
        me.title("")
        me.geometry("500x300")
        me.resizable(False, False)

        lbme = customtkinter.CTkLabel(me, text="Les résultats et les observations:")
        lbme.pack(padx=20, pady=10)

        entrme = customtkinter.CTkTextbox(me, height=150, width=750)
        entrme.pack(padx=20, pady=10)

        def test():
            if entrme.get("1.0", "end-1c") == "":
                messagebox.showerror(
                    "Erreur",
                    "Veuillez remplir le champ des résultats et observations.",
                    parent=me,
                )
            else:
                messagebox.showinfo(
                    "Succès",
                    "Les résultats et observations ont été enregistrés avec succès.",
                    parent=me,
                )
                me.destroy()

        button = customtkinter.CTkButton(me, text="Enregistrer", command=test)
        button.pack(padx=20, pady=10, anchor=customtkinter.E)

        me.mainloop()

    def send_analysis(self):
        if all((self.code2.get(), self.entry9.get())):
            messagebox.showinfo(
                "Analyse envoyée", "Analyse envoyée avec succès!", parent=self.master
            )
        else:
            messagebox.showerror(
                "Erreur", "Veuillez remplir tous les champs.", parent=self.master
            )


class Plaintes(Window):
    def build(self, app):

        app = customtkinter.CTk()

        app.title("Les Plaintes")
        app.geometry("800x350")
        app.resizable(False, False)

        frame = customtkinter.CTkFrame(app)

        lbl1 = customtkinter.CTkLabel(
            app, text="Bienvenue dans vos tâches", font=("Madimi One Regular", 30)
        )

        gerap = customtkinter.CTkButton(
            app,
            text="Gérer les Rapport",
            command=self.rapportt,
            font=("Madimi One Regular", 18),
            hover_color="black",
            height=80,
            border_width=1,
            border_color="black",
            width=300,
            corner_radius=20,
        )
        ordr = customtkinter.CTkButton(
            app,
            text="Rédaction des plaintes",
            command=self.redplnt,
            font=("Madimi One Regular", 18),
            hover_color="black",
            height=80,
            border_width=1,
            border_color="black",
            width=300,
            corner_radius=20,
        )

        lbl1.pack(pady=(40, 15))
        gerap.pack(pady=(40, 20))
        ordr.pack()

        app.mainloop()

    def redplnt(self):

        app = customtkinter.CTk()

        app.title("Rédaction des plaintes")
        app.geometry("800x500")
        app.resizable(False, False)
        frame = customtkinter.CTkFrame(app)

        lbl1 = customtkinter.CTkLabel(
            app,
            text="Vous pouvez rédiger la plainte que vous souhaitez envoyer au gérant",
            font=("Madimi One Regular", 21),
        )
        sujrap = customtkinter.CTkLabel(
            frame, text="Sujet du rapport:", font=("Madimi One Regular", 18)
        )
        sujrapentr = customtkinter.CTkEntry(
            frame,
            font=("Madimi One Regular", 15),
            height=30,
            width=250,
            border_color="light blue",
        )

        reda = customtkinter.CTkLabel(
            frame, text="Rédaction:", font=("Madimi One Regular", 18)
        )
        redaentr = customtkinter.CTkTextbox(
            frame,
            font=("Madimi One Regular", 15),
            width=600,
            height=150,
            border_width=1,
            border_color="light blue",
        )

        def effacer_contenu():
            sujrapentr.delete(0, "end")
            redaentr.delete("1.0", "end")

        def test():
            if sujrapentr.get() == "" or redaentr.get() == "":
                messagebox.showerror(
                    "Erreur", "Veuillez remplir tous les champs.", parent=app
                )
            else:
                messagebox.showinfo("Content", "le message envoyer", parent=app)

        efface = customtkinter.CTkButton(
            app,
            text="Effacer",
            font=("Madimi One Regular", 18),
            hover_color="black",
            command=effacer_contenu,
        )
        enregistre = customtkinter.CTkButton(
            app,
            text="Envoyer",
            font=("Madimi One Regular", 18),
            hover_color="black",
            command=test,
        )

        lbl1.grid(row=0, column=0, pady=(30, 30), padx=80)
        sujrap.grid(row=0, column=0, padx=(0, 400), pady=(20, 5))
        sujrapentr.grid(row=1, column=0, padx=(0, 295), pady=(0, 20))
        reda.grid(row=2, column=0, padx=(0, 450), pady=(0, 5))
        redaentr.grid(row=3, column=0, padx=(50, 0), pady=(0, 30))
        efface.grid(row=3, column=0, padx=(0, 150), pady=30)
        enregistre.grid(row=3, column=0, padx=(150, 0), pady=30)

        frame.grid(row=2, column=0, sticky="nsew", padx=50)

        app.mainloop()

    def rapportt(self):

        app = customtkinter.CTk()

        app.title("Rapports")
        app.geometry("800x460")
        app.resizable(False, False)
        frame = customtkinter.CTkFrame(app)

        lbl1 = customtkinter.CTkLabel(
            app,
            text="Sélectionnez la période pendant laquelle ces rapports ont été enregistrés",
            font=("Madimi One Regular", 21),
        )
        periode = customtkinter.CTkLabel(
            app, text="Période:", font=("Madimi One Regular", 18)
        )

        du = customtkinter.CTkLabel(frame, text="Du", font=("Madimi One Regular", 18))
        au = customtkinter.CTkLabel(frame, text="Au", font=("Madimi One Regular", 18))

        jour = [str(x) for x in range(1, 32)]
        jourvisentr = customtkinter.CTkOptionMenu(
            frame,
            button_hover_color="black",
            values=jour,
            font=("Madimi One Regular", 15),
            height=30,
            width=140,
            dropdown_font=("Madimi One Regular", 14),
            dropdown_hover_color="black",
        )

        mois = [
            "Janvier",
            "Fevrier",
            "Mars",
            "Avril",
            "May",
            "Juin",
            "Juillet",
            "Aout",
            "Septembre",
            "Octobre",
            "Novembre",
            "Decembre",
        ]
        moisvisentr = customtkinter.CTkOptionMenu(
            frame,
            button_hover_color="black",
            values=mois,
            font=("Madimi One Regular", 15),
            height=30,
            width=140,
            dropdown_font=("Madimi One Regular", 14),
            dropdown_hover_color="black",
        )

        annee = [str(x) for x in range(2020, 2025)]
        annevisentr = customtkinter.CTkOptionMenu(
            frame,
            button_hover_color="black",
            values=annee,
            font=("Madimi One Regular", 15),
            height=30,
            width=140,
            dropdown_font=("Madimi One Regular", 14),
            dropdown_hover_color="black",
        )

        jourvisentr2 = customtkinter.CTkOptionMenu(
            frame,
            button_hover_color="black",
            values=jour,
            font=("Madimi One Regular", 15),
            height=30,
            width=140,
            dropdown_font=("Madimi One Regular", 14),
            dropdown_hover_color="black",
        )

        moisvisentr2 = customtkinter.CTkOptionMenu(
            frame,
            button_hover_color="black",
            values=mois,
            font=("Madimi One Regular", 15),
            height=30,
            width=140,
            dropdown_font=("Madimi One Regular", 14),
            dropdown_hover_color="black",
        )

        annevisentr2 = customtkinter.CTkOptionMenu(
            frame,
            button_hover_color="black",
            values=annee,
            font=("Madimi One Regular", 15),
            height=30,
            width=140,
            dropdown_font=("Madimi One Regular", 14),
            dropdown_hover_color="black",
        )
        rece = customtkinter.CTkButton(
            app,
            text="Recevoir",
            font=("Madimi One Regular", 18),
            hover_color="black",
            command=self.rapports,
        )

        lbl1.grid(row=0, column=0, padx=50, pady=30)
        periode.grid(row=1, column=0, padx=(0, 620), pady=(20, 10))
        du.grid(row=0, column=0, pady=(30, 0), padx=(40, 0))
        jourvisentr.grid(row=1, column=0, padx=(140, 10))
        moisvisentr.grid(row=1, column=1, padx=(0, 10))
        annevisentr.grid(row=1, column=2)
        au.grid(row=2, column=0, pady=(20, 0), padx=(40, 0))
        jourvisentr2.grid(row=3, column=0, padx=(140, 10), pady=(0, 50))
        moisvisentr2.grid(row=3, column=1, padx=(0, 10), pady=(0, 50))
        annevisentr2.grid(row=3, column=2, pady=(0, 50))
        rece.grid(row=3, column=0, pady=30)

        frame.grid(row=2, column=0, sticky="nsew", padx=(30, 20))

        app.mainloop()

    def rapports(self):

        app = customtkinter.CTk()

        app.title("Les Rapports")
        app.geometry("800x465")
        app.resizable(False, False)

        frame = customtkinter.CTkFrame(app, height=280)

        lbl1 = customtkinter.CTkLabel(
            app,
            text="Les rapports qui ont été envoyés pendant la période que vous avez spécifiée",
            font=("Madimi One Regular", 21),
        )
        affi = customtkinter.CTkButton(
            app,
            text="Afficher",
            font=("Madimi One Regular", 18),
            hover_color="black",
            command=self.rapport,
        )

        lbl1.grid(row=0, column=0, padx=50, pady=30)
        affi.grid(row=2, column=0, pady=30)
        frame.grid(row=1, column=0, sticky="nsew", padx=(30, 40))

        app.mainloop()

    def rapport(self):

        app = customtkinter.CTk()
        app.title("Le rapport")
        app.geometry("400x400")

        app.mainloop()


class Code(Window):
    def build(self, app):
        self.root = customtkinter.CTk()
        self.root.title(" " * 80 + "Générateur de Code")
        self.root.geometry("700x475")

        self.frame = customtkinter.CTkFrame(self.root)
        self.frame2 = customtkinter.CTkFrame(self.root)

        self.lbl1 = customtkinter.CTkLabel(
            self.root,
            text="Entrez les informations du patient et le nom de l'analyse",
            font=("Madimi One Regular", 21),
        )
        self.pat = customtkinter.CTkLabel(
            self.root, text="Patient", font=("Madimi One Regular", 19)
        )
        self.ana = customtkinter.CTkLabel(
            self.root, text="Analyse", font=("Madimi One Regular", 19)
        )

        self.nom = customtkinter.CTkLabel(
            self.frame, text="Nom:", font=("Madimi One Regular", 18)
        )
        self.pre = customtkinter.CTkLabel(
            self.frame, text="Prénom:", font=("Madimi One Regular", 18)
        )
        self.nomentr = customtkinter.CTkEntry(
            self.frame, font=("Madimi One Regular", 15), height=30
        )
        self.preentr = customtkinter.CTkEntry(
            self.frame, font=("Madimi One Regular", 15), height=30
        )
        self.age = customtkinter.CTkLabel(
            self.frame, text="Age:", font=("Madimi One Regular", 18)
        )
        self.agentr = customtkinter.CTkEntry(
            self.frame, font=("Madimi One Regular", 15), height=30
        )

        self.abrv = customtkinter.CTkLabel(
            self.frame2, text="L'abréviation du nom:\n", font=("Madimi One Regular", 18)
        )
        self.analyse = [
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
        self.abrventr = customtkinter.CTkOptionMenu(
            self.frame2,
            values=self.analyse,
            font=("Madimi One Regular", 15),
            height=30,
            dropdown_font=("Madimi One Regular", 14),
            width=142,
        )
        self.generer = customtkinter.CTkButton(
            self.root,
            text="Générer le code",
            font=("Madimi One Regular", 18),
            hover_color="black",
            command=self.generer_code,
        )

        self.lbl1.grid(row=0, column=0, pady=(30, 20), padx=80)
        self.pat.grid(row=1, column=0, padx=(0, 300), pady=(10, 5))
        self.ana.grid(row=1, column=0, padx=(300, 0), pady=(10, 5))
        self.nom.grid(row=0, column=0, pady=(20, 0), padx=(28, 10))
        self.nomentr.grid(row=0, column=1, pady=(20, 0))
        self.pre.grid(row=1, column=0, pady=(20, 0), padx=(28, 10))
        self.preentr.grid(row=1, column=1, pady=(20, 0))
        self.age.grid(row=2, column=0, pady=(20, 20), padx=(28, 10))
        self.agentr.grid(row=2, column=1, pady=(20, 20))
        self.abrv.grid(row=0, column=0, pady=(50, 0), padx=(50, 0))
        self.abrventr.grid(row=1, column=0, padx=(50, 0))
        self.generer.grid(row=4, column=0, pady=25)

        self.frame.grid(row=2, column=0, sticky="nsew", padx=(70, 350))
        self.frame2.grid(row=2, column=0, sticky="nsew", padx=(350, 70))

        self.frame1 = customtkinter.CTkFrame(self.root, width=500)
        self.frame1.grid(row=3, column=0, pady=10, padx=(70, 70))

        self.lb8 = customtkinter.CTkLabel(
            self.frame1, text="Date et heure :", font=("Madimi One Regular", 14)
        )
        self.lb8.grid(row=0, column=0, pady=5)

        self.day = [str(i) for i in range(1, 32)]
        self.day_combo = customtkinter.CTkComboBox(
            self.frame1, values=self.day, width=70
        )
        self.day_combo.grid(row=1, column=0, padx=10, pady=5)

        self.month = [
            "Janvier",
            "Février",
            "Mars",
            "Avril",
            "Mai",
            "Juin",
            "Juillet",
            "Août",
            "Septembre",
            "Octobre",
            "Novembre",
            "Décembre",
        ]
        self.month_combo = customtkinter.CTkComboBox(
            self.frame1, values=self.month, width=110
        )
        self.month_combo.grid(row=1, column=1, padx=10, pady=5)

        self.year = [str(i) for i in range(2022, 2030)]
        self.year_combo = customtkinter.CTkComboBox(
            self.frame1, values=self.year, width=70
        )
        self.year_combo.grid(row=1, column=2, padx=10, pady=5)

        self.time = customtkinter.CTkLabel(self.frame1, text="à:")
        self.time.grid(row=1, column=3, padx=4, pady=5)

        self.time_entry = customtkinter.CTkEntry(
            self.frame1, placeholder_text="8:00", width=60
        )
        self.time_entry.grid(row=1, column=4, padx=4, pady=5)

        self.root.mainloop()

    def generer_code(self):
        nom_patient = self.nomentr.get()
        prenom_patient = self.preentr.get()
        age_patient = self.agentr.get()
        selected_day = self.day_combo.get()
        selected_month = self.month_combo.get()
        selected_year = self.year_combo.get()
        selected_time = self.time_entry.get()
        abv = self.abrventr.get()

        if not (
            nom_patient
            and prenom_patient
            and age_patient
            and selected_day
            and selected_month
            and selected_year
            and selected_time
        ):
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
            return

        if not (nom_patient.isalpha() and prenom_patient.isalpha()):
            messagebox.showerror(
                "Erreur", "Le nom et le prénom doivent contenir uniquement des lettres."
            )
            return

        if not age_patient.isdigit():
            messagebox.showerror("Erreur", "L'âge doit être un nombre.")
            return

        if not re.match(r"^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$", selected_time):
            messagebox.showerror(
                "Erreur",
                "Format d'heure invalide. Veuillez saisir une heure au format HH:MM.",
            )
            return

        abreviation_nom = nom_patient[0] + prenom_patient[0]
        date_entree = f"{selected_day}-{selected_month}-{selected_year} {selected_time}"

        messagebox.showinfo(
            "Code",
            f"Le code est : {abreviation_nom}-{age_patient}-{abv}\n La date et heure est : {date_entree}",
        )
