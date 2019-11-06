import os

local = os.getcwd()
chemin = local[:local.rindex("/")]+"/src/"

fond = "fond.jpg"
dinosaure = "dinosaure_1.png"
obstacle = "obstacle_1.png"

largeur_fenetre = 1080
hauteur_fenetre = 720

cst_saut = 100
cst_gravite = 10
dx = -10
cst_tolerance = 35
max_obstacles = 3


