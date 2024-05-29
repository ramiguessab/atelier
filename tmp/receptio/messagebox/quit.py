from customtkinter import CTk
from tkinter import messagebox

def quit(root):
    status = messagebox.askyesno(title="Déconnecter", message="Êtes-vous sûr de vouloir vous déconnecter de la plateforme ?")
    if status:
        root.destroy()