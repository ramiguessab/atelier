import customtkinter
from customtkinter import *
from revenue.edithisto import edithisto


def historev(root):
    root = customtkinter.CTk()

    root.title("Les Revenus")
    root.geometry("800x400")
    ("icons/edit.ico")
    root.resizable(False, False)

    def eff():
        nomentr.delete("0", END)

        preentr.delete("0", END)

        analysentr.set("NFS")
        jourentr.set("1")
        moisentr.set("Janvier")
        anneentr.set("2024")

    def edhist():
        edithisto(root)

    def kill():
        root.destroy()

    frame = customtkinter.CTkFrame(root)

    lbl1 = customtkinter.CTkLabel(
        root,
        text="Saisissez toutes les informations pour afficher les revenus du patient",
        font=("Madimi One Regular", 21),
    )
    nom = customtkinter.CTkLabel(
        frame, text="Nom du patient:", font=("Madimi One Regular", 18)
    )
    pre = customtkinter.CTkLabel(
        frame, text="Prénom du patient:", font=("Madimi One Regular", 18)
    )
    nomentr = customtkinter.CTkEntry(frame, font=("Madimi One Regular", 15), height=30)
    preentr = customtkinter.CTkEntry(frame, font=("Madimi One Regular", 15), height=30)
    nomanalyse = customtkinter.CTkLabel(
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
        width=300,
    )
    datevis = customtkinter.CTkLabel(
        frame, text="Date de la visite:", font=("Madimi One Regular", 18)
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
        width=100,
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
        width=114,
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
        width=100,
        dropdown_font=("Madimi One Regular", 14),
        dropdown_hover_color="black",
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
        text="Afficher",
        font=("Madimi One Regular", 18),
        command=edhist,
        fg_color="#FFC552",
        hover_color="#A8833A",
        border_width=2,
        border_color="white",
        text_color="black",
    )

    back = customtkinter.CTkButton(
        root,
        text="<",
        font=("Madimi One Regular", 18, "bold"),
        fg_color="#7B1111",
        hover_color="#3D0909",
        border_width=2,
        border_color="white",
        text_color="white",
        width=30,
        command=kill,
    )
    # back.grid(row=2, column=0, padx=(0, 650))

    lbl1.grid(row=0, column=0, padx=60, pady=30)
    nom.grid(row=0, column=0, padx=(120, 0), pady=(30, 0))
    nomentr.grid(row=1, column=0, padx=(120, 0))
    pre.grid(row=2, column=0, padx=(120, 0), pady=(30, 0))
    preentr.grid(row=3, column=0, padx=(120, 0), pady=(0, 40))
    nomanalyse.grid(row=0, column=1, padx=(0, 0), pady=(30, 0))
    analysentr.grid(row=1, column=1, padx=(40, 40))
    datevis.grid(row=2, column=1, pady=(30, 0))
    jourentr.grid(row=3, column=1, padx=(0, 220), pady=(0, 40))
    moisentr.grid(row=3, column=1, pady=(0, 40))
    anneentr.grid(row=3, column=1, padx=(220, 0), pady=(0, 40))
    efface.grid(row=2, column=0, padx=(0, 150), pady=30)
    enregistre.grid(row=2, column=0, padx=(150, 0), pady=30)

    frame.grid(row=1, column=0, sticky="nsew", padx=(40, 20))

    root.mainloop()
