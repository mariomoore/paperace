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

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("paperace - my first python game")

    imgfile = os.path.join(os.path.split(__file__)[0], 'plansza\plansza.png')
    background = pygame.image.load(imgfile)

    a = Car(400, 80, BLUE) # Pojazd gracza A

    pygame.draw.circle(background, a.color, [a.xpos, a.ypos], 5)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                nearestpoint = get_nearest_point(pygame.mouse.get_pos())
                if nearestpoint in a.get_allowed_positions():
                    xoldpos = a.xpos
                    yoldpos = a.ypos
                    a.move(nearestpoint)
                    pygame.draw.line(background, a.color, [xoldpos, yoldpos], [a.xpos, a.ypos], 2)
                    if check_crossing_lines(screen, background, (a.xpos, a.ypos), (xoldpos, yoldpos), BLACK, a.color):
                        print("Koniec gry! Kraksa")
                        run = False
                    if check_crossing_lines(screen, background, (a.xpos, a.ypos), (xoldpos, yoldpos), RED, a.color):
                        print("Koniec gry! ZWYCIĘSTWO!")
                        run = False
                    if len(a.get_allowed_positions()) == 0:
                        print("Koniec gry! Następny ruch poza pole")
                        run = False
                    pygame.draw.circle(background, a.color, [a.xpos, a.ypos], 5)
        screen.blit(background, background.get_rect())
        pygame.display.flip()

if __name__ == '__main__' :
    main()