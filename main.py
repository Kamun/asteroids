# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroidfield import *


gameclock = pygame.time.Clock()
dt = 0

def main():
	pygame.init() 	# initialize pygame libs
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	# create groups
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (updatable, drawable, shots)
	

	# draw screen, set x,y as center of screen
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2

	# create player at center of screen
	player = Player(x, y, shots)
	# create an asteroid field
	asteroid_field = AsteroidField()


	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: # if user clicks 'x' while game is running, game will close
				pygame.quit()
				return
		screen.fill((0,0,0)) # Fill screen with black
		dt = gameclock.tick(60) / 1000
		for item in drawable:
			item.draw(screen)
		for item in updatable:
			item.update(dt)
		for asteroid in asteroids:
			if player.collision(asteroid):
				print("Game over!")
				pygame.quit()
				sys.exit()
			for bullet in shots:
				if asteroid.collision(bullet):
					asteroid.split()
					bullet.kill()

		pygame.display.flip() # Refresh screen
		
if __name__ == "__main__":
	main()
