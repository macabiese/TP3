# TP3 combat de monstr
# Emile Macabies 401
# 2022

from random import *

# Définition des variables
hp_joueur = 20
nb_combat = 0
nb_victoire = 0
nb_defaite = 0
victoire_desuite = 0
jouer = True
# Variables speciales
force_monstre = randint(2, 11)
lance_des = randint(2, 12)


# Fonction du menu
def menu():
    global choix_joueur
    choix_joueur = int(input(
        "Que voulez-vous faire? \n 1- Combattre cet adversaire\n 2- Contourner cet adversaire pour aller ouvrir une autre porte\n 3- Afficher les règles du jeu\n 4- Quitter la partie"))


# Fonction pour contourner l'adversaire
def fuite():
    if choix_joueur == 2:
        print("Vous avez choisi de contourner cet adversaire \n Votre vie est réduite de 1")


# Fonction ou on affiche les règlement
def regle():
    print(
        "Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire. \n Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire. \n Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire. \n Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire. \n La partie se termine lorsque les points de vie de l’usager tombent sous 0. \n L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")


# Fonction de quitter le jeu
def quitter():
    print("Merci et au revoir...")
    global jouer
    jouer = False


# Fonction après 3 victoires (boss)
def megaboss():
    global force_monstre
    force_monstre = 11
    combat()


# Fonction quand le jouer meurt
def fin_partie():
    print("La partie est terminé. \n Vous avez vaincu", nb_victoire, "monstres")


# Fonction pour combattre un monstre
def combat():
    global nb_combat
    global hp_joueur
    global nb_victoire
    global nb_defaite
    global victoire_desuite
    nb_combat = nb_combat + 1
    print("Vous avez choisi de combattre cet adversaire")
    print(" Adversaire :", nb_combat, "\n Force de l’adversaire :", force_monstre, "\n Niveau de vie de l’usager :",
          hp_joueur, "\n Combat", nb_combat, ":", nb_victoire, "victoire et", nb_defaite, "défaite")
    print("Lancer du dé:", lance_des)

    # Victoire
    if lance_des >= force_monstre:
        print("Vous avez gagné! Votre vie augmente de", force_monstre)
        hp_joueur = hp_joueur + force_monstre
        nb_victoire = nb_victoire + 1
        victoire_desuite = victoire_desuite + 1

    # Défaite
    elif lance_des <= force_monstre:
        print("Vous avez perdu... Votre vie est réduite de", force_monstre)
        hp_joueur = hp_joueur - force_monstre
        nb_defaite = nb_defaite + 1
        victoire_desuite = 0

    # Status
    print("Niveau de vie :", hp_joueur, "\n Nombre de victoires consécutives :", victoire_desuite)


# Boucle ou le jeu se repete
while jouer == True:
    force_monstre = randint(2, 11)
    print("Vous tombez face à face avec un adversaire de difficulté :", force_monstre)
    menu()
    if choix_joueur == 1:
        combat()

    elif choix_joueur == 2:
        fuite()

    elif choix_joueur == 3:
        regle()

    elif choix_joueur == 4:
        quitter()

    elif nb_victoire == 3:
        megaboss()

    elif hp_joueur <= 0:
        fin_partie()