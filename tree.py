import pygame

import config


class Tree:
    def __init__(self, x_all, y_base, color):
        self.x = x_all
        self.y = (y_base, y_base - 1)
        self.top = tree_images[color]["top"]
        self.base = tree_images[color]["base"]

    def pintar(self, tela, camera):
        rect_base = pygame.Rect(self.x * config.scale, self.y[0] * config.scale - (camera[1] * config.scale),
                                config.scale, config.scale)
        rect_top = pygame.Rect(self.x * config.scale, self.y[1] * config.scale - (camera[1] * config.scale),
                               config.scale, config.scale)
        tela.blit(self.top, rect_top)
        tela.blit(self.base, rect_base)


tree_images = {
    "green": {
        "base": pygame.transform.scale(pygame.image.load("assets/images/tree_base1.png"), (config.scale, config.scale)),
        "top": pygame.transform.scale(pygame.image.load("assets/images/tree_top1.png"), (config.scale, config.scale)),
    }
}
