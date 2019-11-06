from random import randrange
import pygame
from pygame.locals import *
from constantes import *


class Dino (pygame.sprite.Sprite) :
	def __init__(self,coordonnees) :
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(chemin+dinosaure).convert_alpha()
		self.image = pygame.transform.smoothscale(self.image,(largeur_fenetre//10,hauteur_fenetre//10))
		x,y = coordonnees
		self.rect = Rect((x,y-self.image.get_height()),(self.image.get_width()-2*cst_tolerance,self.image.get_height()))
		self.vitesse_y = 0
		
	def impulsion(self,limites=None) :
		if limites != None :
			if self.rect.bottom == limites.get_height():
				self.vitesse_y = -cst_saut
		else:
			self.vitesse_y = -cst_saut
	
	def move(self,limites=None):
		if limites != None :
			if (self.rect.bottom+self.vitesse_y)>limites.get_height() or (self.rect.top+self.vitesse_y)<0:
				self.vitesse_y=0
		self.rect.move_ip(0,self.vitesse_y)
		if limites != None:
			if self.rect.bottom < limites.get_height():
				self.vitesse_y +=cst_gravite
		else:
			self.vitesse_y +=cst_gravite
			
	def draw(self,conteneur):
			conteneur.blit(self.image,(self.rect.left-cst_tolerance,self.rect.top))

class Obstacle (pygame.sprite.Sprite) :
	def __init__(self) :
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(chemin+obstacle).convert_alpha()
		self.image = pygame.transform.smoothscale(self.image,(largeur_fenetre//15,hauteur_fenetre//15))
		self.rect = Rect((largeur_fenetre,hauteur_fenetre-self.image.get_height()),self.image.get_size())		
	
	def move(self,x=0):
		self.rect.move_ip(x,0)
		
	def is_out(self,limites):
		if self.rect.right<0 or self.rect.left>limites.get_width():
			return True
		if self.rect.bottom<0 or self.rect.top>limites.get_height():
			return True
		return False

class Niveau :
	def __init__(self,fenetre):
		## charger et  reduire l'image de fond
		self.fond = pygame.image.load(chemin+fond).convert()
		self.fond = pygame.transform.smoothscale(self.fond,(largeur_fenetre,hauteur_fenetre))
		## construire le dinosaure
		self.dinosaure = Dino((largeur_fenetre//3,hauteur_fenetre))
		## construire les obstacles
		self.lobstacles = pygame.sprite.RenderUpdates()
		## construire le score
		self.score = 0
		## recreer la fenetre
		fenetre = pygame.display.set_mode((largeur_fenetre,hauteur_fenetre),RESIZABLE)
		## construire une Font pour afficher le score
		pygame.font.init()
		self.font = pygame.font.Font(pygame.font.match_font(namefont),taille_lettres)
		
	def mise_a_jour(self,event,fenetre):
		collision = False
		if event.type == QUIT:
			return True
		elif event.type == USEREVENT :
			if randrange(2) ==0 and len(self.lobstacles.sprites()) < max_obstacles:
				self.lobstacles.add(Obstacle())
		elif event.type == KEYDOWN :
			if event.key == K_UP :
				self.dinosaure.impulsion()
		return False
	
	def draw(self,conteneur):
		conteneur.blit(self.fond,(0,0))
		self.dinosaure.draw(conteneur)
		self.lobstacles.draw(conteneur)
		conteneur.blit(self.font.render(str(self.score),True,(0,0,0)),(5,5))
		
	def move(self,fenetre):
		global dx
		self.score -= dx//10
		self.dinosaure.move(fenetre)
		for o in self.lobstacles.sprites() :
			o.move(dx)
			if o.is_out(fenetre) :
				self.lobstacles.remove(o)
		if self.score%100 == 0:
				dx -= acceleration
	
	def collision(self):
		if len(pygame.sprite.spritecollide(self.dinosaure,self.lobstacles,False))>0:
			return True
		else: 
			return False
		


if __name__ == "__main__" :
	print("hello")
	pygame.display.init()
	pygame.font.init()
	
	fenetre = pygame.display.set_mode((0,0))
	
	img_fond = pygame.image.load(chemin+"/forest/forest_constructor_kit_READY/10_backgrounds/10_backgrounds-01.jpg").convert()
	img_fond = pygame.transform.smoothscale(img_fond,(img_fond.get_width()//4,img_fond.get_height()//4))
	fenetre = pygame.display.set_mode(img_fond.get_size(),RESIZABLE)
	fond = pygame.Surface(img_fond.get_size())
	fond.fill((255,255,255))
	
	img_obstacle = pygame.image.load(chemin+"/obstacle_1.png").convert_alpha()
	img_obstacle = pygame.transform.smoothscale(img_obstacle,(img_obstacle.get_width()//10,img_obstacle.get_height()//10))
	lObstacle = pygame.sprite.RenderUpdates()
	#lObstacle.add(Obstacle(img_obstacle,(fenetre.get_width()-img_obstacle.get_width(),fenetre.get_height()-img_obstacle.get_height())))
	
	img_dino = pygame.image.load(chemin+"/dinosaure_1.png").convert_alpha()
	img_dino = pygame.transform.smoothscale(img_dino,(img_dino.get_width()//4,img_dino.get_height()//4))
	perso = Dino(img_dino,(img_fond.get_width()//3,img_fond.get_height()-img_dino.get_height()))
	
	img_rocher = pygame.image.load(chemin+"/rocher_1.png").convert_alpha()
	img_rocher = pygame.transform.smoothscale(img_rocher,(img_rocher.get_width()//10,img_rocher.get_height()//10))
	rocher = Obstacle(img_rocher,(fenetre.get_width()-img_rocher.get_width(),fenetre.get_height()-img_rocher.get_height()))
	
	img_arbre = pygame.image.load(chemin+"/arbre_1.png").convert_alpha()
	img_arbre = pygame.transform.smoothscale(img_arbre,(int(img_arbre.get_width()/1.5),int(img_arbre.get_height()/1.5)))
	arbre = Obstacle(img_arbre,(fenetre.get_width(),fenetre.get_height()-img_arbre.get_height()-10))
	
	#fenetre.blit(img_fond,(0,0))
	fenetre.blit(fond,(0,0))
	fenetre.blit(arbre.image,(arbre.rect.x,arbre.rect.y))
	lObstacle.draw(fenetre)
	perso.draw(fenetre)
	score = 0
	namefont = pygame.font.match_font('ComicSansMS')
	font = pygame.font.Font(namefont,50)
	text_score = font.render(str(score),True,(0,0,0))
	fenetre.blit(text_score,(5,fenetre.get_width()-text_score.get_width()-5))
	fenetre.blit(rocher.image,(rocher.rect.x,rocher.rect.y))
	pygame.display.flip()
	
	
	
	timer = pygame.time.Clock()
	sortir = False
	pygame.time.set_timer(USEREVENT,1000)
	while not sortir :
		collision = False
		timer.tick(30)
		## attendre un evenement
		for event in pygame.event.get() :
			if event.type ==QUIT:
				sortir = True
				break
			if event.type == KEYDOWN:
				if event.key == K_UP:
					perso.impulsion(fenetre)
			if event.type == USEREVENT:
				if randrange(2)==0 and len(lObstacle.sprites())<2:
					lObstacle.add(Obstacle(img_obstacle,(fenetre.get_width()-img_obstacle.get_width(),fenetre.get_height()-img_obstacle.get_height())))
		## bouger les sprites
		perso.move(fenetre)
		for o in lObstacle.sprites() :
			o.move(dx)
			if o.is_out(fenetre):
				lObstacle.remove(o)
				score +=1
				if float(score//10) == score/10 : 
					dx -= 10
		## tester l'existence d'une collision
		if len(pygame.sprite.spritecollide(perso,lObstacle,False))>0:
			collision = True
		## dessiner les objets
		rocher.move(1.1*dx)
		arbre.move(0.9*dx)
		#fenetre.blit(img_fond,(0,0))
		fenetre.blit(fond,(0,0))
		fenetre.blit(arbre.image,(arbre.rect.x,arbre.rect.y))
		lObstacle.draw(fenetre)
		perso.draw(fenetre)
		text_score = font.render(str(score),False,(0,0,0))
		fenetre.blit(text_score,(5,5))
		fenetre.blit(rocher.image,(rocher.rect.x,rocher.rect.y))
		if rocher.is_out(fenetre):
			rocher.rect.x = fenetre.get_width()-rocher.image.get_width()
		if arbre.is_out(fenetre):
			arbre.rect.x = fenetre.get_width()
			arbre.rect.x = fenetre.get_width()
		pygame.display.flip()
		## si collision, freeze et quitte
		if collision :
			sortir = True
			pygame.time.wait(5000)
	
	#pygame.time.wait(10000)
	pygame.display.quit()
	
	
