import customtkinter
from messagebox.quit import quit
from patient.patient import patient
from filedattente.file import filldat
from revenue.revenue import revenue
from lecode.code import codi
from lesplaintes.plainte import plaint
from patientpatadd.patientpatient import addpat
import tkinter as tk

root = customtkinter.CTk()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root.title("Accueil Receptionniste")
root.geometry("800x400")  # 800x445 with code button
("icons/gg.ico")
root.resizable(False, False)
frame = customtkinter.CTkFrame(root)

frame.pack(pady=10, padx=10, expand=True, fill="both")


def disconnect():
    quit(root)


def openpat():
    patient(root)


def openfil():
    filldat(root)


def openrev():
    revenue(root)


def opencode():
    codi(root)


def openplainte():
    plaint(root)


def openpatpat():
    addpat(root)


# def disable():
#   ptnbtn.configure(state="disable", fg_color="#246127")

# Bienvenue
binvn = customtkinter.CTkLabel(
    frame, text="Bienvenue", font=("Madimi One Regular", 40), text_color="white"
)
# DossierPatient
dosptnbtn = customtkinter.CTkButton(
    frame,
    text="Dossier Patient",
    font=("Madimi One Regular", 18),
    width=400,
    border_width=2,
    border_color="white",
    command=openpat,
    fg_color="#FFC552",
    hover_color="#A8833A",
    text_color="black",
)
# Patient
ptnbtn = customtkinter.CTkButton(
    frame,
    text="Patient",
    font=("Madimi One Regular", 18),
    width=400,
    border_width=2,
    border_color="white",
    command=openpatpat,
    fg_color="#FFC552",
    hover_color="#A8833A",
    text_color="black",
)

# Fille D'attente
filebtn = customtkinter.CTkButton(
    frame,
    text="File D'attente",
    font=("Madimi One Regular", 18),
    width=400,
    border_width=2,
    border_color="white",
    fg_color="#FFC552",
    hover_color="#A8833A",
    text_color="black",
    command=openfil,
)
# Revenus
revbtn = customtkinter.CTkButton(
    frame,
    text="Caisse",
    font=("Madimi One Regular", 18),
    width=400,
    border_width=2,
    border_color="white",
    fg_color="#FFC552",
    hover_color="#A8833A",
    text_color="black",
    command=openrev,
)
# Code
codbtn = customtkinter.CTkButton(
    frame,
    text="Code",
    font=("Madimi One Regular", 18),
    width=400,
    border_width=2,
    border_color="white",
    fg_color="#FFC552",
    hover_color="#A8833A",
    text_color="black",
    command=opencode,
)
# Plaintes
pltbtn = customtkinter.CTkButton(
    frame,
    text="Plaintes",
    font=("Madimi One Regular", 18),
    width=400,
    border_width=2,
    border_color="white",
    fg_color="#FFC552",
    hover_color="#A8833A",
    text_color="black",
    command=openplainte,
)

# Deconnecter
disconnect_btn = customtkinter.CTkButton(
    frame,
    text="Déconnecter",
    font=("Madimi One Regular", 18),
    width=400,
    height=50,
    command=disconnect,
    border_width=2,
    border_color="white",
    fg_color="#4D0E2E",
    hover_color="#2B081A",
    corner_radius=10,
)


binvn.pack(pady=10)
dosptnbtn.pack(pady=6)
ptnbtn.pack(pady=6)
filebtn.pack(pady=6)
revbtn.pack(pady=6)
# codbtn.pack(pady=6)
pltbtn.pack(pady=6)
disconnect_btn.pack(pady=15)

root.mainloop()
