# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
	pygame.init() 	# initialize pygame libs
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: # if user clicks 'x' while game is running, game will close
				return
		screen.fill((0,0,0)) # Fill screen with black
		pygame.display.flip() # Refresh screen

if __name__ == "__main__":
	main()
