import pygame, spritesheet
from move import Move

class Player(pygame.sprite.Sprite):
    def __init__(self, initial_position):
        pygame.sprite.Sprite.__init__(self)
        # загружаем спрайт стены
        # картинки игрока из общего спрайта
        self.player_images = []
        self.player_images = spritesheet.spritesheet("player.png").images_at(((0, 0, 53, 63), (0, 63, 53, 63), (0, 126, 53, 63), (0, 189, 53, 63)), colorkey=(0, 0, 0))
        self.image = self.player_images[0].convert()

        self.image.set_colorkey(pygame.Color(0, 0, 0))
        self.rect = self.image.get_rect()
        # устанавливаем координаты
        self.rect.x = initial_position[0]
        self.rect.y = initial_position[1]

        # изначально игрок стоит
        self.x_motion = Move.STOP
        self.y_motion = Move.STOP

        self.door_nearby = None
        self.space_is_down = False

    def draw(self, screen):
        # рисуем картинку игрока в зависимости от его текущего движения
        if self.y_motion == Move.DOWN or (self.x_motion == Move.STOP and self.y_motion == Move.STOP):
            screen.blit(self.player_images[0], (self.rect.x, self.rect.y))
        elif self.y_motion == Move.UP:
            screen.blit(self.player_images[1], (self.rect.x, self.rect.y))
        elif self.x_motion == Move.LEFT:
            screen.blit(self.player_images[2], (self.rect.x, self.rect.y))
        elif self.x_motion == Move.RIGHT:
            screen.blit(self.player_images[3], (self.rect.x, self.rect.y))

    def handle_move(self, event, walls, doors):

        # обрабатывем нажание кнопок и реагируем на них
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.x_motion = Move.LEFT
            elif event.key == pygame.K_RIGHT:
                self.x_motion = Move.RIGHT
            elif event.key == pygame.K_UP:
                self.y_motion = Move.UP
            elif event.key == pygame.K_DOWN:
                self.y_motion = Move.DOWN
            elif event.key == pygame.K_SPACE:
                if not self.space_is_down:
                    if self.door_nearby is not None:
                        self.door_nearby.change_state()
                self.space_is_down = True

        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                self.x_motion = Move.STOP
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                self.y_motion = Move.STOP
            if event.key == pygame.K_SPACE:
                self.space_is_down = False


        #print('Current move is: ' + self.x_motion.value + ' ' + self.y_motion.value)

        prev_x = self.rect.x
        if self.x_motion == Move.LEFT:
            self.rect.x -= 3
        elif self.x_motion == Move.RIGHT:
            self.rect.x += 3

        # проверяем столкновение со стеной слева или справа
        collide = pygame.sprite.spritecollide(self, walls, False, False)
        if collide:
            self.rect.x = prev_x

        # проверяем столкновение со дверью слева или справа
        collide = pygame.sprite.spritecollide(self, doors, False, False)
        for door in collide:
            if not door.is_opened:
                self.rect.x = prev_x
            self.door_nearby = door

        prev_y = self.rect.y
        if self.y_motion == Move.UP:
            self.rect.y -= 3
        elif self.y_motion == Move.DOWN:
            self.rect.y += 3

        # проверяем столкновение со стеной сверху или снизу
        collide = pygame.sprite.spritecollide(self, walls, False, False)
        if collide:
            self.rect.y = prev_y

        # проверяем столкновение со дверью сверху или снизу
        collide = pygame.sprite.spritecollide(self, doors, False, False)
        for door in collide:
            if not door.is_opened:
                self.rect.y = prev_y
            self.door_nearby = door

        #print('Current position is: {} {}',self.rect.x, self.rect.y)

