import customtkinter
from customtkinter import *
from messagebox.success import succ


def redplnt(root):

    root = customtkinter.CTk()

    def eff():
        sujrapentr.delete("0", END)
        sujrapentr.insert(END, "")

        redaentr.delete("0.0", END)
        redaentr.insert(END, "")

    def env():
        eff()
        succ("La plainte a été envoyée")

    root.title("Rédaction des plaintes")
    root.geometry("800x500")
    ("icons/edit.ico")
    root.resizable(False, False)
    frame = customtkinter.CTkFrame(root)

    lbl1 = customtkinter.CTkLabel(
        root,
        text="Vous pouvez rédiger la plainte que vous souhaitez envoyer au gérant",
        font=("Madimi One Regular", 21),
    )
    sujrap = customtkinter.CTkLabel(
        frame, text="Sujet du rapport:", font=("Madimi One Regular", 18)
    )
    sujrapentr = customtkinter.CTkEntry(
        frame, font=("Madimi One Regular", 15), height=30, width=250
    )

    reda = customtkinter.CTkLabel(
        frame, text="Rédaction:", font=("Madimi One Regular", 18)
    )
    redaentr = customtkinter.CTkTextbox(
        frame, font=("Madimi One Regular", 15), width=600, height=150, border_width=1
    )

    efface = customtkinter.CTkButton(
        root,
        text="Effacer",
        font=("Madimi One Regular", 18),
        fg_color="#FFC552",
        hover_color="#A8833A",
        border_width=2,
        border_color="white",
        text_color="black",
        command=eff,
    )

    enregistre = customtkinter.CTkButton(
        root,
        text="Envoyer",
        font=("Madimi One Regular", 18),
        fg_color="#FFC552",
        hover_color="#A8833A",
        border_width=2,
        border_color="white",
        text_color="black",
        command=env,
    )

    lbl1.grid(row=0, column=0, pady=(30, 30), padx=80)
    sujrap.grid(row=0, column=0, padx=(0, 400), pady=(20, 5))
    sujrapentr.grid(row=1, column=0, padx=(0, 295), pady=(0, 20))
    reda.grid(row=2, column=0, padx=(0, 450), pady=(0, 5))
    redaentr.grid(row=3, column=0, padx=(50, 0), pady=(0, 30))
    efface.grid(row=3, column=0, padx=(0, 150), pady=30)
    enregistre.grid(row=3, column=0, padx=(150, 0), pady=30)

    frame.grid(row=2, column=0, sticky="nsew", padx=50)

    root.mainloop()
