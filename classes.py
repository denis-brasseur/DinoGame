import pygame
from pygame.locals import *
from constantes import *
#chemin = "/home/arinfo/Documents/DinoGame/src"
#cst_saut = 50
#cst_gravite = 10

class dino (pygame.sprite.Sprite) :
	def __init__(self, image,coordonnees) :
		pygame.sprite.Sprite.__init__(self)
		self.image = image
		self.rect = Rect(coordonnees,(image.get_width()-35,image.get_height()))
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

class Obstacle (pygame.sprite.Sprite) :
	def __init__(self, image,coordonnees) :
		pygame.sprite.Sprite.__init__(self)
		self.image = image
		self.rect = Rect(coordonnees,image.get_size())		
	
	def move(self,x=0):
		self.rect.move_ip(x,0)
		
	def is_out(self,limites):
		x,y = self.rect.center
		if x<0 or x>limites.get_width():
			return True
		if y<0 or y>limites.get_height():
			return True
		return False


if __name__ == "__main__" :
	pygame.display.init()
	
	fenetre = pygame.display.set_mode((0,0))
	
	img_fond = pygame.image.load(chemin+"/forest/forest_constructor_kit_READY/10_backgrounds/10_backgrounds-01.jpg").convert()
	img_fond = pygame.transform.smoothscale(img_fond,(img_fond.get_width()//4,img_fond.get_height()//4))
	fenetre = pygame.display.set_mode(img_fond.get_size(),RESIZABLE)
	
	img_obstacle = pygame.image.load(chemin+"/obstacle_1.png").convert_alpha()
	img_obstacle = pygame.transform.smoothscale(img_obstacle,(img_obstacle.get_width()//10,img_obstacle.get_height()//10))
	LObstacle = pygame.sprite.RenderUpdates()
	LObstacle.add(Obstacle(img_obstacle,(fenetre.get_width()-img_obstacle.get_width(),fenetre.get_height()-img_obstacle.get_height())))
	
	img_dino = pygame.image.load(chemin+"/dinosaure_1.png").convert_alpha()
	img_dino = pygame.transform.smoothscale(img_dino,(img_dino.get_width()//4,img_dino.get_height()//4))
	Dino  = pygame.sprite.RenderUpdates(dino(img_dino,(img_dino.get_width(),img_fond.get_height()-img_dino.get_height())))
	
	fenetre.blit(img_fond,(0,0))
	LObstacle.draw(fenetre)
	Dino.draw(fenetre)
	
	pygame.display.flip()
	
	timer = pygame.time.Clock()
	sortir = False
	#dx=-1
	while not sortir :
		timer.tick(30)
		for event in pygame.event.get() :
			if event.type ==QUIT:
				sortir = True
				break
			if event.type == KEYDOWN:
				if event.key == K_UP:
					Dino.sprites()[0].impulsion(fenetre)
		
		Dino.sprites()[0].move(fenetre)
		for o in LObstacle.sprites() :
			o.move(dx)
			if o.is_out(fenetre):
				LObstacle.remove(o)
		if len(pygame.sprite.spritecollide(Dino.sprites()[0],LObstacle,False))>0:
			pygame.time.wait(10000)
			sortir = True
		fenetre.blit(img_fond,(0,0))
		LObstacle.draw(fenetre)
		Dino.draw(fenetre)
		pygame.display.flip()
	#pygame.time.wait(10000)
	pygame.display.quit()
	
	
