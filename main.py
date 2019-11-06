from constantes import *
from classes import *
import pygame


if __name__ == "__main__" :
	pygame.display.init()
	
	fenetre = pygame.display.set_mode((0,0))
	
	niveau = Niveau(fenetre)
	
	pygame.display.flip()
	pygame.time.wait(5000)
	pygame.display.quit()
