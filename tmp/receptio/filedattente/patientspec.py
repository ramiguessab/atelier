import customtkinter


def patspec(root):

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")

    root = customtkinter.CTk()

    def ok():
        root.destroy()

    root.title("Prise de rendez-vous")
    root.geometry("800x650")
    ("icons/patient.ico")
    root.resizable(False, False)

    frame = customtkinter.CTkFrame(root)

    lbl = customtkinter.CTkLabel(
        frame,
        text="Vous trouverez ici toutes les réservations des patients pour la journée spécifiée",
        font=("Madimi One Regular", 21),
    )

    modbtn = customtkinter.CTkButton(
        root,
        text="Modifier",
        font=("Madimi One Regular", 18),
        border_width=2,
        border_color="white",
        fg_color="#FFC552",
        hover_color="#A8833A",
        text_color="black",
    )

    supbtn = customtkinter.CTkButton(
        root,
        text="Supprimer",
        font=("Madimi One Regular", 18),
        border_width=2,
        border_color="white",
        fg_color="#FFC552",
        hover_color="#A8833A",
        text_color="black",
    )

    frame.pack(padx=10, pady=(20, 5), expand=True, fill="both")
    lbl.pack(pady=15)
    modbtn.pack(pady=(5, 10), padx=(0, 255), side="right")
    supbtn.pack(pady=(5, 10), padx=(255, 0), side="left")

    root.mainloop()
