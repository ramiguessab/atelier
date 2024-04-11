from client.ui import AuthenticationWindow
from customtkinter import CTk, CTkToplevel, CTkButton, CTkLabel, CTkFrame, CTkImage
from client.window import Window
from client.ui import Client
from PIL import Image


class DesconnectPrompt(Window):
    def __init__(self) -> None:
        super().__init__()

    def build(self, app: CTk | CTkToplevel):

        app.title("Déconnecter?")

        def close():
            app.destroy()

        top_frame = CTkFrame(master=app)

        bottom_frame = CTkFrame(master=app)

        image = CTkImage(Image.open("icons/mark.png"), size=(64, 64))

        icon = CTkLabel(master=top_frame, text="", image=image)
        icon.grid(row=0, column=0, padx=16)
        label = CTkLabel(
            master=top_frame,
            text="Êtes-vous sûr de vouloir vous déconnecter de la plateforme ?",
        )

        label.grid(row=0, column=1, pady=4, padx=8)

        cancel = CTkButton(master=bottom_frame, text="Non", command=close)
        cancel.grid(row=0, column=0, pady=16, padx=8)

        desconnect = CTkButton(
            master=bottom_frame,
            text="Oui",
            hover_color="#660000",
            command=self.deconnecter,
        )
        desconnect.grid(row=0, column=1, pady=16, padx=8)

        top_frame.pack(pady=8, padx=16)
        bottom_frame.pack(pady=8, padx=16)

    def deconnecter(self):
        Client.open_new_window(AuthenticationWindow())
