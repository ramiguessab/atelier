from customtkinter import CTk, CTkToplevel
from client.dialogs.authentication_failed import AuthenticationInvalid
from socket import socket as skt
from client.window import Window
import customtkinter
from PIL import Image
from message import Message


class DesconnectPrompt(Window):
    def __init__(self) -> None:
        super().__init__("Desconnect?")

    def build(self, app: CTk | CTkToplevel):

        app.title("Déconnecter?")

        def close():
            app.destroy()

        top_frame = customtkinter.CTkFrame(master=app)

        bottom_frame = customtkinter.CTkFrame(master=app)

        image = customtkinter.CTkImage(Image.open("icons/mark.png"), size=(64, 64))

        icon = customtkinter.CTkLabel(master=top_frame, text="", image=image)
        icon.grid(row=0, column=0, padx=16)
        label = customtkinter.CTkLabel(
            master=top_frame,
            text="Êtes-vous sûr de vouloir vous déconnecter de la plateforme ?",
        )

        label.grid(row=0, column=1, pady=4, padx=8)

        cancel = customtkinter.CTkButton(master=bottom_frame, text="Non", command=close)
        cancel.grid(row=0, column=0, pady=16, padx=8)

        desconnect = customtkinter.CTkButton(
            master=bottom_frame,
            text="Oui",
            hover_color="#660000",
            command=self.deconnecter,
        )
        desconnect.grid(row=0, column=1, pady=16, padx=8)

        top_frame.pack(pady=8, padx=16)
        bottom_frame.pack(pady=8, padx=16)

    def deconnecter(self):
        Client.reset_routing()
        Client.open_new_window(AuthenticationWindow())


class AuthenticationWindow(Window):
    def __init__(self) -> None:
        super().__init__("Authenticate")

    def build(self, app):
        tmp_app = app
        tmp_app.title("Authentification")
        tmp_app.geometry("330x318")
        tmp_app.resizable(False, False)

        app = customtkinter.CTkFrame(master=tmp_app)
        app.pack(padx=8, pady=8)

        label = customtkinter.CTkLabel(master=app, text="Vous devez être authentifié")
        label.grid(row=0, pady=8, padx=8, columnspan=2)

        form = customtkinter.CTkFrame(master=app)
        form.grid(row=1, columnspan=2, pady=8, padx=8)

        poste_label = customtkinter.CTkLabel(master=form, text="Poste:")
        poste_label.grid(row=0, column=0, pady=16, padx=8)
        roles = ["Gerant", "Receptioniste", "Medecin", "Technicien"]
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
    role: None | str = None
    _history: list[Window] = []

    def __init__(self, socket: skt) -> None:
        if Client.socket == None:
            Client.socket = socket

        if Client.app == None:
            Client.app = CTk()
            Client.app.eval("tk::PlaceWindow . center")

        auth = AuthenticationWindow()

        Client.open_new_window(auth)

        Client.app.mainloop()

    @staticmethod
    def open_new_window(window: Window):

        if Client.app != None:
            for widget in Client.app.winfo_children():
                widget.destroy()
            if len(Client._history) > 1:
                title_frame = customtkinter.CTkFrame(master=Client.app)
                title_frame.pack(pady=16)
                customtkinter.CTkButton(
                    text="Retour",
                    master=title_frame,
                    command=Client.__return_last_page,
                    fg_color="green",
                    hover_color="dark green",
                ).pack(side=customtkinter.LEFT)
                customtkinter.CTkLabel(master=Client.app, text=window.title).pack(
                    anchor=customtkinter.CENTER
                )

            Client.app.resizable(True, True)
            Client._history.append(window)

            window.build(Client.app)
            Client.app.title(window.title)

    @staticmethod
    def __return_last_page():
        Client._history.pop()
        last_window = Client._history.pop()
        Client.open_new_window(last_window)

    @staticmethod
    def open_as_dialog(window: Window):
        dialog = CTkToplevel(master=Client.app)
        dialog.title(window.title)
        window.build(dialog)

    @staticmethod
    def reset_routing():
        Client._history = []

    @staticmethod
    def desconnect():

        Client.open_as_dialog(DesconnectPrompt())
