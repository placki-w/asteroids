# boot.dev pygame example of asteroids for some random reason

import pygame
from constants import *
from player import Player

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    #Player Object
    player = Player(SCREEN_WIDTH / 2,  SCREEN_HEIGHT / 2)

    #Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  
        screen.fill([0,0,0])
        player.draw(screen)
        pygame.display.flip()

        # limit the framerate to 60 FPX
        dt = clock.tick(60) / 1000






if __name__ == "__main__":
    main()