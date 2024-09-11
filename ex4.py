# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level =input("Veuillez saisir le pourcentage de batterie du bateau")
battery_level=int(battery_level)
if (battery_level >50)and(battery_level<=100):
    print (2*battery_level)
if(battery_level >25)and (battery_level<=50) :
    print (0.5*battery_level)
if(battery_level >10)and (battery_level<=25) :
    print (1*battery_level)
if(battery_level >5)and(battery_level<=10):
    print (2.5*battery_level)
if(battery_level>0) and(battery_level<=5):
    print (6*battery_level)

    