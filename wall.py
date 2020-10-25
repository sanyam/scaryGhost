import pygame
from pygame.locals import *

class Wall(pygame.sprite.Sprite):
    def __init__(self, initial_position):
        pygame.sprite.Sprite.__init__(self)

        # загружаем спрайт стены
        self.image = pygame.image.load("wall-small.jpg").convert()
        self.image.set_colorkey(pygame.Color(255, 0, 0))
        self.rect = self.image.get_rect()

        # устанавливаем координаты
        self.rect.topleft = initial_position

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
