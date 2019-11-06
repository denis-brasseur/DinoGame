from constantes import *
from classes import *
import pygame


if __name__ == "__main__" :
	pygame.display.init()
	
	fenetre = pygame.display.set_mode((0,0))
	
	niveau = Niveau(fenetre)
	pygame.display.flip()
	
	pygame.time.set_timer(USEREVENT,1000)
	sortir = False
	while not sortir :
		pygame.time.Clock().tick(30)
		
		for event in pygame.event.get() :
			sortir = niveau.mise_a_jour(event,fenetre)
			
		niveau.move(fenetre)
		
		niveau.draw(fenetre)
		pygame.display.flip()
		
		if niveau.collision() :
			sortir = True
	
	pygame.time.wait(5000)
	pygame.display.quit()
