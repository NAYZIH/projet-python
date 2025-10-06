import random

choix_possibles = ["pierre", "feuille", "ciseaux"]

while True:
    joueur = input("Choisis : pierre, feuille ou ciseaux (stop pour quitter) \n ").lower().strip()
    if joueur == "stop":
        break
    if joueur not in choix_possibles:
        print("Choix invalide, réessaie.")
        continue
        
    ordi = random.choice(choix_possibles)
    print("L'adversaire a choisi", ordi)
    
    if joueur == ordi:
        print("Égalité !")
    elif (joueur == "pierre" and ordi == "ciseaux") or (joueur == "feuille" and ordi == "pierre") or (joueur == "ciseaux" and ordi == "feuille"):
        print("Tu gagnes !")
    else:
        print("Tu perds !")