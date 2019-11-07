from constantes import *
from classes import *
import pygame


if __name__ == "__main__" :
	pygame.display.init()
	
	fenetre = pygame.display.set_mode((0,0))
	ecran_initial = Initial()
	#ecran_initial.draw(fenetre)
	#pygame.display.flip()
	sortir = False
	while not sortir:
		niveau = Niveau(fenetre)
		niveau.draw(fenetre)
		pygame.display.flip()
		
		pygame.time.set_timer(USEREVENT,1000)
		perdu = False
		while not perdu :
			pygame.time.Clock().tick(30)
			
			for event in pygame.event.get() :
				if event.type == QUIT:
					sortir = True
				perdu = niveau.mise_a_jour(event,fenetre)
				
			niveau.move(fenetre)
			
			niveau.draw(fenetre)
			pygame.display.flip()
			
			if niveau.collision() :
				perdu = True
				pygame.time.wait(1000)
		
		if not sortir:
			quitter = False
			ecran_initial.set_highscore(niveau.score)
			ecran_initial.draw(fenetre)
			pygame.display.flip()
		
			while not quitter :
				for event in pygame.event.get():
					if event.type == QUIT:
						sortir = True
						quitter = True
					if event.type == KEYDOWN:
						if event.key == K_RETURN:
							quitter = True
	
	#pygame.time.wait(5000)
	pygame.display.quit()
