from client.windows.receptioniste.revenue.search_bilan import SearchBilan
import customtkinter
from client.ui import Client
from client.window import Window
from message import Message


class ReciptionisteHome(Window):
    def __init__(self) -> None:
        super().__init__("Reciptioniste Home")

    def build(self, root):
        self.root = root
        root.title("Accueil Receptionniste")

        root.geometry("800x350")  # 800x445 with code button
        root.resizable(False, False)
        frame = customtkinter.CTkFrame(root)

        frame.pack(
            fill=customtkinter.BOTH,
            pady=16,
            padx=16,
            ipady=8,
            ipadx=16,
            anchor="center",
        )

        binvn = customtkinter.CTkLabel(frame, text="Bienvenue")
        # DossierPatient
        dosptnbtn = customtkinter.CTkButton(
            frame,
            text="Billan",
            command=self.open_bilan,
        )
        # Patient
        ptnbtn = customtkinter.CTkButton(
            frame,
            text="Patient",
            command=self.open_patient,
        )

        # Fille D'attente
        filebtn = customtkinter.CTkButton(
            frame,
            text="File D'attente",
            command=self.open_file_attente,
        )
        # Revenus
        revbtn = customtkinter.CTkButton(
            frame,
            text="Caisse",
            command=self.open_revenus,
        )

        # Deconnecter
        disconnect_btn = customtkinter.CTkButton(
            frame,
            text="Déconnecter",
            command=self.deconnecter,
            fg_color="red",
            hover_color="dark red",
        )

        binvn.pack(pady=4, padx=16, fill="both")
        dosptnbtn.pack(pady=4, padx=16, fill="both")
        ptnbtn.pack(pady=4, padx=16, fill="both")
        filebtn.pack(pady=4, padx=16, fill="both")
        revbtn.pack(pady=4, padx=16, fill="both")
        disconnect_btn.pack(pady=4, padx=16, fill="both")

    def deconnecter(self):
        Client.desconnect()

    def open_bilan(self):
        if Client.socket:
            Message("open_receptioniste_bilan", {}, Client.socket).send()

    def open_patient(self):
        if Client.socket:
            Message("open_receptioniste_patients", {}, Client.socket).send()

    def open_file_attente(self):
        if Client.socket:
            Message("open_order_arriver", {}, Client.socket).send()

    def open_revenus(self):
        Client.open_new_window(SearchBilan())
