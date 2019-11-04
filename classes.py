import pygame
from pygame.locals import *

chemin = "/home/arinfo/Documents/DinoGame/src"

if __name__ == "__main__" :
	pygame.display.init()
	
	img_dino = pygame.image.load(chemin+"/animals/dinosaur/png/dinosaur-01.png").alpha_convert()
	img_fond = pygame.image.load(chemin+"/forest/forest	_constructor_kit_READY/10_backgrounds/10_backgrounds-01.jpg").convert()
	
	fenetre = pygame.display.set_mode(img_fond.get_size(),RESIZABLE)
	fenetre.blit(img_fond,(0,0))
	
	pygame.display.flip()
	
	pygame.time.wait(10000)
	pygame.display.quit()
	
	
