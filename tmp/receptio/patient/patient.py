import customtkinter
from messagebox.error import error
from patient.addpatient import addpat
from patient.modifypatient import mod


def patient(root):

    def addp():
        addpat(root)

    def err():
        error("Aucun patient a été selectioné")

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")

    root = customtkinter.CTk()

    root.title("Les Patients")
    root.geometry("800x490")
    ("icons/patient.ico")
    root.resizable(False, False)

    def modify():
        mod(root)

    frame = customtkinter.CTkFrame(root)

    lbl = customtkinter.CTkLabel(
        frame,
        text="Vous trouverez ici tous les dossier patients enregistrés dans ce laboratoire",
        font=("Madimi One Regular", 21),
    )

    modbtn = customtkinter.CTkButton(
        root,
        text="Modifier",
        font=("Madimi One Regular", 18),
        command=modify,
        border_width=2,
        border_color="white",
        fg_color="#FFC552",
        hover_color="#A8833A",
        text_color="black",
    )
    ajtbtn = customtkinter.CTkButton(
        root,
        text="Ajouter",
        font=("Madimi One Regular", 18),
        command=addp,
        border_width=2,
        border_color="white",
        fg_color="#FFC552",
        hover_color="#A8833A",
        text_color="black",
    )

    frame.pack(padx=10, pady=(20, 5), expand=True, fill="both")
    lbl.pack(pady=15)
    modbtn.pack(pady=(5, 15), padx=(255, 0), side="left")
    ajtbtn.pack(pady=(5, 15), padx=(0, 255), side="right")

    root.mainloop()
