import sys
import os
import pygame
pygame.init()

# set size of window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# name of game
pygame.display.set_caption("first game")

WHITE = (255, 255, 255)
FPS = 60

# loads in images, assets referring to folder,spaceship yellow file
YellowShip = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))


def draw_window():
    # fill window color, tuple RGB
    WIN.fill((WHITE))
    # display wont updated drawn things until we use this command
    pygame.display.update()


def main():
    # creates object to track time (documentation)
    clock = pygame.time.Clock()
    # inf loop so game display doesnt close
    run = True
    while run:
        # "by calling once per frame, program will never
        # run faster then given FPS"
        clock.tick(FPS)
        # getting list of all events, loop through them to check them
        for event in pygame.event.get():
            # check if user closed window
            if event.type == pygame.QUIT:
                run = False
        # if event type is not quit
        draw_window()

    pygame.quit()


# runs main function IFF we run file directly
if __name__ == '__main__':
    main()
