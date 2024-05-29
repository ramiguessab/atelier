import customtkinter
from client.window import Window


class NoUserFound(Window):
    def __init__(self) -> None:
        super().__init__("No User")

    def build(self, app):
        app.title("Informations Incorrects")

        def close():
            app.destroy()

        customtkinter.CTkLabel(master=app, text="Aucun utilisateur trouvé").pack(
            padx=16, pady=8
        )
        customtkinter.CTkButton(master=app, text="OK", command=close).pack(
            fill="both", padx=16, pady=8
        )


class AuthenticationInvalid(Window):
    def __init__(self) -> None:
        super().__init__("Invalid Authentication")

    def build(self, app):
        app.title("Informations Incorrects")

        def close():
            app.destroy()

        customtkinter.CTkLabel(
            master=app, text="Vos informations ne sont pas valides"
        ).pack(padx=16, pady=8)
        customtkinter.CTkButton(master=app, text="OK", command=close).pack(
            fill="both", padx=16, pady=8
        )
