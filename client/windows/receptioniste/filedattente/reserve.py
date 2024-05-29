import customtkinter
from client.window import Window


class Reservation(Window):
    def __init__(self) -> None:
        super().__init__("Ajouter reservation")

    def build(self, root):
        root.geometry("850x550")
        root.resizable(False, False)

        root = customtkinter.CTkFrame(master=root)
        root.pack()

        frame = customtkinter.CTkFrame(root)

        lbl1 = customtkinter.CTkLabel(
            root,
            text="Entrez les informations du nouveau patient",
        )

        nom = customtkinter.CTkLabel(frame, text="Nom:")
        pre = customtkinter.CTkLabel(frame, text="Prénom:")
        nomentr = customtkinter.CTkEntry(frame)
        preentr = customtkinter.CTkEntry(frame)
        sexe = customtkinter.CTkLabel(frame, text="Sexe:")
        num = customtkinter.CTkLabel(frame, text="Num Telephone:")
        sexentr = customtkinter.CTkOptionMenu(
            frame,
            values=["Male", "Female"],
        )
        numentr = customtkinter.CTkEntry(
            frame,
            placeholder_text="07********",
        )
        nomanalyse = customtkinter.CTkLabel(frame, text="Nom d'analyse:")
        analyse = ["NFS", "ALAT", "ASLO", "CREA", "GPP", "VDRL"]
        analysentr = customtkinter.CTkOptionMenu(
            frame,
            values=analyse,
        )
        datenai = customtkinter.CTkLabel(frame, text="Date de Naissance:")
        jour = [str(x) for x in range(1, 32)]
        jourentr = customtkinter.CTkOptionMenu(frame, values=jour)

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
        moisentr = customtkinter.CTkOptionMenu(frame, values=mois)

        annee = [str(x) for x in range(1950, 2024)]
        anneentr = customtkinter.CTkOptionMenu(
            frame,
            values=annee,
        )
        abrv = customtkinter.CTkLabel(frame, text="Abréviation:")
        datevis = customtkinter.CTkLabel(frame, text="Date de Visite:")
        abrventr = customtkinter.CTkEntry(frame, placeholder_text="NFS")
        jourvisentr = customtkinter.CTkOptionMenu(
            frame,
            values=jour,
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
            values=mois,
        )

        annee = [str(x) for x in range(2020, 2025)]
        annevisentr = customtkinter.CTkOptionMenu(
            frame,
            values=annee,
        )

        redu = customtkinter.CTkLabel(frame, text="Réduction:")
        prix = customtkinter.CTkLabel(frame, text="Prix:")
        reduentr = customtkinter.CTkOptionMenu(
            frame,
            values=["OUI", "NON"],
        )
        prixentr = customtkinter.CTkEntry(
            frame,
        )
        efface = customtkinter.CTkButton(
            root,
            text="Effacer",
            # command=eff,
        )
        enregistre = customtkinter.CTkButton(
            root,
            text="Enregistrer",
            # command=suc,
        )

        lbl1.grid(row=0, column=1, pady=(20, 15), padx=(70, 40))
        nom.grid(row=1, column=0, pady=(10, 3))
        pre.grid(row=1, column=1, padx=(10, 0), pady=(10, 3))
        nomentr.grid(row=2, column=0, padx=(70, 0), pady=(0, 10))
        preentr.grid(row=2, column=1, padx=(70, 10), pady=(0, 10))
        sexe.grid(row=3, column=0, pady=(0, 3))
        num.grid(row=3, column=1, padx=(70, 0), pady=(0, 3))
        sexentr.grid(row=4, column=0, padx=(70, 0), pady=(0, 10))
        numentr.grid(row=4, column=1, padx=(70, 10), pady=(0, 10))
        nomanalyse.grid(row=5, column=0, padx=(70, 0), pady=(5, 3))
        datenai.grid(row=5, column=1, padx=(90, 0), pady=(5, 3))
        jourentr.grid(row=6, column=1, padx=(60, 0), pady=(0, 10))
        moisentr.grid(row=6, column=2, padx=(3, 20), pady=(0, 10))
        anneentr.grid(row=6, column=3, padx=(0, 60), pady=(0, 10))
        analysentr.grid(row=6, column=0, padx=(70, 0), pady=(0, 10))
        abrv.grid(row=7, column=0, padx=(50, 0), pady=(5, 3))
        datevis.grid(row=7, column=1, padx=(60, 0), pady=(5, 3))
        abrventr.grid(row=8, column=0, padx=(70, 0), pady=(0, 10))
        jourvisentr.grid(row=8, column=1, padx=(60, 0), pady=(0, 10))
        moisvisentr.grid(row=8, column=2, padx=(3, 20), pady=(0, 10))
        annevisentr.grid(row=8, column=3, padx=(0, 60), pady=(0, 10))
        redu.grid(row=9, column=0, padx=(40, 0), pady=(5, 3))
        prix.grid(row=9, column=1, pady=(5, 3))
        reduentr.grid(row=10, column=0, padx=(70, 0), pady=(0, 30))
        prixentr.grid(row=10, column=1, padx=(70, 10), pady=(0, 30))

        frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=10)

        efface.grid(row=2, column=1, padx=(0, 150), pady=10)
        enregistre.grid(row=2, column=1, padx=(150, 0), pady=10)


# def reserve(root):
#     root = customtkinter.CTk()
#     customtkinter.set_default_color_theme("green")

#     def eff():
#         nomentr.delete("0", END)

#         preentr.delete("0", END)

#         numentr.delete("0", END)

#         abrventr.delete("0", END)

#         prixentr.delete("0", END)

#         sexentr.set("Male")
#         analysentr.set("NFS")
#         jourentr.set("1")
#         moisentr.set("Janvier")
#         anneentr.set("1950")
#         jourvisentr.set("1")
#         moisvisentr.set("Janvier")
#         annevisentr.set("2024")
#         reduentr.set("OUI")

#     def suc():
#         eff()
#         succ("Le rendez-vous a été réservé")
#         root.destroy()

#     root.mainloop()
