import sys, pygame
import cProfile
import re
from wall import Wall
from player import Player
from ghost import Ghost
from door import Door

cProfile.run('re.compile("foo|bar")')

# Инициализация игрового движка PyGame
pygame.init()
# устанавливаем частоту обновления 30 кадров/сек
FPS = 60
clock = pygame.time.Clock()

# устанавливаем размер окна
screen = pygame.display.set_mode((1360, 760), pygame.HWSURFACE | pygame.DOUBLEBUF)
# устанавливаем заголовок окна
pygame.display.set_caption("Игра - Страшный призрак")

# создаем группу спрайтов стен
walls = pygame.sprite.Group()
doors = pygame.sprite.Group()
# загружаем данные из файла level0.txt, где описана структура уровня (0 - ничего нет, 1 - стена)
level_lines = open("level0.txt","r").readlines()
i = 0
for line in level_lines:
    j = 0
    for blockType in line:
        if blockType == "1":
            walls.add(Wall((j * 40, i * 40)))
        elif blockType == "2":
            doors.add(Door((j * 40, i * 40), True))
        elif blockType == "3":
            doors.add(Door((j * 40, i * 40), False))
        j = j + 1
    i = i + 1
i = 0

# создаем игрока
player = Player((1260, 600));

#coздаем приведение
ghost = Ghost((100, 100));

# бесконечный цикл игры
i = 0
while True:
    # обрабатывем нажание кнопок и реагируем на них
    for event in pygame.event.get():
        # нажали выход из игры - прекращаем программу
        if event.type == pygame.QUIT:
            sys.exit()

    #двигаем игрока
    player.handle_move(event, walls, doors)

    # заполняем поле черным
    screen.fill(pygame.Color(0, 0, 0))
    #рисуем стены
    for wall in walls:
        wall.draw(screen)
    # рисуем двери
    for wall in doors:
        doors.draw(screen)
    # рисуем игрока
    player.draw(screen)
    #рисуем приведение
    ghost.draw(screen)

    # обновляем экран (все что мы сделали выше применяется на экране)
    pygame.display.update()
    # устанавливаем скорость отрисовки экрана FPS = Frames Per Second
    clock.tick(FPS)