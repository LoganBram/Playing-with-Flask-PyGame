import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


def main():
    # inf loop so game display doesnt close
    run = True
    while run:
        # getting list of all events, loop through them to check them
        for event in pygame.event.get():
            # check if user closed window
            if event.type == pygame.QUIT:
                run = False
        pygame.quit()


main()
