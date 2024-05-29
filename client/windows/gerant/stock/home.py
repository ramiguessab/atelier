import customtkinter
from client.ui import Client
from client.window import Window
from client.windows.gerant.stock.add import AddStock
from tkinter import messagebox
from client.components.Table import CTkTable
from message import Message


class Stock(Window):
    def __init__(self, stock) -> None:
        super().__init__("Stock")
        self.stock = stock

    def build(self, app):
        app.title("Stock")
        app.geometry("800x400")
        frame = customtkinter.CTkFrame(master=app)

        customtkinter.CTkLabel(
            master=frame,
            text="Vous trouverez ici tous qui ont dans stock",
        ).pack(pady=8)

        self.stock_table = CTkTable(
            master=frame,
            columns=["Id", "Nom", "Quantite", "Prix Unitaire", "Date de peremption"],
            rows=self.stock,
        )
        self.stock_table.pack(padx=4, pady=8)

        actions_frame = customtkinter.CTkFrame(master=frame, fg_color="transparent")
        actions_frame.pack(pady=8, padx=8)

        customtkinter.CTkButton(
            master=actions_frame, text="Modifier", command=self.open_edit_stock
        ).grid(row=0, column=0, padx=8)
        customtkinter.CTkButton(
            master=actions_frame, text="Ajouter", command=self.open_add_stock
        ).grid(row=0, column=1, padx=8)
        customtkinter.CTkButton(
            master=actions_frame,
            text="Suprimer",
            fg_color="red",
            hover_color="dark red",
            command=self.delete_stock,
        ).grid(row=0, column=2, padx=8)

        frame.pack()

    def open_add_stock(self):
        Client.open_as_dialog(window=AddStock())

    def open_edit_stock(self):
        selected_stock = self.stock_table.selected_value.get()
        if not selected_stock:
            messagebox.showwarning(
                title="Selectionner stock",
                message="Il faut spécifier un stock",
            )
        else:
            if Client.socket:
                Message("open_edit_stock", {"id": selected_stock}, Client.socket).send()

    def delete_stock(self):
        selected_stock = self.stock_table.selected_value.get()
        if not selected_stock:
            messagebox.showwarning(
                title="Selectionner Stock",
                message="Il faut spécifier un stock",
            )
        else:
            if Client.socket:
                Message("delete_stock", {"id": selected_stock}, Client.socket).send()
