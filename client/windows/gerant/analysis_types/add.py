from tkinter import messagebox
import customtkinter
from client.ui import Client
from client.window import Window
from message import Message


class AddAnalysis(Window):
    def __init__(self) -> None:
        super().__init__("Ajouter Analysis")

    def build(self, app):
        app.geometry("400x350")

        customtkinter.CTkLabel(
            master=app, text="Entrez les modifications que vous souhaitez"
        ).pack(padx=4, pady=8)

        body_frame = customtkinter.CTkFrame(master=app)
        body_frame.pack(padx=4, pady=8)

        self.nom = customtkinter.StringVar()
        self.abrv = customtkinter.StringVar()
        self.prix = customtkinter.StringVar()

        ####
        left_frame = customtkinter.CTkFrame(master=body_frame)
        left_frame.grid(column=0, row=0, padx=4, pady=8)

        customtkinter.CTkLabel(master=left_frame, text="Nom d'analyse:").pack(
            padx=4, pady=4
        )
        customtkinter.CTkEntry(master=left_frame, textvariable=self.nom).pack(
            padx=4, pady=4
        )
        customtkinter.CTkLabel(master=left_frame, text="Abréviation:").pack(
            padx=4, pady=4
        )
        customtkinter.CTkEntry(master=left_frame, textvariable=self.abrv).pack(
            padx=4, pady=4
        )
        customtkinter.CTkLabel(master=left_frame, text="Prix:").pack(padx=4, pady=4)
        customtkinter.CTkEntry(master=left_frame, textvariable=self.prix).pack(
            padx=4, pady=4
        )
        ####
        right_frame = customtkinter.CTkFrame(master=body_frame)
        right_frame.grid(column=1, row=0, padx=4, pady=8)

        self.description = customtkinter.CTkTextbox(master=right_frame)
        self.description.pack(padx=4, pady=4)

        customtkinter.CTkButton(
            master=app, text="Enregistrer", command=self.add_analyse
        ).pack(padx=4, pady=16)

    def add_analyse(self):
        nom = self.nom.get()
        abrv = self.abrv.get()
        prix = self.prix.get()
        description = self.description.get("1.0", customtkinter.END)
        if not nom or not abrv or not prix or not description:
            messagebox.showerror("Completer les champs")
        elif Client.socket:

            Message(
                "add_analyse",
                {"nom": nom, "arbv": abrv, "prix": prix, "description": description},
                Client.socket,
            ).send()
