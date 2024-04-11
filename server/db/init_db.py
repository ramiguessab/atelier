from query import Query


with open("server/db/db.sql") as init_file:
    sql = init_file.read()
    Query(sql).commit()

print("****CREATION DE NOUVEAU GERANT****")
manager_first_name = input("Entrez le prenom de gerant: ")
manager_last_name = input("Entrez le nom de gerant: ")
manager_username = input("Entrez le nom d'utilisateur de gerant: ")
manager_password = input("Entrez le mot de pass de gerant: ")
manager_phone = input("Entrez le numero de telephone de gerant: ")

Query(
    f"""INSERT INTO gerant 
    (prenom, nom, username, password, phone) VALUES 
    ('{manager_first_name}', '{manager_last_name}', '{manager_username}', '{manager_password}', '{manager_phone}');""",
).commit()
