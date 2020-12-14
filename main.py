import pygame
import config
from game import Game
from player import Player

# inicializando a biblioteca
pygame.init()

# inicializando a tela
screen = pygame.display.set_mode((config.screen_width, config.screen_height), 0)
# fonte = pygame.font.SysFont("arial", 24, True, False)

pygame.display.set_caption("Fora de Tempo")

clock = pygame.time.Clock()

if __name__ == "__main__":
    player = Player(1, 1, screen)
    game = Game(player, screen)

    while True:
        clock.tick(10)
        pygame.display.flip()

        # Calcular as Regras
        game.calcular_regras()
        player.calcular_regras()

        # Pintar a Tela
        screen.fill(config.black)
        game.pintar()
        player.pintar()
        pygame.display.update()

        # Captura de eventos
        eventos = pygame.event.get()
        game.processar_eventos(eventos)
        player.processar_eventos(eventos)
