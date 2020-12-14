import math

import pygame
import config
from elemento_jogo import ElementoJogo
from maps.maps import mapa1, mapa2

# cenario
from tree import Tree


class Game(ElementoJogo):
    def __init__(self, player, screen):
        self.screen = screen
        self.player = player
        self.objects = []
        self.map = []
        self.set_up()
        self.camera = [0, 0]

    def set_up(self):
        # self.objects.append(self.player)
        tree = Tree(10, 10, "green")
        self.objects.append(tree)
        self.load_map(mapa1)

    def calcular_regras(self):
        col = self.player.coluna_intencao
        lin = self.player.linha_intencao

        if col < 0 or col > (len(self.map[0]) - 1):
            return

        if lin < 0 or lin > (len(self.map) - 1):
            return

        if self.map[lin][col][0:1] != "W" and self.map[lin][col] != "OBJ":
            self.player.aceitar_movimento()

    def pintar(self, camera):
        # self.screen.fill(config.black)
        # self.processar_eventos()

        self.render_map()

        for p in self.objects:
            p.pintar(self.screen, self.camera)

    def change_map(self, num):
        self.map = []
        self.objects = []
        if num == 2:
            self.load_map(mapa2)

    def evento_objeto(self):
        col = self.player.x
        lin = self.player.y
        last = self.player.last

        for p in self.objects:
            if last == "right" and p.x - 1 == col and p.y[0] == lin:
                self.change_map(2)
            elif last == "left" and p.x + 1 == col and p.y[0] == lin:
                self.change_map(2)

    def processar_eventos(self, eventos):
        for event in eventos:
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.evento_objeto()

    def load_map(self, mapa):
        for line in mapa:
            tiles = []
            for i in range(0, len(line), 1):
                tiles.append(line[i])
            self.map.append(tiles)

    def render_map(self):

        self.determine_camera()

        y_pos = 0
        for line in self.map:
            x_pos = 0
            for tile in line:
                if tile != "OBJ":
                    image = map_tile_images[tile]
                else:
                    image = map_tile_images["G1"]

                rect = pygame.Rect(x_pos * config.scale, y_pos * config.scale - (self.camera[1] * config.scale),
                                   config.scale, config.scale)
                self.screen.blit(image, rect)
                x_pos += 1
            y_pos += 1

    def determine_camera(self):
        max_y_position = len(self.map) - config.screen_height / config.scale
        y_position = self.player.y - math.ceil(round(config.screen_height / config.scale / 2))

        if max_y_position >= y_position >= 0:
            self.camera[1] = y_position
        elif y_position < 0:
            self.camera[1] = 0
        else:
            self.camera[1] = max_y_position


map_tile_images = {
    "G1": pygame.transform.scale(pygame.image.load("assets/images/grass1.png"), (config.scale, config.scale)),
    "W1": pygame.transform.scale(pygame.image.load("assets/images/water.png"), (config.scale, config.scale)),
    "W2": pygame.transform.scale(pygame.image.load("assets/images/water2.png"), (config.scale, config.scale)),
    "W3": pygame.transform.scale(pygame.image.load("assets/images/water3.png"), (config.scale, config.scale)),
    "W4": pygame.transform.scale(pygame.image.load("assets/images/water4.png"), (config.scale, config.scale)),
    "W5": pygame.transform.scale(pygame.image.load("assets/images/water5.png"), (config.scale, config.scale)),
    "W6": pygame.transform.scale(pygame.image.load("assets/images/water6.png"), (config.scale, config.scale)),
    "W7": pygame.transform.scale(pygame.image.load("assets/images/water7.png"), (config.scale, config.scale)),
    "W8": pygame.transform.scale(pygame.image.load("assets/images/water8.png"), (config.scale, config.scale)),
    "W9": pygame.transform.scale(pygame.image.load("assets/images/water9.png"), (config.scale, config.scale)),
}
