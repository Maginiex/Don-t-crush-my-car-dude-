from pygame import time, image, transform, display
# размер окна
display_width = 800  # параметр высоты
display_height = 600  # параметр ширины

# окно игры
gameDisplay = display.set_mode((display_width, display_height))  # размер
display.set_caption("Don't crush my car, dude!")  # название

# цвета
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# кадры в секунду
clock = time.Clock()

#задний фон
bg = image.load('1621617616_1-phonoteka_org-p-fon-dorogi-dlya-detei-1.jpg')
bg = transform.scale(bg, (800, 600))

# игрок
carImg = image.load("c5fa9689-a185-48d2-aa22-f5d906ed04f6-removebg-preview.png")  # картинка для игрока
carImg = transform.scale(carImg, (70, 80))  # задаем размер картинки, если большая
car_width = 73

# игрок2
carImg2 = image.load("red-car-top-view-clipart-2.png")  # картинка для игрока
carImg2 = transform.scale(carImg2, (114, 89))  # задаем размер картинки, если большая
car_width2 = 73

#препятствие
enemyImg = image.load('Без_названия-removebg-preview.png')
enemyImg = transform.scale(enemyImg, (70, 80))