import os

local = os.getcwd()
chemin = local[:local.rindex("/")]+"/src/"

fond = "fond.jpg"
dinosaure = "dinosaure_1.png"
obstacle = "obstacle_1.png"

largeur_fenetre = 1600
hauteur_fenetre = 900

cst_saut = hauteur_fenetre//10
cst_gravite = hauteur_fenetre//100
dx = -(largeur_fenetre//100)
cst_tolerance = (largeur_fenetre//10)//3
max_obstacles = 3
taille_lettres = 50
namefont = 'ComicSansMS'
acceleration = 1
