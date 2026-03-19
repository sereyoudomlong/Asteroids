import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    while True:
        log_state()
        #clock for fps
        clock = pygame.time.Clock()

        #init player in the middle of screen
        player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

        # inf loop for event handle
        for event in pygame.event.get():
            # quit when press x on the window
            if event.type == pygame.QUIT:
                return
        
        # pause the loop until 1/60th of a second then continue
        delta = clock.tick(60)
        # .tick() return delta time in millisecond so we divide by 1000 to get second
        dt = delta / 1000

        
        #just filling screen with black color
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()

