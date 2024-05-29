from tkinter import messagebox
import customtkinter
from client.window import Window


class Comptabilite(Window):
    def __init__(self, somme) -> None:
        super().__init__("Gerant Home")
        self.somme = somme

    def build(self, app):
        app.geometry("800x300")
        frame = customtkinter.CTkFrame(master=app)

        self.revenues = customtkinter.StringVar(value=self.somme["somme"])
        self.charges = customtkinter.StringVar()
        self.total = customtkinter.StringVar()
        customtkinter.CTkLabel(master=frame, text="Revenues:").pack(padx=8, pady=8)
        customtkinter.CTkEntry(
            master=frame, state="disabled", textvariable=self.revenues
        ).pack(padx=8, pady=8)
        customtkinter.CTkLabel(master=frame, text="Charges:").pack(padx=8, pady=8)
        customtkinter.CTkEntry(master=frame, textvariable=self.charges).pack(
            padx=8, pady=8
        )
        customtkinter.CTkLabel(master=frame, text="Total:").pack(padx=8, pady=8)
        customtkinter.CTkEntry(master=frame, textvariable=self.total).pack(
            padx=8, pady=8
        )

    def calculate(self):
        charges = self.charges.get()
        if not charges:
            messagebox.showerror(message="Entrez les charges")
        else:
            self.total.set(str(float(self.revenues.get()) - float(self.charges.get())))
