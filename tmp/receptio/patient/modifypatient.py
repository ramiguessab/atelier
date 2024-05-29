import customtkinter
from customtkinter import *
from messagebox.success import succ


def mod(root):
    root = customtkinter.CTk()
    customtkinter.set_default_color_theme("green")

    root.title("Les Patiens")
    root.geometry("850x560")
    ("icons/edit.ico")
    root.resizable(False, False)

    frame = customtkinter.CTkFrame(root, border_width=1, border_color="#676767")

    def eff():
        nomentr.delete("0", END)

        preentr.delete("0", END)

        numentr.delete("0", END)

        abrventr.delete("0", END)

        prixentr.delete("0", END)

        txt.configure(state="normal")
        txt.delete("0.0", END)
        txt.configure(state="disabled")

        checkbox_var.set(False)

        reduentr.set(value="OUI")
        analysentr.set(value="NFS")

    def suc():
        eff()
        succ("La modification a été apportée au patient que vous avez sélectionné")
        root.destroy()

    def checked():
        if check.get() == 1:
            txt.configure(state="normal")
        else:
            txt.configure(state="disabled")

    lbl1 = customtkinter.CTkLabel(
        root,
        text="Entrez les modifications que vous souhaitez",
        font=("Madimi One Regular", 21),
    )

    nom = customtkinter.CTkLabel(frame, text="Nom:", font=("Madimi One Regular", 18))
    pre = customtkinter.CTkLabel(frame, text="Prénom:", font=("Madimi One Regular", 18))
    nomentr = customtkinter.CTkEntry(frame, font=("Madimi One Regular", 15), height=30)
    preentr = customtkinter.CTkEntry(frame, font=("Madimi One Regular", 15), height=30)
    num = customtkinter.CTkLabel(
        frame, text="Num Telephone:", font=("Madimi One Regular", 18)
    )
    numentr = customtkinter.CTkEntry(
        frame, font=("Madimi One Regular", 15), height=30, placeholder_text="07********"
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
    abrv = customtkinter.CTkLabel(
        frame, text="Abréviation:", font=("Madimi One Regular", 18)
    )
    abrventr = customtkinter.CTkEntry(
        frame, font=("Madimi One Regular", 15), height=30, placeholder_text="NFS"
    )

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

    checkbox_var = BooleanVar(value=False)
    check = customtkinter.CTkCheckBox(
        frame,
        text="Cliquez pour ouvrir la zone de saisie \ndes nouveaux enregistrements du patient",
        font=("Madimi One Regular", 15),
        hover_color="#A07832",
        border_width=2,
        fg_color="#A07832",
        command=checked,
        variable=checkbox_var,
    )

    txt = customtkinter.CTkTextbox(
        frame, height=50, width=310, font=("Madimi One Regular", 13), state="disabled"
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
    num.grid(row=3, column=1, padx=(70, 0), pady=(0, 3))
    numentr.grid(row=4, column=1, padx=(70, 10), pady=(0, 10))
    nomanalyse.grid(row=3, column=0, padx=(70, 0), pady=(5, 3))
    analysentr.grid(row=4, column=0, padx=(70, 0), pady=(0, 10))
    abrv.grid(row=7, column=0, padx=(50, 0), pady=(5, 3))
    abrventr.grid(row=8, column=0, padx=(70, 0), pady=(0, 10))
    redu.grid(row=9, column=0, padx=(40, 0), pady=(5, 3))
    prix.grid(row=11, column=0, pady=(5, 0))
    reduentr.grid(row=10, column=0, padx=(70, 0), pady=(0, 10))
    prixentr.grid(row=12, column=0, padx=(80, 10), pady=(0, 30))
    check.grid(column=1, row=8, padx=(200, 75))
    txt.grid(column=1, row=(10), padx=(130, 0))

    frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=10)

    efface.grid(row=2, column=1, padx=(0, 150), pady=10)
    enregistre.grid(row=2, column=1, padx=(150, 0), pady=10)

    root.mainloop()
