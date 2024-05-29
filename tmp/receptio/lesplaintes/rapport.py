import customtkinter
from customtkinter import *
from lesplaintes.lesrapports import lesrap


def rappo(root):

    root = customtkinter.CTk()

    def eff():
        jourvisentr.set("1")
        moisvisentr.set("Janvier")
        annevisentr.set("2020")
        jourvisentr2.set("1")
        moisvisentr2.set("Janvier")
        annevisentr2.set("2020")

    def lsrapps():
        eff()
        lesrap(root)

    root.title("Rapports")
    root.geometry("800x460")
    ("icons/edit.ico")
    root.resizable(False, False)
    frame = customtkinter.CTkFrame(root)

    lbl1 = customtkinter.CTkLabel(
        root,
        text="Sélectionnez la période pendant laquelle ces rapports ont été enregistrés",
        font=("Madimi One Regular", 21),
    )

    periode = customtkinter.CTkLabel(
        root, text="Période:", font=("Madimi One Regular", 18)
    )

    du = customtkinter.CTkLabel(frame, text="Du", font=("Madimi One Regular", 18))
    au = customtkinter.CTkLabel(frame, text="Au", font=("Madimi One Regular", 18))

    jour = [str(x) for x in range(1, 32)]
    jourvisentr = customtkinter.CTkOptionMenu(
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
    moisvisentr = customtkinter.CTkOptionMenu(
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

    annee = [str(x) for x in range(2020, 2025)]
    annevisentr = customtkinter.CTkOptionMenu(
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

    jourvisentr2 = customtkinter.CTkOptionMenu(
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

    moisvisentr2 = customtkinter.CTkOptionMenu(
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

    annevisentr2 = customtkinter.CTkOptionMenu(
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
    rece = customtkinter.CTkButton(
        root,
        text="Recevoir",
        font=("Madimi One Regular", 18),
        fg_color="#FFC552",
        hover_color="#A8833A",
        border_width=2,
        border_color="white",
        text_color="black",
        command=lsrapps,
    )

    lbl1.grid(row=0, column=0, padx=50, pady=30)
    periode.grid(row=1, column=0, padx=(0, 620), pady=(20, 10))
    du.grid(row=0, column=0, pady=(30, 0), padx=(40, 0))
    jourvisentr.grid(row=1, column=0, padx=(140, 10))
    moisvisentr.grid(row=1, column=1, padx=(0, 10))
    annevisentr.grid(row=1, column=2)
    au.grid(row=2, column=0, pady=(20, 0), padx=(40, 0))
    jourvisentr2.grid(row=3, column=0, padx=(140, 10), pady=(0, 50))
    moisvisentr2.grid(row=3, column=1, padx=(0, 10), pady=(0, 50))
    annevisentr2.grid(row=3, column=2, pady=(0, 50))
    rece.grid(row=3, column=0, pady=30)

    frame.grid(row=2, column=0, sticky="nsew", padx=(30, 20))

    root.mainloop()
