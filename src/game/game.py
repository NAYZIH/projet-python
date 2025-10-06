import random

choix_possibles = ["pierre", "feuille", "ciseaux"]

joueur = input("Choisis : pierre, feuille ou ciseaux \n ").lower()
ordi = random.choice(choix_possibles)
print("L'adversaire a choisi", ordi)

if joueur == ordi:
    print("Égalité !")
elif (joueur == "pierre" and ordi == "ciseaux") or (joueur == "feuille" and ordi == "pierre") or (joueur == "ciseaux" and ordi == "feuille"):
    print("Tu gagnes !")
else:
    print("Tu perds !")