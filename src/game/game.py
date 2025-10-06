import random
from colorama import Fore, Style

def game():
    choix_possibles = ["pierre", "feuille", "ciseaux"]
    victoires = 0
    defaites = 0
    egalites = 0
    
    while True:
        joueur = input(Fore.CYAN + "Choisis : pierre, feuille ou ciseaux (stop pour quitter) \n" + Style.RESET_ALL).lower().strip()
        if joueur == "stop":
            break
        if joueur not in choix_possibles:
            print(Fore.CYAN + "Choix invalide, réessaie. \n" + Style.RESET_ALL)
            continue
        
        ordi = random.choice(choix_possibles)
        print(Fore.CYAN + "L'adversaire a choisi", ordi + "\n" + Style.RESET_ALL)
        
        if joueur == ordi:
            print(Fore.YELLOW + "Égalité ! \n" + Style.RESET_ALL)
            egalites += 1
        elif (joueur == "pierre" and ordi == "ciseaux") or (joueur == "feuille" and ordi == "pierre") or (joueur == "ciseaux" and ordi == "feuille"):
            print(Fore.GREEN + "Tu gagnes ! \n" + Style.RESET_ALL)
            victoires += 1
        else:
            print(Fore.RED + "Tu perds ! \n" + Style.RESET_ALL)
            defaites += 1
        print(Fore.CYAN + f"Score actuel : {victoires} victoire(s), {defaites} défaite(s), {egalites} égalité(s).\n" + Style.RESET_ALL)