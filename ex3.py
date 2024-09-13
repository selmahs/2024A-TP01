# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.

speed = input("Vitesse initiale (m/s): ") 
angle = input("Angle de lancer (en degrés): ")

import math

speed= float(speed)
angle = float(angle)

distance= pow (speed,2) * math.sin ( math.radians (2*angle)) / 9.8
distance= round(distance,2)
print(f"Distance parcourue: {distance}m")

