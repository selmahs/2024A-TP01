# TODO: Créer un script permettant le formattage du livre des records des JO.

country = input("De quelle nationalité est l'athlète ? ")
athlete = input("Quelle est le nom de l'athlete?")
date = input("Quelle est la date du record?")
discipline = input("Dans quelle discipline?")
categorie = input("Dans quelle categorie specifique?")
record = input("Quel est le record?")

print(f"""Nouveau records:
------------------------------
{date} - {discipline} - {categorie}:
        {athlete} ({country}) - {record}""")
