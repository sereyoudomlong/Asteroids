import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from logger import log_state, log_event
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font(None, 36)
    dt = 0
    #clock for fps
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    

    #init player in the middle of screen
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidField = AsteroidField()

    score = 0


    while True:
        log_state()

        #loop for event handle
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
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("GAME OVER!!!!")
                sys.exit()
            
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    score += asteroid.split()
                    log_event("asteroid_shot")

                
    

        for thing in drawable:
            thing.draw(screen)

        text = font.render("SCORE: " + str(score), 1, 'white')
        screen.blit(text, (10, 10))
        pygame.display.flip()



if __name__ == "__main__":
    main()

