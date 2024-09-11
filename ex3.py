# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.
import math

speed = input("Veuillez saisir la vitesse initiale de la boule:") 
angle = input("Veuillez saisir l'angle de lancement:")
speed= float(speed)
angle = float(angle)
d = pow(speed,2)*math.sin(math.radians (2*angle))/9.8
d= round(d,2)
print(f"Distance parcourue:{d}m")

