import pygame
from pygame.locals import *

chemin = "/home/arinfo/Documents/DinoGame/src"

if __name__ == "__main__" :
	pygame.display.init()
	
	fenetre = pygame.display.set_mode((0,0))
	
	img_dino = pygame.image.load(chemin+"/animals/dinosaur/png/dinosaur-01.png").convert_alpha()
	img_fond = pygame.image.load(chemin+"/forest/forest_constructor_kit_READY/10_backgrounds/10_backgrounds-01.jpg").convert()
	
	fenetre = pygame.display.set_mode((img_fond.get_width()//4,img_fond.get_height()//4),RESIZABLE)
	fenetre.blit(img_fond,(0,0))
	fenetre.blit(img_dino,(0,0))
	
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
					dy = 10
			fenetre.blit(img_fond,(0,0))
			fenetre.blit(img_dino,(0,-dy))
		pygame.display.flip()
	#pygame.time.wait(10000)
	pygame.display.quit()
	
	
