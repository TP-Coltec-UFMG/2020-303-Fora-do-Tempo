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

click = False

def escreve_texto(texto, fonte, cor, superficie, x, y):
    texto_obj = font.render(texto, 1, cor)
    texto_rect = texto_obj.get_rect()
    texto_rect.topleft = (x, y)
    superficie.blit(texto_obj, texto_rect)

def menu_principal():
    player = Player(1, 1, screen)
    game = Game(player, screen)
    rodando = True

    while True:

        screen.fill(0, 0, 0)
        escreve_texto('menu principal', font, (255, 255, 255), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        botao1 = pygame.Rect(50, 100, 200, 50)
        botao2 = pygame.Rect(50, 200, 200, 50)

        if botao1.collidepoint((mx, my)):
            pass
        if botao2.collidepoint((mx, my)):
            pass

        pygame.draw.rect(screen, (255, 0, 0), botao1)
        pygame.draw.rect(screen, (255, 0, 0), botao2)

    while rodando:
        clock.tick(10)
        pygame.display.flip()

        # Calcular as Regras
        game.calcular_regras()
        player.calcular_regras()

        # Pintar a Tela
        screen.fill(config.black)
        game.pintar(game.camera)
        player.pintar(game.camera)
        pygame.display.update()

        # Captura de eventos
        eventos = pygame.event.get()
        game.processar_eventos(eventos)
        player.processar_eventos(eventos)