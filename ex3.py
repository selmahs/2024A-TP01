# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.
import math
speed = input("Veuillez saisir la vitesse initiale de la boule:") 
angle = input("Veuillez saisir l'angle de lancement:")
d = (pow(float(speed),2)*math.sin(2*float(angle)))/9.8
