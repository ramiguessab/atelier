import customtkinter
from customtkinter import *
from messagebox.info import inf


def codi(root):
    root = customtkinter.CTk()

    def cdinfo():
        inf('Le code est "........"')

    root.title("Le code")
    root.geometry("700x375")
    ("icons/edit.ico")
    root.resizable(False, False)
    frame = customtkinter.CTkFrame(root)
    frame2 = customtkinter.CTkFrame(root)

    lbl1 = customtkinter.CTkLabel(
        root,
        text="Entrez les informations du patient et le nom de l'analyse",
        font=("Madimi One Regular", 21),
    )
    pat = customtkinter.CTkLabel(root, text="Patient", font=("Madimi One Regular", 19))
    ana = customtkinter.CTkLabel(root, text="Analyse", font=("Madimi One Regular", 19))

    nom = customtkinter.CTkLabel(frame, text="Nom:", font=("Madimi One Regular", 18))
    pre = customtkinter.CTkLabel(frame, text="Prénom:", font=("Madimi One Regular", 18))
    nomentr = customtkinter.CTkEntry(frame, font=("Madimi One Regular", 15), height=30)
    preentr = customtkinter.CTkEntry(frame, font=("Madimi One Regular", 15), height=30)
    age = customtkinter.CTkLabel(frame, text="Age:", font=("Madimi One Regular", 18))
    agentr = customtkinter.CTkEntry(frame, font=("Madimi One Regular", 15), height=30)

    abrv = customtkinter.CTkLabel(
        frame2, text="L'abréviation du nom:", font=("Madimi One Regular", 18)
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
    abrventr = customtkinter.CTkOptionMenu(
        frame2,
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
    genere = customtkinter.CTkButton(
        root,
        text="Générer le code",
        font=("Madimi One Regular", 18),
        fg_color="#FFC552",
        hover_color="#A8833A",
        border_width=2,
        border_color="white",
        text_color="black",
        command=cdinfo,
    )

    lbl1.grid(row=0, column=0, pady=(30, 20), padx=80)
    pat.grid(row=1, column=0, padx=(0, 300), pady=(10, 5))
    ana.grid(row=1, column=0, padx=(300, 0), pady=(10, 5))
    nom.grid(row=0, column=0, pady=(20, 0), padx=(28, 10))
    nomentr.grid(row=0, column=1, pady=(20, 0))
    pre.grid(row=1, column=0, pady=(20, 0), padx=(28, 10))
    preentr.grid(row=1, column=1, pady=(20, 0))
    age.grid(row=2, column=0, pady=(20, 20), padx=(28, 10))
    agentr.grid(row=2, column=1, pady=(20, 20))
    abrv.grid(row=0, column=0, pady=(50, 0), padx=(50, 0))
    abrventr.grid(row=1, column=0, padx=(50, 0))
    genere.grid(row=3, column=0, pady=25)

    frame.grid(row=2, column=0, sticky="nsew", padx=(70, 350))
    frame2.grid(row=2, column=0, sticky="nsew", padx=(350, 70))

    root.mainloop()
