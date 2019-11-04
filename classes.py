import pygame
from pygame.locals import *

chemin = "/home/arinfo/Documents/DinoGame/src"
cst_saut = 50
cst_gravite = 10

class dino (pygame.sprite.Sprite) :
	def __init__(self, image,coordonnees) :
		pygame.sprite.Sprite.__init__(self)
		self.image = image
		self.rect = Rect(coordonnees,image.get_size())
		self.vitesse_x = 0
		self.vitesse_y = 0
		
	def impulsion(self) :
		self.vitesse_y = -cst_saut
	
	def move(self,limites=None):
		if limites != None :
			if (self.rect.left+self.vitesse_x)<0 or (self.rect.right+self.vitesse_x)>limites.get_width():
				self.vitesse_x=0
			if (self.rect.bottom+self.vitesse_y)>limites.get_height() or (self.rect.top+self.vitesse_y)<0:
				self.vitesse_y=0
		self.rect.move_ip(self.vitesse_x,self.vitesse_y)
		self.vitesse_y +=cst_gravite


if __name__ == "__main__" :
	pygame.display.init()
	
	fenetre = pygame.display.set_mode((0,0))
	
	img_dino = pygame.image.load(chemin+"/animals/dinosaur/png/dinosaur-01.png").convert_alpha()
	img_dino = pygame.transform.smoothscale(img_dino,(img_dino.get_width()//4,img_dino.get_height()//4))
	img_fond = pygame.image.load(chemin+"/forest/forest_constructor_kit_READY/10_backgrounds/10_backgrounds-01.jpg").convert()
	img_fond = pygame.transform.smoothscale(img_fond,(img_fond.get_width()//4,img_fond.get_height()//4))
	Dino = pygame.sprite.RenderUpdates()
	Dino.add(dino(img_dino,(0,0)))
	
	fenetre = pygame.display.set_mode(img_fond.get_size(),RESIZABLE)
	fenetre.blit(img_fond,(0,0))
	Dino.draw(fenetre)
	
	pygame.display.flip()
	
	timer = pygame.time.Clock()
	sortir = False
	while not sortir :
		timer.tick(30)
		dy = 0
		for event in pygame.event.get() :
			if event.type ==QUIT:
				sortir = True
				break
			if event.type == KEYDOWN :
				if event.key == K_UP :
					Dino.sprites()[0].impulsion()
			
		Dino.sprites()[0].move(fenetre)
		fenetre.blit(img_fond,(0,0))
		Dino.draw(fenetre)
		fenetre.blit(img_obstacle,(100,0))
		pygame.display.flip()
	#pygame.time.wait(10000)
	pygame.display.quit()
	
	
