import sys
from src.game import game

def afficher_regles():
    print("\n=== RÈGLES DU JEU ===")
    print("1. Tu choisis entre pierre, feuille ou ciseaux.")
    print("2. L'ordinateur fait aussi un choix aléatoire.")
    print("3. Les règles sont simples :")
    print("   - Pierre bat Ciseaux")
    print("   - Feuille bat Pierre")
    print("   - Ciseaux bat Feuille")
    print("4. Si les deux choix sont identiques, c'est une égalité.")
    print("5. Tape 'stop' pendant la partie pour quitter.\n")

def menu():
    while True:
        print("=== MENU PRINCIPAL ===")
        print("1. Jouer à Pierre-Feuille-Ciseaux")
        print("2. Afficher les règles du jeu")
        print("3. Quitter")
        
        choix = input("Choisis une option : ").strip()

        if choix == "1":
            game.game()  
        elif choix == "2":
            afficher_regles()  
        elif choix == "3":
            print("Au revoir ")
            sys.exit()
        else:
            print("Choix invalide, réessaie.\n")
