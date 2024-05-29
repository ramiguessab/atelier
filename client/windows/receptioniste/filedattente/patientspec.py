import customtkinter
from client.window import Window


class JounreSpecifier(Window):
    def __init__(self) -> None:
        super().__init__()

    def build(self, root):
        root.title("Prise de rendez-vous")
        root.geometry("800x650")
        root.resizable(False, False)

        frame = customtkinter.CTkFrame(root)

        lbl = customtkinter.CTkLabel(
            frame,
            text="Vous trouverez ici toutes les réservations des patients pour la journée spécifiée",
        )

        modbtn = customtkinter.CTkButton(
            root,
            text="Modifier",
        )

        supbtn = customtkinter.CTkButton(
            root,
            text="Supprimer",
        )

        frame.pack(padx=10, pady=(20, 5), expand=True, fill="both")
        lbl.pack(pady=15)
        modbtn.pack(pady=(5, 10), padx=(0, 255), side="right")
        supbtn.pack(pady=(5, 10), padx=(255, 0), side="left")


# def patspec(root):

#     customtkinter.set_appearance_mode("dark")
#     customtkinter.set_default_color_theme("green")

#     root = customtkinter.CTk()

#     def ok():
#         root.destroy()

#     root.mainloop()
