#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

country = input ("Pays concerné ? ")
code_medals = input("Chaine représentant les médailles ? ")
G= S =B =0
for letter in code_medals:
    if letter == "G": G+=1
    if letter == "S": S+=1
    if letter == "B": B+=1

print(f"""{country}:
- {G} OR
- {S} Argent
- {B} Bronze""")