import customtkinter
from customtkinter import *
from revenue.enrgrev import enrgrev
from revenue.historev import historev


def revenue(root):
    root = customtkinter.CTk()

    def enrrev():
        enrgrev(root)

    def histrev():
        historev(root)

    root.title("Les Revenus")
    root.geometry("800x350")
    ("icons/edit.ico")
    root.resizable(False, False)

    frame = customtkinter.CTkFrame(root)

    lbl1 = customtkinter.CTkLabel(
        root, text="Bienvenue dans vos tâches", font=("Madimi One Regular", 30)
    )

    prise = customtkinter.CTkButton(
        root,
        text="Enregistrer les paiement",
        font=("Madimi One Regular", 18),
        fg_color="#FFC552",
        text_color="black",
        hover_color="#A8833A",
        height=80,
        border_width=1,
        border_color="black",
        width=300,
        corner_radius=20,
        command=enrrev,
    )
    ordr = customtkinter.CTkButton(
        root,
        text="Vérifier l'historique des \npaiements",
        font=("Madimi One Regular", 18),
        fg_color="#FFC552",
        text_color="black",
        hover_color="#A8833A",
        height=80,
        border_width=1,
        border_color="black",
        width=300,
        corner_radius=20,
        command=histrev,
    )

    lbl1.pack(pady=(40, 15))
    prise.pack(pady=(20, 0))
    ordr.pack()

    root.mainloop()
