import time
from datetime import datetime
import pygame.freetype
from constants import black, gameDisplay, carImg, carImg2, display_width, display_height, enemyImg, bg
import pygame

# функция для появляющихся элементов на дороге
def things(thingx, thingy):
    gameDisplay.blit(enemyImg, [thingx, thingy] )

#дата и время
def get_time_now():
    cur_time = datetime.now().time()
    cur_date = datetime.now().date()
    return f'время: {cur_time} / дата: {cur_date}'

# отрисовка авто
def car(x, y):
    gameDisplay.blit(carImg, (x, y))


# отрисовка авто 2
def car2(x1, y1):
    gameDisplay.blit(carImg2, (x1, y1))


# счетчик
def things_dodged(count):
    font = pygame.font.SysFont(None, 30)
    text = font.render("Проехал: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


# обработка текста
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# вывод текста на экран
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)
    from main import game_loop
    game_loop()



def crash():
    with open('database.txt', 'w+', encoding='utf8') as file:
        file.write(get_time_now())
    message_display('GAME OVER!')