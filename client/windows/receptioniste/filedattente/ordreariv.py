from tkinter import messagebox
import customtkinter
from client.window import Window


class OrderArriver(Window):
    def __init__(self, analyses) -> None:
        super().__init__("Order De Rendez-Vous")
        self.analyses = analyses

    def build(self, root):
        root.title("Ordre d'arrivé des patients")
        root.geometry("400x400")
        root.resizable(False, False)

        root = customtkinter.CTkFrame(master=root)
        root.pack()

        frame = customtkinter.CTkFrame(root)
        frame2 = customtkinter.CTkFrame(root)
        lbl1 = customtkinter.CTkLabel(
            root, text="Remplissez ces informations \npour générer un ticket"
        )
        lbl2 = customtkinter.CTkLabel(root, text="Contrôle de l'affichage")

        nomana = customtkinter.CTkLabel(frame, text="Nom d'analyse:")
        analyse = self.analyses
        anaentr = customtkinter.CTkOptionMenu(
            frame,
            values=analyse,
        )

        self.num_new_order = customtkinter.StringVar()
        numordr = customtkinter.CTkLabel(frame, text="Numéro d'ordre:")
        numordrentr = customtkinter.CTkEntry(frame, textvariable=self.num_new_order)

        nomana2 = customtkinter.CTkLabel(frame2, text="Nom d'analyse:")
        anaentr2 = customtkinter.CTkOptionMenu(
            frame2,
            values=analyse,
        )
        self.num_a_actualiser = customtkinter.StringVar()
        ordrpat = customtkinter.CTkLabel(frame2, text="Order de Patient Current")
        ordrpatentr = customtkinter.CTkEntry(frame2, textvariable=self.num_a_actualiser)

        generer = customtkinter.CTkButton(
            root,
            text="Générer le ticket",
            command=self.imprimer,
        )

        actualiser = customtkinter.CTkButton(
            root, text="Actualiser", command=self.actualiser
        )

        lbl1.grid(row=0, column=0, padx=8, pady=8)
        lbl2.grid(row=0, column=1, padx=8, pady=8)

        nomana.pack(padx=8, pady=8)
        anaentr.pack(padx=8, pady=8)
        numordr.pack(padx=8, pady=8)
        numordrentr.pack(padx=8, pady=8)

        nomana2.pack(padx=8, pady=8)
        anaentr2.pack(padx=8, pady=8)
        ordrpat.pack(padx=8, pady=8)
        ordrpatentr.pack(padx=8, pady=8)

        generer.grid(column=0, row=2, padx=8, pady=8)
        actualiser.grid(column=1, row=2, padx=8, pady=8)

        frame.grid(row=1, column=0, sticky="nsew", padx=8, pady=8)
        frame2.grid(row=1, column=1, sticky="nsew", padx=8, pady=8)

    def imprimer(self):
        if not self.num_new_order.get():
            messagebox.showerror(message="Specifier le nouveaux numero de ticket")
        else:
            messagebox.showinfo(message="Impression de tickets en cours")

    def actualiser(self):
        if not self.num_a_actualiser.get():
            messagebox.showerror(message="Specifier le nouveaux numero d'afichage")
        else:
            messagebox.showinfo(message="L'affichage est actualise")
