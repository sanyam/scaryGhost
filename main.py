import sys, pygame, spritesheet

# Инициализация игрового движка pygame
pygame.init()

# устанавливаем размер окна
screen = pygame.display.set_mode((800, 576))
# устанавливаем заголовок окна
pygame.display.set_caption("Игра - Страшный призрак!")

# устанавливаем частоту обновления 60 кадров/сек
clock = pygame.time.Clock()
fps = 60

# устанавлваем фон черный
black = [0, 0, 0]

# устанавливаем начальные координаты игрока
x = 50
y = 50

#40x36
spriteGroup = pygame.sprite.Group()

wall = pygame.image.load("wall-small.jpg")

#ghost = pygame.image.load("ghost.png")
gss = spritesheet.spritesheet('ghost-sprite.png')
pss = spritesheet.spritesheet('player.png')
ghost_images = []
ghost_images = gss.images_at(((0, 0, 42, 47),(0, 47, 42, 47),(0, 94, 42, 47),(0, 141, 42, 47)), colorkey = (0,0,0))
player_images = []
player_images = pss.images_at(((0, 0, 53, 63),(0, 63, 53, 63),(0, 126, 53, 63),(0, 189, 53, 63)), colorkey = (0,0,0))

pygame.display.flip()

RIGHT = "right"
LEFT = "left"
UP = "up"
DOWN = "down"
STOP = "stop"

x_motion = STOP
y_motion = STOP

while 1:
    screen.fill(black)

    i = 0
    while i < 20:
        screen.blit(wall, (i * 40, 0))
        screen.blit(wall, (i * 40, 540))
        i = i + 1

    i = 0
    while i < 14:
        screen.blit(wall, (0, 36 + 36 * i))
        screen.blit(wall, (760, 36 + 36 * i))
        i = i + 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_motion = LEFT
            elif event.key == pygame.K_RIGHT:
                x_motion = RIGHT
            elif event.key == pygame.K_UP:
                y_motion = UP
            elif event.key == pygame.K_DOWN:
                y_motion = DOWN
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                x_motion = STOP
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                y_motion = STOP
    #ghost_images
    # [0] - вниз
    # [1] - влево
    # [2] - вправо
    # [3] - вверх
    screen.blit(ghost_images[0], (540/2-x, 760/2-y))

    if x_motion == STOP and y_motion == STOP:
        screen.blit(player_images[0], (x, y))

    if x_motion == LEFT:
        x -= 3
        screen.blit(player_images[2], (x, y))

    elif x_motion == RIGHT:
        x += 3
        screen.blit(player_images[3], (x, y))

    elif y_motion == UP:
        y -= 3
        screen.blit(player_images[1], (x, y))

    elif y_motion == DOWN:
        y += 3
        screen.blit(player_images[0], (x, y))

    pygame.display.update()

    clock.tick(fps)