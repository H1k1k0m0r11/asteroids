import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    
    #funcao para iniciar
    pygame.init()

    #tela
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #titulo do programa
    pygame.display.set_caption("Asteroids")

    #para controlar o consumo de 'ram' do programa
    clock = pygame.time.Clock()
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    #loop principal do jogo, enquanto estiver jogando (running) = true, quando eu quiser fechar (running) = false
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
            
        screen.fill((0, 0, 0))

        for obj in drawable:
            obj.draw(screen)

        
        pygame.display.flip()

        #limitador de fps
        dt = clock.tick(60) / 1000

    #feixa o jogo
    pygame.quit()

if __name__ == "__main__":
    main()
