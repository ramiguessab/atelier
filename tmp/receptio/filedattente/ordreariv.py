import customtkinter
from messagebox.success import succ


def ordrarv(root):

    root = customtkinter.CTk()

    def gen():
        succ("Le ticket a été imprimé")
        root.destroy()

    root.title("Ordre d'arrivé des patients")
    root.geometry("1184x532")
    ("icons/edit.ico")
    root.resizable(False, False)

    frame = customtkinter.CTkFrame(root)
    frame2 = customtkinter.CTkFrame(root)
    lbl1 = customtkinter.CTkLabel(
        root,
        text="Remplissez ces informations \npour générer un ticket",
        font=("Madimi One Regular", 21),
    )
    lbl2 = customtkinter.CTkLabel(
        root, text="Contrôle de l'affichage", font=("Madimi One Regular", 21)
    )
    pat = customtkinter.CTkLabel(frame, text="Patient", font=("Madimi One Regular", 19))

    nom = customtkinter.CTkLabel(frame, text="Nom:", font=("Madimi One Regular", 18))
    prenom = customtkinter.CTkLabel(
        frame, text="Prenom:", font=("Madimi One Regular", 18)
    )
    nomentr = customtkinter.CTkEntry(
        frame, font=("Madimi One Regular", 16), height=30, width=120
    )
    preentr = customtkinter.CTkEntry(
        frame, font=("Madimi One Regular", 16), height=30, width=120
    )
    nomana = customtkinter.CTkLabel(
        frame, text="Nom d'analyse:", font=("Madimi One Regular", 18)
    )
    analyse = [
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
    anaentr = customtkinter.CTkOptionMenu(
        frame,
        button_color="#A07832",
        fg_color="#D6A041",
        button_hover_color="#725624",
        values=analyse,
        font=("Madimi One Regular", 15),
        height=30,
        width=142,
        dropdown_font=("Madimi One Regular", 14),
        dropdown_hover_color="black",
    )
    numordr = customtkinter.CTkLabel(
        frame, text="Numéro d'ordre:", font=("Madimi One Regular", 18)
    )
    numordrentr = customtkinter.CTkEntry(
        frame, font=("Madimi One Regular", 16), height=30, width=50
    )
    date = customtkinter.CTkLabel(frame, text="Date:", font=("Madimi One Regular", 18))
    jour = [str(x) for x in range(1, 32)]
    jourentr = customtkinter.CTkOptionMenu(
        frame,
        button_color="#A07832",
        fg_color="#D6A041",
        button_hover_color="#725624",
        values=jour,
        font=("Madimi One Regular", 15),
        height=30,
        width=130,
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
        width=130,
        dropdown_font=("Madimi One Regular", 14),
        dropdown_hover_color="black",
    )

    annee = [str(x) for x in range(2024, 2025)]
    anneentr = customtkinter.CTkOptionMenu(
        frame,
        button_color="#A07832",
        fg_color="#D6A041",
        button_hover_color="#725624",
        values=annee,
        font=("Madimi One Regular", 15),
        height=30,
        width=130,
        dropdown_font=("Madimi One Regular", 14),
        dropdown_hover_color="black",
    )

    npavant = customtkinter.CTkLabel(
        frame, text="Nbr de personne\navant vous:", font=("Madimi One Regular", 18)
    )
    npavantentr = customtkinter.CTkEntry(
        frame, font=("Madimi One Regular", 16), height=30, width=50
    )

    nomana2 = customtkinter.CTkLabel(
        frame2, text="Nom d'analyse:", font=("Madimi One Regular", 18)
    )
    anaentr2 = customtkinter.CTkOptionMenu(
        frame2,
        button_color="#A07832",
        fg_color="#D6A041",
        button_hover_color="#725624",
        values=analyse,
        font=("Madimi One Regular", 15),
        height=30,
        width=142,
        dropdown_font=("Madimi One Regular", 14),
        dropdown_hover_color="black",
    )

    ordrpat = customtkinter.CTkLabel(
        frame2, text="Ordre des patients:", font=("Madimi One Regular", 18)
    )
    ordrpatentr = customtkinter.CTkEntry(
        frame2, font=("Madimi One Regular", 16), height=30, width=50
    )

    place = customtkinter.CTkLabel(
        frame2,
        text="Places disponible\npour les analyses:",
        font=("Madimi One Regular", 18),
    )
    placentr = customtkinter.CTkTextbox(
        frame2, height=160, width=140, font=("Madimi One Regular", 16)
    )

    generer = customtkinter.CTkButton(
        root,
        text="Générer le ticket",
        font=("Madimi One Regular", 18),
        fg_color="#FFC552",
        hover_color="#A8833A",
        border_width=2,
        border_color="white",
        text_color="black",
        command=gen,
    )
    affichage = customtkinter.CTkButton(
        root,
        text="Affichage",
        font=("Madimi One Regular", 18),
        fg_color="#FFC552",
        hover_color="#A8833A",
        border_width=2,
        border_color="white",
        text_color="black",
    )
    actualiser = customtkinter.CTkButton(
        root,
        text="Actualiser",
        font=("Madimi One Regular", 18),
        fg_color="#FFC552",
        hover_color="#A8833A",
        border_width=2,
        border_color="white",
        text_color="black",
    )

    a = customtkinter.CTkLabel(frame, text="à", font=("Madimi One Regular", 18))
    aentr = customtkinter.CTkEntry(
        frame,
        font=("Madimi One Regular", 16),
        height=30,
        width=58,
        placeholder_text="00:00",
    )

    lbl1.grid(row=0, column=0, pady=(20, 20))
    lbl2.grid(row=0, column=1)

    pat.grid(row=0, column=2, pady=20)
    nom.grid(row=1, column=0, pady=(0, 25))
    prenom.grid(row=1, column=3, pady=(0, 25))
    nomentr.grid(row=1, column=1, pady=(0, 25))
    preentr.grid(row=1, column=4, padx=(20, 30), pady=(0, 25))
    nomana.grid(row=2, column=0, pady=(0, 25), padx=(20, 0))
    anaentr.grid(row=2, column=1, pady=(0, 25))
    numordr.grid(row=3, column=0, pady=(0, 25), padx=(20, 0))
    numordrentr.grid(row=3, column=1, pady=(0, 25))
    date.grid(row=4, column=0, pady=(0, 25))
    jourentr.grid(row=4, column=1, pady=(0, 25))
    moisentr.grid(row=4, column=2, pady=(0, 25), padx=3)
    anneentr.grid(row=4, column=3, pady=(0, 25), padx=(5, 0))
    a.grid(row=4, column=4, pady=(0, 25), padx=(0, 80))
    aentr.grid(row=4, column=4, pady=(0, 25), padx=(20, 0))
    npavant.grid(row=5, column=0, pady=(0, 25), padx=(20, 0))
    npavantentr.grid(row=5, column=1, pady=(0, 25))

    nomana2.grid(row=0, column=0)
    anaentr2.grid(row=0, column=0, pady=(90, 0))
    ordrpat.grid(row=1, column=0, padx=20, pady=(0, 0))
    ordrpatentr.grid(row=1, column=0, pady=(70, 0))
    place.grid(row=0, column=1, pady=10, padx=(20, 40))
    placentr.grid(row=1, column=1, pady=20, padx=(20, 40))

    generer.grid(row=2, column=0, pady=20)
    affichage.grid(row=2, column=1, pady=20, padx=(0, 170))
    actualiser.grid(row=2, column=1, pady=20, padx=(170, 0))

    frame.grid(row=1, column=0, sticky="nsew", padx=20)
    frame2.grid(row=1, column=1, sticky="nsew")

    root.mainloop()
