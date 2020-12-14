import pygame
import config
from elemento_jogo import ElementoJogo


class Player(ElementoJogo):
    def __init__(self, x_position, y_position, screen):
        self.screen = screen
        self.last = "down"
        self.image = player_images["stop"]["down"]
        self.x = x_position
        self.y = y_position
        self.rect = pygame.Rect(self.x * config.scale, self.y * config.scale, config.scale, config.scale)
        self.alternar = 1

        # velocidade
        self.vel_x = 0
        self.vel_y = 0
        self.coluna_intencao = self.x
        self.linha_intencao = self.y

    def pintar(self, camera):
        if self.alternar == 1:
            self.alternar = 0
        else:
            self.alternar = 1
        if (self.vel_y != 0 or self.vel_x != 0) and self.alternar == 1:
            self.image = player_images["walk"][self.last]
        else:
            self.image = player_images["stop"][self.last]

        self.rect = pygame.Rect(self.x * config.scale, self.y * config.scale - (camera[1] * config.scale), config.scale,
                                config.scale)
        self.screen.blit(self.image, self.rect)

    def calcular_regras(self):
        self.coluna_intencao = self.x + self.vel_x
        self.linha_intencao = self.y + self.vel_y

        if self.x < self.coluna_intencao:
            self.last = "right"
        elif self.x > self.coluna_intencao:
            self.last = "left"

        if self.y > self.linha_intencao:
            self.last = "up"
        elif self.y < self.linha_intencao:
            self.last = "down"

    def processar_eventos(self, eventos):

        for event in eventos:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:  # up
                    self.vel_y = -1
                    self.vel_x = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:  # down
                    self.vel_y = 1
                    self.vel_x = 0
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:  # left
                    self.vel_x = -1
                    self.vel_y = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:  # right
                    self.vel_x = 1
                    self.vel_y = 0

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_w:  # up
                    self.vel_y = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:  # down
                    self.vel_y = 0
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:  # left
                    self.vel_x = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:  # right
                    self.vel_x = 0

    def aceitar_movimento(self):
        self.x = self.coluna_intencao
        self.y = self.linha_intencao


player_images = {

    "stop": {
        "up": pygame.transform.scale(pygame.image.load("assets/images/player_up.png"),
                                     (config.scale, config.scale)),
        "down": pygame.transform.scale(pygame.image.load("assets/images/player_down.png"),
                                       (config.scale, config.scale)),
        "left": pygame.transform.scale(pygame.image.load("assets/images/player_left.png"),
                                       (config.scale, config.scale)),
        "right": pygame.transform.scale(pygame.image.load("assets/images/player_right.png"),
                                        (config.scale, config.scale)),
    },
    "walk": {
        "up": pygame.transform.scale(pygame.image.load("assets/images/player_up_walk.png"),
                                     (config.scale, config.scale)),
        "down": pygame.transform.scale(pygame.image.load("assets/images/player_down_walk.png"),
                                       (config.scale, config.scale)),
        "left": pygame.transform.scale(pygame.image.load("assets/images/player_left_walk.png"),
                                       (config.scale, config.scale)),
        "right": pygame.transform.scale(pygame.image.load("assets/images/player_right_walk.png"),
                                        (config.scale, config.scale)),
    }
}
