import sys
import pygame
pygame.init()

# set size of window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# name of game
pygame.display.set_caption("first game")

WHITE = (255, 255, 255)


def main():
    # inf loop so game display doesnt close
    run = True
    while run:
        # getting list of all events, loop through them to check them
        for event in pygame.event.get():
            # check if user closed window
            if event.type == pygame.QUIT:
                run = False
        # if event type is not quit

        # fill window color, tuple RGB
        WIN.fill((WHITE))
        # display wont updated drawn things until we use this command
        pygame.display.update()

    pygame.quit()


# runs main function IFF we run file directly
if __name__ == '__main__':
    main()
