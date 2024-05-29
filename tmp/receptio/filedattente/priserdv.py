import customtkinter
from filedattente.patientspec import patspec
from filedattente.reserve import reserve


def priserdv(root):

    root = customtkinter.CTk()

    def affi():
        patspec(root)

    def res():
        reserve(root)

    root.title("Prise de rendez-vous")
    root.geometry("800x350")
    ("icons/edit.ico")
    root.resizable(False, False)

    frame = customtkinter.CTkFrame(root)

    lbl1 = customtkinter.CTkLabel(
        root,
        text="Les rendez-vous réservés pour la journée:",
        font=("Madimi One Regular", 21),
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

    annee = [str(x) for x in range(2024, 2025)]
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
    affich = customtkinter.CTkButton(
        root,
        text="Afficher",
        font=("Madimi One Regular", 18),
        fg_color="#FFC552",
        hover_color="#A8833A",
        border_width=2,
        border_color="white",
        text_color="black",
        command=affi,
    )

    lbl2 = customtkinter.CTkLabel(
        root,
        text="Nouvelle réservation de rendez-vous:",
        font=("Madimi One Regular", 21),
    )

    reserv = customtkinter.CTkButton(
        root,
        text="Reservation",
        font=("Madimi One Regular", 18),
        fg_color="#FFC552",
        hover_color="#A8833A",
        border_width=2,
        border_color="white",
        text_color="black",
        command=res,
    )

    lbl1.grid(row=0, column=1, padx=175, pady=(35, 10))
    jourentr.grid(row=1, column=1, padx=(0, 2))
    moisentr.grid(row=1, column=2, padx=(0, 2))
    anneentr.grid(row=1, column=3)
    affich.grid(row=2, column=1, pady=(10, 40))
    lbl2.grid(row=3, column=1, pady=(10, 10))
    reserv.grid(row=4, column=1)
    frame.grid(row=1, column=1, sticky="nsew", padx=175, pady=10)

    root.mainloop()
