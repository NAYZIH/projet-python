import random

def game():
    choix_possibles = ["pierre", "feuille", "ciseaux"]
    victoires = 0
    defaites = 0
    egalites = 0
    
    while True:
        joueur = input("Choisis : pierre, feuille ou ciseaux (stop pour quitter) \n ").lower().strip()
        if joueur == "stop":
            break
        if joueur not in choix_possibles:
            print("Choix invalide, réessaie. \n")
            continue
        
        ordi = random.choice(choix_possibles)
        print("L'adversaire a choisi", ordi + "\n")
        
        if joueur == ordi:
            print("Égalité ! \n")
            egalites += 1
        elif (joueur == "pierre" and ordi == "ciseaux") or (joueur == "feuille" and ordi == "pierre") or (joueur == "ciseaux" and ordi == "feuille"):
            print("Tu gagnes ! \n")
            victoires += 1
        else:
            print("Tu perds ! \n")
            defaites += 1
        print(f"Score actuel : {victoires} victoire(s), {defaites} défaite(s), {egalites} égalité(s).\n")