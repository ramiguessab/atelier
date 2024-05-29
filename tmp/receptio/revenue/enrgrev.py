import customtkinter
from customtkinter import *
from messagebox.success import succ
from messagebox.yesno import ask


def enrgrev(root):
    root = customtkinter.CTk()

    root.title("Les Revenus")
    root.geometry("555x540")
    ("icons/edit.ico")
    root.resizable(False, False)

    def eff():
        nomentr.delete("0", END)

        preentr.delete("0", END)

        revtotentr.delete("0", END)

        taureduentr.delete("0", END)

        prixentr.delete("0", END)

        detailentr.delete("0.0", END)

        analysentr.set("NFS")
        reduentr.set("OUI")

    def succs():
        eff()
        succ("Les données ont été enregistrées")

    def yn():
        ask("Voulez-vous imprimer la facture ?")

    frame = customtkinter.CTkFrame(root)

    lbl1 = customtkinter.CTkLabel(
        root,
        text="Entrez les revenus du nouveau patient",
        font=("Madimi One Regular", 21),
    )

    nom = customtkinter.CTkLabel(
        frame, text="Nom du patient:", font=("Madimi One Regular", 18)
    )
    pre = customtkinter.CTkLabel(
        frame, text="Prénom \ndu patient:", font=("Madimi One Regular", 18)
    )
    nomentr = customtkinter.CTkEntry(frame, font=("Madimi One Regular", 15), height=30)
    preentr = customtkinter.CTkEntry(frame, font=("Madimi One Regular", 15), height=30)
    redu = customtkinter.CTkLabel(
        frame, text="Réduction:", font=("Madimi One Regular", 18)
    )
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
    revtot = customtkinter.CTkLabel(
        frame,
        text="Les revenus totales \nde la journée:",
        font=("Madimi One Regular", 18),
    )
    revtotentr = customtkinter.CTkEntry(
        frame, font=("Madimi One Regular", 15), height=30
    )
    tauredu = customtkinter.CTkLabel(
        frame, text="Le taux \nde réduction:", font=("Madimi One Regular", 18)
    )
    taureduentr = customtkinter.CTkEntry(
        frame, font=("Madimi One Regular", 15), height=30
    )

    detail = customtkinter.CTkLabel(
        frame, text="Détails:", font=("Madimi One Regular", 18)
    )
    detailentr = customtkinter.CTkTextbox(
        frame,
        font=("Madimi One Regular", 15),
        height=120,
        width=120,
        border_width=1,
        border_color="#A2A2A2",
    )

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
        width=142,
    )
    prix = customtkinter.CTkLabel(frame, text="Prix:", font=("Madimi One Regular", 18))
    prixentr = customtkinter.CTkEntry(
        frame,
        font=("Madimi One Regular", 15),
        height=30,
        fg_color="#E1E1E1",
        text_color="black",
        placeholder_text="**DA",
        placeholder_text_color="#848484",
    )

    generer = customtkinter.CTkButton(
        root,
        text="Générer \nla facture",
        font=("Madimi One Regular", 18),
        fg_color="#FFC552",
        hover_color="#A8833A",
        border_width=2,
        border_color="white",
        text_color="black",
        command=yn,
    )
    enregistre = customtkinter.CTkButton(
        root,
        text="Enregistrer",
        font=("Madimi One Regular", 18),
        fg_color="#FFC552",
        hover_color="#A8833A",
        border_width=2,
        border_color="white",
        text_color="black",
        height=57,
        command=succs,
    )

    lbl1.grid(row=0, column=0, pady=30)
    nom.grid(row=0, column=0, padx=(20, 0))
    redu.grid(row=0, column=1, padx=(20, 0))
    revtot.grid(row=0, column=2, padx=(20, 20), pady=(10, 5))
    nomentr.grid(row=1, column=0, padx=(20, 0))
    reduentr.grid(row=1, column=1, padx=(20, 0))
    revtotentr.grid(row=1, column=2, padx=(20, 20))
    pre.grid(row=3, column=0, pady=(0, 50), padx=(20, 0))
    preentr.grid(row=3, column=0, pady=(40, 0), padx=(20, 0))
    tauredu.grid(row=3, column=1, pady=(0, 50), padx=(20, 0))
    taureduentr.grid(row=3, column=1, pady=(40, 0), padx=(20, 0))
    detail.grid(row=2, column=2, padx=(20, 20), pady=(20, 0))
    detailentr.grid(row=3, column=2, padx=(20, 20))
    nomanalyse.grid(row=4, column=0, padx=(20, 0))
    analysentr.grid(row=5, column=0, padx=(20, 0), pady=(0, 30))
    prix.grid(row=4, column=1, padx=(20, 0))
    prixentr.grid(row=5, column=1, padx=(20, 0), pady=(0, 30))
    enregistre.grid(row=2, column=0, padx=(0, 150), pady=20)
    generer.grid(row=2, column=0, padx=(150, 0), pady=20)

    frame.grid(row=1, column=0, padx=20)

    root.mainloop()
