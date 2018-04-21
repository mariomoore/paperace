import sys
import os
import pygame
import math
from paperace.car import Car

WIDTH = 800
HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (47, 79, 79)

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

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("paperace - my first python game")

    imgfile = os.path.join(os.path.split(__file__)[0], 'plansza\plansza.png')
    background = pygame.image.load(imgfile)

    a = Car(400, 80) # Pojazd gracza A

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                nearestpos = get_nearest_point(pygame.mouse.get_pos())
                if nearestpos in a.get_allowed_positions():
                    xoldpos = a.xpos
                    yoldpos = a.ypos
                    a.move(nearestpos)
                    #print(a.get_allowed_positions())
                    #print("Jest jeszcze: ", len(a.get_allowed_positions()), " możliwości")
                    pygame.draw.line(background, BLUE, [xoldpos, yoldpos], [a.xpos, a.ypos], 2)
                    if len(a.get_allowed_positions()) == 0:
                        print("Koniec gry! Następny ruch poza pole")
                        sys.exit()
            pygame.draw.circle(background, BLUE, [a.xpos, a.ypos], 5)
            screen.blit(background, background.get_rect())
        pygame.display.flip()

if __name__ == '__main__' :
    main()