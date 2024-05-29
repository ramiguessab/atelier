import customtkinter
from customtkinter import *
from messagebox.error import error
from lesplaintes.lerapport import lerap


def lesrap(root):
    root = customtkinter.CTk()

    def err():
        error("Il faut spécifier un seul rapport")

    def rap():
        lerap(root)

    root.title("Les Rapports")
    root.geometry("800x465")
    ("icons/edit.ico")
    root.resizable(False, False)
    frame = customtkinter.CTkFrame(root, height=280)

    lbl1 = customtkinter.CTkLabel(
        root,
        text="Les rapports qui ont été envoyés pendant la période que vous avez spécifiée",
        font=("Madimi One Regular", 21),
    )
    affi = customtkinter.CTkButton(
        root,
        text="Afficher",
        font=("Madimi One Regular", 18),
        fg_color="#FFC552",
        hover_color="#A8833A",
        border_width=2,
        border_color="white",
        text_color="black",
        command=err,
    )

    lbl1.grid(row=0, column=0, padx=50, pady=30)
    affi.grid(row=2, column=0, pady=30)
    frame.grid(row=1, column=0, sticky="nsew", padx=(30, 40))

    root.mainloop()
