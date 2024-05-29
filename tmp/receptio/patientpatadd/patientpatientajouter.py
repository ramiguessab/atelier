import customtkinter
from customtkinter import *
from messagebox.success import succ


def patpatadd(root):
    root = customtkinter.CTk()
    customtkinter.set_default_color_theme("green")

    root.title("Les Patiens")
    root.geometry("850x390")
    ("icons/edit.ico")
    root.resizable(False, False)

    frame = customtkinter.CTkFrame(root, border_width=1, border_color="#676767")

    def eff():
        nomentr.delete("0", END)

        preentr.delete("0", END)

        numentr.delete("0", END)

        abrventr.delete("0", END)

        prixentr.delete("0", END)

        sexentr.set("Male")
        analysentr.set("NFS")
        jourentr.set("1")
        moisentr.set("Janvier")
        anneentr.set("1950")
        jourvisentr.set("1")
        moisvisentr.set("Janvier")
        annevisentr.set("2024")
        reduentr.set("OUI")

    def suc():
        eff()
        succ("Le patient a été modifier")
        root.destroy()

    lbl1 = customtkinter.CTkLabel(
        root,
        text="Modifier les informations du patient",
        font=("Madimi One Regular", 21),
    )

    nom = customtkinter.CTkLabel(frame, text="Nom:", font=("Madimi One Regular", 18))
    pre = customtkinter.CTkLabel(frame, text="Prénom:", font=("Madimi One Regular", 18))
    nomentr = customtkinter.CTkEntry(frame, font=("Madimi One Regular", 15), height=30)
    preentr = customtkinter.CTkEntry(frame, font=("Madimi One Regular", 15), height=30)
    sexe = customtkinter.CTkLabel(frame, text="Sexe:", font=("Madimi One Regular", 18))
    num = customtkinter.CTkLabel(
        frame, text="Num Telephone:", font=("Madimi One Regular", 18)
    )
    sexentr = customtkinter.CTkOptionMenu(
        frame,
        values=["Male", "Female", "Autre"],
        font=("Madimi One Regular", 15),
        height=30,
        button_color="#A07832",
        fg_color="#D6A041",
        button_hover_color="#725624",
        dropdown_font=("Madimi One Regular", 14),
        dropdown_hover_color="black",
    )
    numentr = customtkinter.CTkEntry(
        frame, font=("Madimi One Regular", 15), height=30, placeholder_text="07********"
    )
    nomanalyse = customtkinter.CTkLabel(
        frame, text="Nom d'analyse:", font=("Madimi One Regular", 18)
    )
    analyse = ["NFS", "ALAT", "ASLO", "CREA", "GPP", "VDRL"]
    analysentr = customtkinter.CTkOptionMenu(
        frame,
        button_color="#A07832",
        fg_color="#D6A041",
        button_hover_color="#725624",
        values=analyse,
        font=("Madimi One Regular", 15),
        height=30,
        dropdown_font=("Madimi One Regular", 14),
        dropdown_hover_color="black",
    )
    datenai = customtkinter.CTkLabel(
        frame, text="Date de Naissance:", font=("Madimi One Regular", 18)
    )

    jour = [str(x) for x in range(1, 32)]
    jourentr = customtkinter.CTkOptionMenu(
        frame,
        button_color="#A07832",
        fg_color="#D6A041",
        button_hover_color="#725624",
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
    moisentr = customtkinter.CTkOptionMenu(
        frame,
        button_color="#A07832",
        fg_color="#D6A041",
        button_hover_color="#725624",
        values=mois,
        font=("Madimi One Regular", 15),
        height=30,
        width=140,
        dropdown_font=("Madimi One Regular", 14),
        dropdown_hover_color="black",
    )

    annee = [str(x) for x in range(1950, 2024)]
    anneentr = customtkinter.CTkOptionMenu(
        frame,
        button_color="#A07832",
        fg_color="#D6A041",
        button_hover_color="#725624",
        values=annee,
        font=("Madimi One Regular", 15),
        height=30,
        width=140,
        dropdown_font=("Madimi One Regular", 14),
        dropdown_hover_color="black",
    )
    abrv = customtkinter.CTkLabel(
        frame, text="Abréviation:", font=("Madimi One Regular", 18)
    )
    datevis = customtkinter.CTkLabel(
        frame, text="Date de Visite:", font=("Madimi One Regular", 18)
    )
    abrventr = customtkinter.CTkEntry(
        frame, font=("Madimi One Regular", 15), height=30, placeholder_text="NFS"
    )
    jourvisentr = customtkinter.CTkOptionMenu(
        frame,
        button_color="#A07832",
        fg_color="#D6A041",
        button_hover_color="#725624",
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
        button_color="#A07832",
        fg_color="#D6A041",
        button_hover_color="#725624",
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
        button_color="#A07832",
        fg_color="#D6A041",
        button_hover_color="#725624",
        values=annee,
        font=("Madimi One Regular", 15),
        height=30,
        width=140,
        dropdown_font=("Madimi One Regular", 14),
        dropdown_hover_color="black",
    )
    annevisentr.set("2024")

    redu = customtkinter.CTkLabel(
        frame, text="Réduction:", font=("Madimi One Regular", 18)
    )
    prix = customtkinter.CTkLabel(frame, text="Prix:", font=("Madimi One Regular", 18))
    reduentr = customtkinter.CTkOptionMenu(
        frame,
        button_color="#A07832",
        fg_color="#D6A041",
        button_hover_color="#725624",
        values=["OUI", "NON"],
        font=("Madimi One Regular", 15),
        height=30,
        dropdown_font=("Madimi One Regular", 14),
        dropdown_hover_color="black",
    )
    prixentr = customtkinter.CTkEntry(
        frame,
        font=("Madimi One Regular", 15),
        height=30,
        fg_color="#E1E1E1",
        text_color="black",
        placeholder_text="**DA",
        placeholder_text_color="#848484",
    )
    efface = customtkinter.CTkButton(
        root,
        text="Effacer",
        font=("Madimi One Regular", 18),
        command=eff,
        fg_color="#FFC552",
        hover_color="#A8833A",
        border_width=2,
        border_color="white",
        text_color="black",
    )
    enregistre = customtkinter.CTkButton(
        root,
        text="Enregistrer",
        font=("Madimi One Regular", 18),
        command=suc,
        fg_color="#FFC552",
        hover_color="#A8833A",
        border_width=2,
        border_color="white",
        text_color="black",
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
    # nomanalyse.grid(row=5, column=0, padx=(70, 0), pady=(5, 3))
    datenai.grid(row=6, column=0, padx=(90, 0), pady=(5, 3))
    jourentr.grid(row=6, column=1, padx=(60, 0), pady=(25, 25))
    moisentr.grid(row=6, column=2, padx=(0, 10), pady=(25, 25))
    anneentr.grid(row=6, column=3, padx=(0, 60), pady=(25, 25))
    # analysentr.grid(row=6, column=0, padx=(70, 0), pady=(0, 10))
    # abrv.grid(row=7, column=0, padx=(50, 0), pady=(5, 3))
    # datevis.grid(row=7, column=1, padx=(60, 0), pady=(5, 3))
    # abrventr.grid(row=8, column=0, padx=(70, 0), pady=(0, 10))
    # jourvisentr.grid(row=8, column=1, padx=(60, 0), pady=(0, 10))
    # moisvisentr.grid(row=8, column=2, padx=(3, 20), pady=(0, 10))
    # annevisentr.grid(row=8, column=3, padx=(0, 60), pady=(0, 10))
    # redu.grid(row=9, column=0, padx=(40, 0), pady=(5, 3))
    # prix.grid(row=9, column=1, pady=(5, 3))
    # reduentr.grid(row=10, column=0, padx=(70, 0), pady=(0, 30))
    # prixentr.grid(row=10, column=1, padx=(70, 10), pady=(0, 30))

    frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=10)

    efface.grid(row=2, column=1, padx=(0, 150), pady=10)
    enregistre.grid(row=2, column=1, padx=(150, 0), pady=10)

    root.mainloop()
