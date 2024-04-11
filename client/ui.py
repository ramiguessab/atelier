from customtkinter import CTk, CTkToplevel
from client.dialogs.authentication_failed import AuthenticationInvalid
from socket import socket as skt
from client.window import Window
import customtkinter
from thread import Thread
from message import Message


class AuthenticationWindow(Window):
    def __init__(self) -> None:
        super().__init__()

    def build(self, app):
        app.title("Authentification")
        app.geometry("315x310")
        app.resizable(False, False)

        label = customtkinter.CTkLabel(master=app, text="Vous devez être authentifié")
        label.grid(row=0, pady=8, padx=8, columnspan=2)

        form = customtkinter.CTkFrame(master=app)
        form.grid(row=1, columnspan=2, pady=8, padx=8)

        poste_label = customtkinter.CTkLabel(master=form, text="Poste:")
        poste_label.grid(row=0, column=0, pady=16, padx=8)
        roles = ["Gerant", "Receptioniste", "Medicin", "Technicien"]
        self.poste = customtkinter.StringVar(value=roles[0])

        poste_combo = customtkinter.CTkOptionMenu(
            master=form, values=roles, variable=self.poste
        )
        poste_combo.grid(row=0, column=1, pady=16, padx=8)

        username_label = customtkinter.CTkLabel(master=form, text="Nom d'utilisateur:")
        username_label.grid(row=1, column=0, pady=16, padx=8)

        self.username = customtkinter.StringVar()
        username_input = customtkinter.CTkEntry(master=form, textvariable=self.username)
        username_input.grid(row=1, column=1, pady=16, padx=8)

        password_label = customtkinter.CTkLabel(master=form, text="Mot de pass:")
        password_label.grid(row=2, column=0, pady=16, padx=8)

        self.password = customtkinter.StringVar()
        password_input = customtkinter.CTkEntry(
            master=form, show="*", textvariable=self.password
        )
        password_input.grid(row=2, column=1, pady=16, padx=8)

        reset_form = customtkinter.CTkButton(
            master=app, text="Effacer", command=self.reset_form
        )

        reset_form.grid(row=2, column=0, pady=16, padx=8)

        connect = customtkinter.CTkButton(
            master=app, text="Se Connecter", command=self.handle_connection
        )

        connect.grid(row=2, column=1, pady=16, padx=8)

    def handle_connection(self):
        if Client.socket != None:
            password = self.password.get()
            poste = self.poste.get()
            username = self.username.get()
            if password == "" or username == "":
                Client.open_as_dialog(AuthenticationInvalid())
            else:
                Message(
                    "authentication_data",
                    {
                        "password": password,
                        "poste": poste,
                        "username": username,
                    },
                    Client.socket,
                ).send()

    def reset_form(self):
        self.password.set("")
        self.poste.set("Gerant")
        self.username.set("")


class Client:
    app: None | CTk = None
    socket: None | skt = None

    def __init__(self, socket: skt) -> None:
        if Client.socket == None:
            Client.socket = socket

        if Client.app == None:
            Client.app = CTk()
            Client.app.eval("tk::PlaceWindow . center")

        auth = AuthenticationWindow()

        self.open_new_window(auth)

        Client.app.mainloop()

    @staticmethod
    def open_new_window(window: Window):
        if Client.app != None:
            for widget in Client.app.winfo_children():
                widget.destroy()

            Client.app.resizable(True, True)

            window.build(Client.app)

    @staticmethod
    def open_as_dialog(window: Window):
        dialog = CTkToplevel(master=Client.app)
        # dialog.wm_e

        window.build(dialog)
