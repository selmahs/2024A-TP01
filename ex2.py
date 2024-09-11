# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

water_quantity =input("Quelle quantite d'eau faut-il assainir?")
water_quantity=int(water_quantity)
filtres = water_quantity/5
lampes= (water_quantity*3)/5
chlore=(water_quantity*0.5)/5

print(f"""Voici les matériaux requis pour l'assainissement de {water_quantity}L d'eau:
- {filtres} filtres
- {lampes} lampes UV
- {chlore}kg de chlore""")

