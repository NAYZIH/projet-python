# Pierre-Feuille-Ciseaux (Console)

Ce projet est une implémentation du célèbre jeu **Pierre-Feuille-Ciseaux** en Python, jouable directement dans le terminal.  
Le jeu propose un menu interactif, un affichage coloré et une boucle de jeu permettant d’enchaîner les manches tout en suivant les scores en temps réel.

## Sommaire

1. [Structure du Projet](#structure-du-projet)
2. [Fonctionnalités](#fonctionnalités)
3. [Installation et Lancement](#installation-et-lancement)
4. [Fonctionnement du Jeu](#fonctionnement-du-jeu)
5. [Collaborateurs](#collaborateurs)

## Structure du Projet

L’arborescence du projet est la suivante :

<pre>
nayzih-projet-python/
├── README.md                     # Documentation du projet
├── main.py                       # Point d'entrée du programme
└── src/
    ├── clear/
    │   └── clear.py              # Contient la fonction clear() pour nettoyer le terminal
    ├── game/
    │   └── game.py               # Logique principale du jeu (Pierre-Feuille-Ciseaux)
    └── menu/
        └── menu.py               # Menu principal et affichage des règles
</pre>

## Fonctionnalités

### Menu interactif
L’utilisateur accède à un menu simple et clair lui permettant de :
- **Jouer à Pierre-Feuille-Ciseaux**
- **Afficher les règles du jeu**
- **Quitter**

### Partie de jeu
Lorsqu’une partie est lancée :
- Le joueur choisit entre *pierre*, *feuille* ou *ciseaux*.
- L’ordinateur fait un choix aléatoire.
- Le résultat (victoire, défaite ou égalité) est immédiatement affiché.
- Le score cumulé est mis à jour et visible après chaque manche.

### Règles intégrées
Une section dédiée permet d’afficher les règles directement dans le terminal :
- Pierre bat Ciseaux  
- Feuille bat Pierre  
- Ciseaux bat Feuille  
- Si les deux choix sont identiques, il y a égalité.

### Arrêt du jeu
Le joueur peut quitter la partie à tout moment en tapant **stop**.

## Installation et Lancement

### 1. Cloner le projet
<pre>
git clone https://github.com/NAYZIH/projet-python.git
cd projet-python
</pre>

### 2. Installer les dépendances
Ce projet utilise **colorama** pour l’affichage en couleur.  
Installez-le avec la commande suivante :
<pre>
pip install colorama
</pre>

### 3. Lancer le programme
<pre>
python main.py
</pre>

Le menu principal apparaîtra dans le terminal.

## Fonctionnement du Jeu

1. Le joueur lance le programme et arrive sur le menu principal.  
2. En choisissant **1**, il démarre une partie.  
3. Il saisit son choix parmi *pierre*, *feuille* ou *ciseaux*.  
4. L’ordinateur fait un choix aléatoire et le résultat est affiché.  
5. Le score est mis à jour et le joueur peut continuer ou taper *stop* pour quitter.  
6. À tout moment, il peut revenir au menu principal pour relire les règles ou quitter.

## Collaborateurs

- [Sriram MALLIPOUDY](https://github.com/NAYZIH)
- [Sami EL ABDALLAOUI](https://github.com/samsko775)
