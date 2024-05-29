import customtkinter
from client.ui import Client
from client.window import Window
from client.windows.gerant.analysis_types.add import AddAnalysis
from client.components.Table import CTkTable
from message import Message
from tkinter import messagebox


class AnalysisType(Window):
    def __init__(self, analyses) -> None:
        super().__init__("Types D'Analyse")
        self.analyses = analyses

    def build(self, app):
        app.geometry("800x450")
        app.title("Types d'analyses")

        # description_frame = customtkinter.CTkFrame(app)
        # description_frame.pack()
        # customtkinter.CTkLabel(master=description_frame, text="Description").pack()
        # customtkinter.CTkTextbox(master=description_frame).pack()

        # price_frame = customtkinter.CTkFrame(app)
        # price_frame.pack()
        # customtkinter.CTkLabel(master=price_frame, text="Price").grid(column=0, row=0)
        # customtkinter.CTkEntry(master=price_frame).grid(column=1, row=0)

        self.analysis_table = CTkTable(
            master=app,
            columns=["Id", "Nom", "Abreviation", "Description", "Prix"],
            rows=self.analyses,
        )
        self.analysis_table.pack(padx=4, pady=16)

        cudActions = customtkinter.CTkFrame(master=app)
        cudActions.pack(padx=4, pady=16)
        customtkinter.CTkButton(
            master=cudActions, text="Ajouter", command=self.open_add_analyse
        ).grid(row=0, column=1, padx=16, pady=8)
        customtkinter.CTkButton(
            master=cudActions, text="Modifier", command=self.open_edit_analyse
        ).grid(row=0, column=2, padx=16, pady=8)
        customtkinter.CTkButton(
            master=cudActions,
            text="Supprimer",
            command=self.delete_analyse,
            fg_color="red",
            hover_color="dark red",
        ).grid(row=0, column=3, padx=16, pady=8)

    def open_add_analyse(self):
        Client.open_as_dialog(AddAnalysis())

    def open_edit_analyse(self):
        selected_analyse = self.analysis_table.selected_value.get()
        if selected_analyse:
            if Client.socket:
                Message(
                    "open_edit_analyse",
                    {"id": selected_analyse},
                    Client.socket,
                ).send()
        else:
            messagebox.showwarning(
                title="Selectionner Analyse",
                message="Il faut spécifier un Analyse",
            )

    def delete_analyse(self):
        selected_analyse = self.analysis_table.selected_value.get()
        if selected_analyse:
            if Client.socket:
                Message(
                    "delete_analyse",
                    {"id": selected_analyse},
                    Client.socket,
                ).send()
        else:
            messagebox.showwarning(
                title="Selectionner Analyse",
                message="Il faut spécifier un Analyse",
            )
