import pygame
from pygame.locals import *

chemin = "/home/arinfo/Documents/DinoGame/src"
cst_saut = 50
cst_gravite = 10

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
	
	img_obstacle = pygame.image.load(chemin+"/forest/icon-pot/png/pot-01.png").convert_alpha()
	img_obstacle = pygame.transform.smoothscale(img_obstacle,(img_obstacle.get_width()//10,img_obstacle.get_height()//10))
	LObstacle = pygame.sprite.RenderUpdates()
	LObstacle.add(Obstacle(img_obstacle,(fenetre.get_width()-img_obstacle.get_width(),fenetre.get_height()-img_obstacle.get_height())))
	
	fenetre.blit(img_fond,(0,0))
	LObstacle.draw(fenetre)
	
	pygame.display.flip()
	
	timer = pygame.time.Clock()
	sortir = False
	dx=-1
	while not sortir :
		timer.tick(30)
		for event in pygame.event.get() :
			if event.type ==QUIT:
				sortir = True
				break
		
		#LObstacle.sprites()[0].move(dx)
		for o in LObstacle.sprites() :
			o.move(dx)
			if o.is_out(fenetre):
				LObstacle.remove(o)
		fenetre.blit(img_fond,(0,0))
		LObstacle.draw(fenetre)
		pygame.display.flip()
	#pygame.time.wait(10000)
	pygame.display.quit()
	
	
