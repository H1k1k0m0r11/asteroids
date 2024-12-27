import pygame
from constants import *

def main():
    print("Starting asteroids!")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.display.set_caption("Asteroids")


    #loop principal do jogo, enquanto estiver jogando (running) = true, quando eu quiser fechar (running) = false
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #tela cor preta
        screen.fill((0, 0, 0))

        #atualiza a tela
        pygame.display.flip()

    #feixa o jogo
    pygame.quit()

if __name__ == "__main__":
    main()
