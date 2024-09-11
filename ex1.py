# TODO: Créer un script permettant le formattage du livre des records des JO.

country = input("De quelle nationalité est l'athlète ? ")
athlete = input("Quelle est le nom de l'athlete?")
date = input("Quelle est la date du record?")
discipline = input("Dans quelle discipline?")
categorie = input("Dans quelle categorie specifique?")
record = input("Quel est le record?")

print(f"""Nouveau record:
------------------------------
{date} - {discipline} - {categorie}:
        {athlete} ({country}) - {record}""")
#Demander la nationalité de l'athlète
#Demander le nom de l'athlète
#Demander la date du record
#Demander la discipline
#Demander la catégorie, qui peut être nulle
#Demander le record