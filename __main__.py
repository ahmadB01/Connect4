# La fonction choice(list) du module random sert
# pour la méthode coup_aleatoire(grille, j)
from random import choice

# Cette liste permet lors de l'affichage
# de transformer les nombres dans la liste grille
# en leur icône respectif
icons = ['.', 'X', 'O']

def grille_vide():
    """
    Génère un tableau multi-dimensionnel
    qui représente le jeu du Puissance 4 puis le retourne.
    
    grille_vide() -> list
    """
    # Le tableau résultant
    output = []
    # Le tableau comporte 6 sous-tableaux représentants les lignes
    for i in range(6):
        # Chaque sous-tableau est initialement composé de 7 0
        output.append([0]*7)
    return output

def affiche(grille):
    """
    Affiche le tableau multi-dimensionnel grille entré en paramètre.
    
    affiche(grille: list) -> None  
    """
    # Inversement des lignes du tableau grille
    # pour avoir les premières cases remplies en bas
    grille = grille[::-1]
    for line in grille:
        # Sépare les colonnes avec des | (esthétique)
        print('|'.join([icons[number] for number in line]))
    # Affichage des numéros de colonnes du jeu
    for i in range(len(grille[0])):
        print(i+1, end=' ')
    print('\n')

def coup_possible(grille, col):
    """
    Retourne vrai si un coup est possible dans la colonne col
    du tableau multi-dimensionnel grille.
    Autrement dit, si la case à l'indice col de la dernière ligne
    (la ligne la plus haute du jeu) est libre, alors un coup est possible.

    coup_possible(grille: list, col: int) -> bool
    """
    return grille[-1][col] == 0

def jouer(grille, j, col):
    """
    Joue un coup à la colonne col.
    Autrement dit, la fonction change la case
    la plus basse du jeu à l'indice col,
    si la case est vide.

    jouer(grille: list, j: int, col: int) -> None
    """
    # Parcourt chaque ligne du jeu de bas en haut
    for l in range(len(grille)):            
        # pour vérifier si un coup est possible dans la colonne col
        if grille[l][col] == 0:
            grille[l][col] = j
            # Si un coup est possible, alors il est inutile
            # de continuer de vérifier les autres lignes
            break;

def horizontal(grille, j, lig, col):
    """
    Retourne vrai s'il y a une combinaison de 4 mêmes cases
    horizontalement à partir de la case à l'indice grille[lig][col].
    Autrement dit, à partir de la case à l'indice grille[lig][col],
    on décale vers la droite de 3 cases puis on rajoute le contenu
    de chaque case dans la liste combination, puis on vérifie
    si combination est égale à la case du joueur j x 4.

    horizontal(grille: list, j: int, lig: int, col: int) -> bool
    """
    combination = [grille[lig][index] for index in range(col, col+4)]
    return combination == [j]*4

def vertical(grille, j, lig, col):
    """
    Retourne vrai s'il y a une combinaison de 4 mêmes cases
    verticalement à partir de la case à l'indice grille[lig][col].
    Autrement dit, à partir de la case à l'indice grille[lig][col],
    on décale vers le haut de 3 cases puis on rajoute le contenu
    de chaque case dans la liste combination, puis on vérifie
    si combination est égale à la case du joueur j x 4.

    vertical(grille: list, j: int, lig: int, col: int) -> bool
    """
    combination = [grille[index][col] for index in range(lig, lig+4)]
    return combination == [j]*4

def diagonal(grille, j, lig, col):
    """
    Retourne vrai s'il y a une combinaison de 4 mêmes cases
    dans un premier sens de la diagonale (vers la droite) puis
    dans le deuxième sens de la diagonale (vers la gauche) à partir
    de la case à l'indice grille[lig][col].
    
    Autrement dit, dans le premier sens on décale
    d'une ligne de haut et d'une case à droite, puis on ajoute le contenu
    de chaque case dans la liste combination, puis on vérifie
    si combination est égale à la case du joueur j x 4.
    
    Dans l'autre sens (vers la gauche), on décale d'une ligne de haut
    et d'une case à gauche, puis on ajoute le contenu de chaque case dans
    la liste combination, puis on vérifie si combination
    est égale à la case du joueur j x 4.

    diagonal(grille: list, j: int, lig: int, col: int) -> bool
    """
    # Dans le premier sens (vers la droite)
    if col < 4:
        combination = [grille[lig+i][col+i] for i in range(4)]
        if combination == [j]*4:
            return True
    # S'il n'y a eu aucune combinaison dans le premier sens,
    # on vérifie dans l'autre sens (vers la gauche)
    if col > 2:
        combination = [grille[lig+i][col-i] for i in range(4)]
        if combination == [j]*4:
            return True

    # Si aucune combinaison n'a été trouvée, alors la fonction
    # retourne faux
    return False

def victoire(grille, j):
    """
    Retourne si dans tout le jeu une combinaison a été trouvée
    Parmi les fonctions horizontal, vertical et diagonal.

    On limite la vérification à certaines cases selon la direction
    étudiée.
    Par exemple, dans le cas d'une combinaison horizontale,
    l'indice col ne peut pas être supérieur à 3:

  lig = 5 .|.|.|.|.|.|. 
        4 .|.|.|.|.|.|. 
        3 .|.|.|.|.|.|. 
        2 .|.|.|.|.|.|. 
        1 .|.|.|.|.|.|. 
        0 .|.|.|.|X|X|X 
          0 1 2 3 4 5 6 = col

    Dans le cas d'une combinaison verticale,
    l'indice lig ne peut pas être supérieur à 2:

  lig = 5 X|.|.|.|.|.|. 
        4 X|.|.|.|.|.|. 
        3 X|.|.|.|.|.|. 
        2 .|.|.|.|.|.|. 
        1 .|.|.|.|.|.|. 
        0 .|.|.|.|.|.|. 
          0 1 2 3 4 5 6 = col

    Même chose pour le cas
    d'une combinaison diagonale :

  lig = 5 .|.|.|.|.|X|. 
        4 .|.|.|.|X|.|. 
        3 .|.|.|X|.|.|. 
        2 .|.|.|.|.|.|. 
        1 .|.|.|.|.|.|. 
        0 .|.|.|.|.|.|. 
          0 1 2 3 4 5 6 = col
    
    victoire(grille: list, j: int) -> bool
    """
    # Vérification pour une combinaison horizontale
    for lig in range(len(grille)):
        for col in range(4):
            if horizontal(grille, j, lig, col):
                return True

    # Vérification pour une combinaison verticale
    for lig in range(3):
        for col in range(len(grille[lig])):
            if vertical(grille, j, lig, col):
                return True
            
    # Vérification pour une combinaison diagonale
    for lig in range(3):
        for col in range(len(grille[lig])):
            if diagonal(grille, j, lig, col):
                return True

    # Si dans tout le jeu, aucune combinaison n'a été trouvée,
    # alors la fonction retourne faux
    return False

def match_nul(grille):
    """
    Vérifie s'il y a un match nul, autrement dit
    si le jeu est totalement rempli.
    Pour que la grille soit totalement remplie,
    il faut que la dernière ligne soit totalement remplie.
    On vérifie donc si une case est vide
    dans la dernière ligne du jeu, c'est-à-dire si la dernière
    ligne comporte un 0.

    match_nul(grille: list) -> bool
    """
    return 0 not in grille[-1]

def coup_aleatoire(grille, j):
    """
    Joue un coup aléatoire dans le jeu.
    Autrement dit: on détermine d'abord la liste des indices de
    colonnes disponibles, c'est-à-dire celles
    où un coup est possible, et on pioche
    aléatoirement un indice parmi la liste.

    coup_aleatoire(grille: list, j: int) -> None
    """

    # Récupère seulement les colonnes
    # où un coup est possible
    availables = [i for i in range(7) if coup_possible(grille, i)]
    # On pioche un indice aléatoirement parmi la liste
    random_col = choice(availables)
    jouer(grille, j, random_col)

def play(grille, j):
    """
    Joue un coup à la case entrée par l'utilisateur
    avec la fonction input()

    play(grille: list, j: int) -> None
    """
    col = -1
    
    # Vérifie que le nombre entré est bien compris entre 1 et 7
    while col not in list(range(7)):
        col = int(input('Colonne à jouer : '))-1
        
    # Vérifie si un coup est possible à cette case
    while not coup_possible(grille, col):
        col = int(input('Colonne à jouer : '))-1
    jouer(grille, j, col)

def choose_chip():
    """
    Permet à l'utilisateur de choisir le jeton qu'il veut.
    Il a le choix entre X ; et O.

    choose_chip() -> int
    """
    chip = 0
    # Empêche l'utilisateur de choisir un nombre qui n'existe pas
    while chip not in (1, 2):
        print('Choisissez votre jeton :')
        print('1 - X')
        print('2 - O')
        chip = int(input())
    return chip

def result(grille, current_player):
    """
    Affiche le résultat du jeu une fois qu'il est terminé.
    Soit il y a une victoire pour le joueur qui a joué en dernier,
    soit il y a match nul.

    result(grille: list, current_player: int) -> None
    """
    if match_nul(grille):
        print('Match nul ! ')
    else:
        # On inverse le jeton, car c'est le dernier joueur qui a gagné,
        # et non le joueur courant (c'est-à-dire celui qui joue le prochain tour)
        print('Le joueur {} a gagné la partie.'.format(
            icons[1 if current_player == 2 else 2]))

def player_vs_rand():
    """
    Fonction qui représente le premier mode du jeu Puissance 4.
    Comporte le programme qui permet de faire jouer
    l'utilisateur contre l'ordinateur.
    L'ordinateur joue aléatoirement.

    player_vs_rand() -> None
    """
    # On génère une grille puis on l'affiche
    # la variable grille représente le jeu
    grille = grille_vide()
    affiche(grille)

    # On laisse l'utilisateur choisir son jeton
    # grâce à la fonction choose_chip()
    player_chip = choose_chip()
    # L'ordinateur aura alors l'autre jeton
    comp_chip = 1 if player_chip == 2 else 2

    # Le joueur courant, celui qui joue le prochain tour
    current_player = 1

    # Le jeu tourne en boucle
    # tant qu'il n'y a aucune victoire des deux joueurs
    # ou un match nul
    while not victoire(grille, 1) \
            and not victoire(grille, 2) \
            and not match_nul(grille):
        print('Au tour du joueur {}:'.format(icons[current_player]))
        # Permet de faire jouer celui qui a le jeton X en premier
        # dans tous les cas
        if current_player == player_chip:
            play(grille, player_chip)
            current_player = comp_chip
        else:
            coup_aleatoire(grille, current_player)
            current_player = player_chip
        affiche(grille)

    # Affiche le résultat de la partie une fois terminée
    result(grille, current_player)

def player_vs_player():
    """
    Fonction qui représente le deuxième mode du jeu Puissance 4.
    Comporte le programme qui permet de faire jouer
    deux utilisateurs (deux joueurs humains).

    player_vs_player() -> None
    """
    # On génère une grille puis on l'affiche
    # la variable grille représente le jeu
    grille = grille_vide()
    affiche(grille)

    # Le joueur courant, celui qui joue le prochain tour
    current_player = 1

    # Le jeu tourne en boucle
    # tant qu'il n'y a aucune victoire des deux joueurs
    # ou un match nul
    while not victoire(grille, 1) \
            and not victoire(grille, 2) \
            and not match_nul(grille):
        print('Au tour du joueur {}:'.format(icons[current_player]))
        # Fait jouer le joueur courant
        play(grille, current_player)
        # Inverse la variable current_player pour faire jouer l'autre joueur
        if current_player == 1:
            current_player = 2
        else:
            current_player = 1
        affiche(grille)

    # Affiche le résultat de la partie une fois terminée
    result(grille, current_player)

def rand_vs_rand():
    """
    Fonction qui représente le troisième mode du jeu Puissance 4.
    Comporte le programme qui permet de faire jouer
    deux "ordinateurs".
    Les deux joueurs jouent aléatoirement.

    rand_vs_rand() -> None
    """
    # On génère une grille
    # la variable grille représente le jeu
    grille = grille_vide()
    # Le joueur courant, celui qui joue le prochain tour
    current_player = 1

    # Le jeu tourne en boucle
    # tant qu'il n'y a aucune victoire des deux joueurs
    # ou un match nul
    while not victoire(grille, 1) \
            and not victoire(grille, 2) \
            and not match_nul(grille):
        print('Au tour du joueur {}:'.format(icons[current_player]))
        # Fait jouer le joueur courant
        coup_aleatoire(grille, current_player)
        # Inverse la variable current_player pour faire jouer l'autre joueur
        if current_player == 1:
            current_player = 2
        else:
            current_player = 1
        affiche(grille)
        
    # Affiche le résultat de la partie une fois terminée
    result(grille, current_player)

def main_menu():
    """
    Permet à l'utilisateur de choisir le mode de jeu qu'il veut au Puissance 4.
    Il s'agit en quelque sorte du menu principal,
    car cette fonction est appelée en début de jeu.

    main_menu() -> None
    """
    print('Puissance 4\n-----------')
    mode = 0
    # Empêche l'utilisateur de choisir un mode qui n'existe pas.
    while mode not in (1, 2, 3):
        print('Choisissez un mode :')
        print('1 - Jouer contre l\'ordinateur')
        print('2 - Jouer contre un autre adversaire')
        print('3 - Laisser jouer deux joueurs aléatoirement')
        mode = int(input())
    return mode

def end_menu():
    """
    Permet à l'utilisateur de recommencer le jeu s'il le souhaite.
    Il s'agit en quelque sorte du menu de fin,
    car lorsque la partie est terminée, cette fonction est appelée.

    end_menu() -> None
    """
    choice = 0
    # Empêche l'utilisateur de choisir un nombre qui n'existe pas.
    while choice not in (1, 2):
        print('1 - Revenir au menu principal')
        print('2 - Quitter le jeu')
        choice = int(input())
    return choice

def main():
    """
    Fonction qui représente le programme principal.

    main() -> None
    """
    # Tant que l'utilisateur n'a pas choisi de quitter le jeu,
    # le jeu tourne alors en boucle
    while True:
        # On laisse l'utilisateur choisir le mode de jeu qu'il veut
        mode = main_menu()

        # On lance alors le mode de jeu demandé
        if mode == 1:
            player_vs_rand()
        elif mode == 2:
            player_vs_player()
        else:
            rand_vs_rand()

        # Lors de la fin d'une partie, on demande à l'utilisateur
        # s'il souhaite continuer
        restart = end_menu()
        # S'il ne veut pas, autrement dit si le nombre choisi
        # est le 2, alors on sort de la boucle principale.
        if restart == 2:
            break

    print('Au revoir !')

# On lance le programme principal
main()
