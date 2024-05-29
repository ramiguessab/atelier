import customtkinter
from client.ui import Client
from client.window import Window
from client.windows.receptioniste.filedattente.reserve import Reservation


class PriseRendezVous(Window):
    def __init__(self) -> None:
        super().__init__("Prise De Rendez-Vous")

    def build(self, root):
        root.title("Prise de rendez-vous")
        root.geometry("800x350")
        root.resizable(False, False)

        root = customtkinter.CTkFrame(master=root)

        root.pack()

        lbl2 = customtkinter.CTkLabel(
            root,
            text="Nouvelle réservation de rendez-vous:",
        )

        reserv = customtkinter.CTkButton(
            root,
            text="Reservation",
            command=self.open_add_reservation,
        )

        lbl2.grid(row=3, column=1, pady=(10, 10))
        reserv.grid(row=4, column=1)

    def open_add_reservation(self):
        Client.open_new_window(Reservation())


# def patspec(root):

#     customtkinter.set_appearance_mode("dark")
#     customtkinter.set_default_color_theme("green")

#     root = customtkinter.CTk()

#     def ok():
#         root.destroy()

#     root.mainloop()


# def priserdv(root):

#     root = customtkinter.CTk()

#     def affi():
#         patspec(root)

#     def res():
#         reserve(root)

#     root.mainloop()
