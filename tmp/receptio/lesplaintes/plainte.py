import customtkinter
from lesplaintes.redplnt import redplnt
from lesplaintes.rapport import rappo


def plaint(root):

    def redaplainte():
        redplnt(root)

    def rapp():
        rappo(root)

    root = customtkinter.CTk()

    root.title("Les Plaintes")
    root.geometry("800x350")
    ("icons/edit.ico")
    root.resizable(False, False)

    frame = customtkinter.CTkFrame(root)

    lbl1 = customtkinter.CTkLabel(
        root, text="Bienvenue dans vos tâches", font=("Madimi One Regular", 30)
    )

    gerap = customtkinter.CTkButton(
        root,
        text="Gérer les Rapport",
        font=("Madimi One Regular", 18),
        fg_color="#FFC552",
        text_color="black",
        hover_color="#A8833A",
        height=80,
        border_width=1,
        border_color="black",
        width=300,
        corner_radius=20,
        command=rapp,
    )
    ordr = customtkinter.CTkButton(
        root,
        text="Rédactoin des plaintes",
        font=("Madimi One Regular", 18),
        fg_color="#FFC552",
        text_color="black",
        hover_color="#A8833A",
        height=80,
        border_width=1,
        border_color="black",
        width=300,
        corner_radius=20,
        command=redaplainte,
    )

    lbl1.pack(pady=(40, 15))
    gerap.pack(pady=(20, 0))
    ordr.pack()

    root.mainloop()
