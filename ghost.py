import pygame, spritesheet
from move import Move

class Ghost(pygame.sprite.Sprite):
    def __init__(self, initial_position):
        pygame.sprite.Sprite.__init__(self)
        # загружаем спрайт стены
        # картинки игрока из общего спрайта
        self.ghost_images = []
        self.ghost_images = spritesheet.spritesheet("ghost-sprite.png").images_at(((0, 0, 42, 47),(0, 47, 42, 47),(0, 94, 42, 47),(0, 141, 42, 47)), colorkey = (0,0,0))
        self.image = self.ghost_images[0].convert()

        self.image.set_colorkey(pygame.Color(0, 0, 0))
        self.rect = self.image.get_rect()
        # устанавливаем координаты
        self.rect.x = initial_position[0]
        self.rect.y = initial_position[1]

        # изначально игрок стоит
        self.x_motion = Move.STOP
        self.y_motion = Move.STOP

    def draw(self, screen):
        screen.blit(self.ghost_images[3], (self.rect.x, self.rect.y))


#    def handle_move(self, player, walls):

        # обрабатывем нажание кнопок и реагируем на них
        #print('Current move is: ' + self.x_motion.value + ' ' + self.y_motion.value)
'''
        prev_x = self.rect.x
        if self.x_motion == Move.LEFT:
            self.rect.x -= 3
        elif self.x_motion == Move.RIGHT:
            self.rect.x += 3
        collide = pygame.sprite.spritecollide(self, walls, False, False)
        if collide:
            self.rect.x = prev_x

        prev_y = self.rect.y
        if self.y_motion == Move.UP:
            self.rect.y -= 3
        elif self.y_motion == Move.DOWN:
            self.rect.y += 3
        collide = pygame.sprite.spritecollide(self, walls, False, False)
        if collide:
            self.rect.y = prev_y
'''
        #print('Current position is: {} {}',self.rect.x, self.rect.y)

