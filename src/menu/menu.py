import sys
from src.game import game
from colorama import Fore, Style


def afficher_regles():
    print(Fore.YELLOW + "\n=== RÈGLES DU JEU ===" + Style.RESET_ALL)
    print(Fore.CYAN + "1. Tu choisis entre pierre, feuille ou ciseaux." + Style.RESET_ALL)
    print(Fore.CYAN + "2. L'ordinateur fait aussi un choix aléatoire." + Style.RESET_ALL)
    print(Fore.CYAN + "3. Les règles sont simples :" + Style.RESET_ALL)
    print(Fore.CYAN + "   - Pierre bat Ciseaux" + Style.RESET_ALL)
    print(Fore.CYAN + "   - Feuille bat Pierre" + Style.RESET_ALL)
    print(Fore.CYAN + "   - Ciseaux bat Feuille" + Style.RESET_ALL)
    print(Fore.CYAN + "4. Si les deux choix sont identiques, c'est une égalité." + Style.RESET_ALL)
    print(Fore.CYAN + "5. Tape 'stop' pendant la partie pour quitter.\n" + Style.RESET_ALL)

def menu():
    while True:
        print(Fore.YELLOW + "=== MENU PRINCIPAL ===" + Style.RESET_ALL)
        print(Fore.CYAN + "1. Jouer à Pierre-Feuille-Ciseaux" + Style.RESET_ALL)
        print(Fore.CYAN + "2. Afficher les règles du jeu" + Style.RESET_ALL)
        print(Fore.CYAN + "3. Quitter" + Style.RESET_ALL)
        
        choix = input(Fore.CYAN + "Choisis une option : " + Style.RESET_ALL).strip()

        if choix == "1":
            game.game()  
        elif choix == "2":
            afficher_regles()  
        elif choix == "3":
            print(Fore.YELLOW + "Au revoir " + Style.RESET_ALL)
            sys.exit()
        else:
            print(Fore.RED + "Choix invalide, réessaie.\n" + Style.RESET_ALL)