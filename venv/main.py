import random
import sys
import pygame
from constants import black, white, display_height, display_width, car_width, clock, gameDisplay, carImg, carImg2, bg
from functions import text_objects, things, car, car2, things_dodged, crash

# стартуем в файле модули пайгейм
pygame.init()

# функция для запуска игры
def game_loop():
    # размещение
    x = (display_width * 0.75)
    y = (display_height * 0.8)
    x1 = (display_width * 0.25)
    y1 = (display_height * 0.8)
    # параметры для появления things
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 5
    thing_width = 72
    thing_height = 72

    # базовое значение для dodged
    dodged = 0

    x_change = 0  # позиция
    x1_change = 0  # позиция
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                gameExit = True
                sys.exit()
            # блок для обработки нажатия на клавиши
            if event.type == pygame.KEYDOWN:
                # если нажали на esc, то окно закр.
                if event.key == pygame.K_ESCAPE:
                    crashed = True
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_LEFT:
                    x_change = -5

                if event.key == pygame.K_a:
                    x1_change = -5

                elif event.key == pygame.K_RIGHT:
                    x_change = 5

                elif event.key == pygame.K_d:
                    x1_change = 5

            # условия для движения
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            # условия для движения
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x1_change = 0
        # смена позиции
        x += x_change

        # смена позиции 2
        x1 += x1_change

        # фон
        gameDisplay.blit(bg,(0,0))
        # вызов things
        things(thing_startx, thing_starty)
        thing_starty += thing_speed

        # создаем машину
        car(x, y)
        things_dodged(dodged)

        # создаем машину 2
        car2(x1, y1)
        things_dodged(dodged)

        # задаем границы
        if x > display_width - car_width or x < 0:
            gameExit = True
            crash()
        # задаем границы
        if x1 > display_width - car_width or x1 < 0:
            gameExit = True
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1
            # thing_width += (dodged * 1.2)

        if y < thing_starty + thing_height:

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                crash()
        if y1 < thing_starty + thing_height:

            if x1 > thing_startx and x1 < thing_startx + thing_width or x1 + car_width > thing_startx and x1 + car_width < thing_startx + thing_width:
                crash()

        # проверяем на обновления дисплея
        pygame.display.update()
        # кадры в секунду = 60
        clock.tick(60)

game_loop()
pygame.quit()
quit()