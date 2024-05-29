import customtkinter
from customtkinter import *
from filedattente.priserdv import priserdv
from filedattente.ordreariv import ordrarv


def filldat(root):

    def rdv():
        priserdv(root)

    def ordre():
        ordrarv(root)

    root = customtkinter.CTk()

    root.title("File d'attente")
    root.geometry("800x350")
    ("icons/edit.ico")
    root.resizable(False, False)

    frame = customtkinter.CTkFrame(root)

    lbl1 = customtkinter.CTkLabel(
        root, text="Bienvenue dans vos tâches", font=("Madimi One Regular", 30)
    )

    prise = customtkinter.CTkButton(
        root,
        text="Prise de rendez-vous",
        font=("Madimi One Regular", 18),
        fg_color="#FFC552",
        text_color="black",
        hover_color="#A8833A",
        height=80,
        border_width=1,
        border_color="black",
        width=300,
        corner_radius=20,
        command=rdv,
    )
    ordr = customtkinter.CTkButton(
        root,
        text="Met l'ordre d'arrivé des patients",
        font=("Madimi One Regular", 18),
        fg_color="#FFC552",
        text_color="black",
        hover_color="#A8833A",
        height=80,
        border_width=1,
        border_color="black",
        width=300,
        corner_radius=20,
        command=ordre,
    )

    lbl1.pack(pady=(40, 15))
    prise.pack(pady=(20, 0))
    ordr.pack()

    root.mainloop()
