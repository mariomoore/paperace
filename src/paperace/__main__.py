import sys
import os
import pygame
import math
from paperace.car import Car
from paperace.const import *

def get_nearest_point(mousexy):
    """Zwraca punkt najbliższego przecięcia kratek po kliknięciu myszką.""" 
    if mousexy[0] % 20 < 10:
        x = int(mousexy[0] / 20.0) * 20
    else:
        x = int(math.ceil(mousexy[0] / 20.0)) * 20
    if mousexy[1] % 20 < 10:
        y = int(mousexy[1] / 20.0) * 20
    else:
        y = int(math.ceil(mousexy[1] / 20.0)) * 20    
    return (x, y)

def check_crossing_lines(first_img, second_img, rectbegin, rectend, first_color, second_color):
    """Zwraca True jeśli na prostokątnym obszarze rectbegin x rectend na obrazkach first_img i second_img przecinają się linie o kolorach odpowiednio: first_color i second_color."""
    # Ustawaia prawidłowy prostokąt
    xbegin = min(rectbegin[0], rectend[0])
    xend = max(rectbegin[0], rectend[0])
    ybegin = min(rectbegin[1], rectend[1])
    yend = max(rectbegin[1], rectend[1])
    if xbegin == xend:
        xend = xend + 1
    if ybegin == yend:
        yend = yend + 1

    for y in range(ybegin, yend):
        for x in range(xbegin, xend):
            first_img_color = first_img.get_at((x, y))
            second_img_color = second_img.get_at((x, y))
            if first_img_color == first_color and second_img_color == second_color:
                return True
    return False

def get_allowed_car_positions(cars, i):
    """Zwraca listę punktów, na które może przemieścić się samochód cars[i] oraz usuwa pozycje, na których znajduje się pojazd przeciwnika)."""
    positions = cars[i].get_allowed_positions()
    for c in cars:
        position_to_remove = ((c.xpos, c.ypos))
        if position_to_remove in positions:
            positions.remove(position_to_remove)
    return positions

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("paperace - my first python game")

    imgfile = os.path.join(os.path.split(__file__)[0], 'plansza\plansza.png')
    background = pygame.image.load(imgfile)

    a = Car(400, 60, BLUE) # Pojazd gracza A
    b = Car(400, 120, GREEN) # Pojazd gracza B

    cars = [a, b] # Lista pojazdów
    cp = 0 # Aktualny gracz na liście. Current Player

    screen.blit(background, background.get_rect())
    pygame.draw.circle(screen, a.color, [a.xpos, a.ypos], 5)
    pygame.draw.circle(screen, b.color, [b.xpos, b.ypos], 5)
    pygame.draw.rect(screen, a.color, (0, 0, WIDTH, HEIGHT) , 3)
    pygame.display.flip()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                nearestpoint = get_nearest_point(pygame.mouse.get_pos())
                if nearestpoint in get_allowed_car_positions(cars, cp):
                    xoldpos = cars[cp].xpos
                    yoldpos = cars[cp].ypos
                    cars[cp].move(nearestpoint)
                    pygame.draw.line(screen, cars[cp].color, [xoldpos, yoldpos], [cars[cp].xpos, cars[cp].ypos], 2)
                    if check_crossing_lines(background, screen, (cars[cp].xpos, cars[cp].ypos), (xoldpos, yoldpos), BLACK, cars[cp].color):
                        print("Koniec gry! Kraksa")
                        run = False
                    if check_crossing_lines(background, screen, (cars[cp].xpos, cars[cp].ypos), (xoldpos, yoldpos), RED, cars[cp].color) and xoldpos != 400:
                        print("Koniec gry! ZWYCIĘSTWO!")
                        run = False
                    if len(cars[cp].get_allowed_positions()) == 0:
                        print("Koniec gry! Następny ruch poza pole")
                        run = False
                    pygame.draw.circle(screen, cars[cp].color, [cars[cp].xpos, cars[cp].ypos], 5)
                    
                    cp = cp + 1
                    if cp >= len(cars):
                        cp = 0

                    pygame.draw.rect(screen, cars[cp].color, (0, 0, WIDTH, HEIGHT) , 3)
        pygame.display.flip()

if __name__ == '__main__' :
    main()