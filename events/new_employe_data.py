from socket import socket
from server_main import EventHandler
from message import Message
from server.db.query import Query, Row


class InServer(EventHandler):
    def __init__(self) -> None:
        super().__init__("new_employe_data")

    def handle(self, socket: socket, data):

        nom = data["nom"]
        lastname = data["lastname"]
        role = data["role"]
        username = data["username"]
        salery = data["salery"]
        phone_number = data["phone_number"]
        birthdate = data["birthdate"]
        entrydate = data["entrydate"]
        speciality = data["speciality"]
        password = data["password"]

        Query(
            f"""INSERT INTO utilisateur 
            (nom, prenom, username, password, phone, date_naissance, poste) VALUES 
            ('{nom}','{lastname}','{username}','{password}','{phone_number}','{birthdate}','{role}');"""
        ).commit()

        new_user = Query(
            f"SELECT id FROM utilisateur WHERE username='{username}'"
        ).getAll()[0]

        if new_user != None:
            if speciality != "":
                Query(
                    f"""INSERT INTO specialite 
              (nom, utilisateur_id) VALUES 
              ('{speciality}','{new_user["id"]}');"""
                ).commit()

            Query(
                f"""INSERT INTO employe 
              (date_entree, salaire, utilisateur_id) VALUES 
              ('{entrydate}','{float(salery)}','{new_user["id"]}');"""
            ).commit()

            Message("employe_added", {}, socket=socket).send()
