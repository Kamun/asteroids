# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

gameclock = pygame.time.Clock()
dt = 0

def main():
	pygame.init() 	# initialize pygame libs
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	player = Player(x, y)
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: # if user clicks 'x' while game is running, game will close
				pygame.quit()
				return
		screen.fill((0,0,0)) # Fill screen with black
		player.draw(screen)
		dt = gameclock.tick(60) / 1000
		player.update(dt)
		pygame.display.flip() # Refresh screen
		
		

if __name__ == "__main__":
	main()
