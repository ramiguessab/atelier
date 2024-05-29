from socket import socket
from server_main import EventHandler
from message import Message
from server.db.query import Query
from tkinter import messagebox


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("edit_employee")

    def handle(self, socket: socket, data):
        
        employee_id = data["id"]


        Query(
            f"UPDATE employe SET date_sortie={f"'{data["exit_date"]}'" if data["exit_date"]!="" else 'null'},salaire='{data["salery"]}' WHERE utilisateur_id={employee_id};"
        ).commit()

        Query(
            f"UPDATE utilisateur SET nom='{data["nom"]}',prenom='{data["prenom"]}',password='{data["password"]}',username='{data["username"]}',phone='{data["phone_number"]}' WHERE id={employee_id};"
        ).commit()

        Query(
            f"UPDATE specialite SET nom='{data["speciality"]}' WHERE utilisateur_id={employee_id};"
        ).commit()

        Message("edit_employee", {}, socket).send()


class InClient(EventHandler):
    def __init__(self) -> None:
        super().__init__("edit_employee")

    def handle(self, socket, data):
        messagebox.showinfo(
            title="Success",
            message="La modification a été apportée à l'employé que vous avez sélectionné",
        )
