#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

country = input("Pays concerne ?")
code_medals = input("Chaine representant les medailles ?")
G=0
S=0
B=0

for letter in code_medals:
    if letter == "G": G+=1
    if letter == "S": S+=1
    if letter == "B": B+=1

print(f"""{country}:
- {G} Or
- {S} Argent 
- {B} Bronze""")