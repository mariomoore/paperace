import sys
import os
import pygame
import math
import random
from paperace.car import Car
from paperace.const import *


def main():
    run = True
    show_menu = True
    while run:
        if show_menu:
            human_players = menu()
        after_race_event = race_loop(human_players)
        show_menu = end_game(after_race_event)
    pygame.quit()


def menu():
    """Wyświetla menu, w którym można wybrać ilość graczy lub zamknąć grę.
    Zwraca ilość graczy."""
    screen.blit(background, background.get_rect())
    game_font = pygame.font.SysFont("monospace", 30)
    game_font.set_bold(True)
    text_to_show = game_font.render("1 Player", False, WHITE, BLACK)
    screen.blit(text_to_show, text_to_show.get_rect(center=(WIDTH/2, HEIGHT/2-120)))
    text_to_show = game_font.render("2 Players", False, WHITE, BLACK)
    screen.blit(text_to_show, text_to_show.get_rect(center=(WIDTH/2, HEIGHT/2-80)))
    text_to_show = game_font.render("3 Players", False, WHITE, BLACK)
    screen.blit(text_to_show, text_to_show.get_rect(center=(WIDTH/2, HEIGHT/2-40)))
    text_to_show = game_font.render("4 Players", False, WHITE, BLACK)
    screen.blit(text_to_show, text_to_show.get_rect(center=(WIDTH/2, HEIGHT/2)))
    text_to_show = game_font.render("5 Players", False, WHITE, BLACK)
    screen.blit(text_to_show, text_to_show.get_rect(center=(WIDTH/2, HEIGHT/2+40)))
    text_to_show = game_font.render("6 Players", False, WHITE, BLACK)
    screen.blit(text_to_show, text_to_show.get_rect(center=(WIDTH/2, HEIGHT/2+80)))
    text_to_show = game_font.render("Exit", False, WHITE, BLACK)
    screen.blit(text_to_show, text_to_show.get_rect(center=(WIDTH/2, HEIGHT/2+120)))
    pygame.display.flip()
    
    menu_loop = True
    while menu_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseclick = pygame.mouse.get_pos()
                if mouseclick[0] > 320 and mouseclick[0] < 480 and mouseclick[1] > 160 and mouseclick[1] < 200:
                    return 1
                elif mouseclick[0] > 320 and mouseclick[0] < 480 and mouseclick[1] > 200 and mouseclick[1] < 240:
                    return 2
                elif mouseclick[0] > 320 and mouseclick[0] < 480 and mouseclick[1] > 240 and mouseclick[1] < 280:
                    return 3
                elif mouseclick[0] > 320 and mouseclick[0] < 480 and mouseclick[1] > 280 and mouseclick[1] < 320:
                    return 4
                elif mouseclick[0] > 320 and mouseclick[0] < 480 and mouseclick[1] > 320 and mouseclick[1] < 360:
                    return 5
                elif mouseclick[0] > 320 and mouseclick[0] < 480 and mouseclick[1] > 360 and mouseclick[1] < 400:
                    return 6
                elif mouseclick[0] > 360 and mouseclick[0] < 440 and mouseclick[1] > 400 and mouseclick[1] < 440:
                    pygame.quit()
                    sys.exit()


def race_loop(human_players):
    """Przyjmuje ilość graczy. Ustawia wszystkie parametry oraz wykonuje główną
    pętlę gry. Zwraca wydarzenie: zwycięstwo, wyjście poza trasę, kraksa."""
    cars = init_cars_rand(human_players)  # Lista pojazdów
    cp = 0  # Aktualny gracz na liście - Current Player

    screen.blit(background, background.get_rect())
    for car in cars:
        pygame.draw.circle(screen, car.color, [car.xpos, car.ypos], 5)
    pygame.draw.rect(screen, cars[0].color, (0, 0, WIDTH, HEIGHT), 3)
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
                        pygame.draw.circle(screen, cars[cp].color, [cars[cp].xpos, cars[cp].ypos], 5)
                        del cars[cp]
                        cp -= 1
                        if len(cars) == 0:
                            return "Crash"
                    if check_crossing_lines(background, screen, (cars[cp].xpos, cars[cp].ypos), (xoldpos, yoldpos), RED, cars[cp].color) and xoldpos != 400:
                        pygame.draw.circle(screen, cars[cp].color, [cars[cp].xpos, cars[cp].ypos], 5)
                        return "Winning"
                    if len(cars[cp].get_allowed_positions()) == 0:
                        pygame.draw.circle(screen, cars[cp].color, [cars[cp].xpos, cars[cp].ypos], 5)
                        del cars[cp]
                        cp -= 1
                        if len(cars) == 0:
                            return "Out"
                    pygame.draw.circle(screen, cars[cp].color, [cars[cp].xpos, cars[cp].ypos], 5)
                    
                    cp = cp + 1
                    if cp >= len(cars):
                        cp = 0

                    pygame.draw.rect(screen, cars[cp].color, (0, 0, WIDTH, HEIGHT), 3)
        pygame.display.flip()


def end_game(after_race_event):
    """Przyjmuje wydarzenie: koniec gry, wyjście poza trasę, kraksa. Wyświetla
    wynik wyścigu oraz pyta o dalsze kroki: menu, nowa gra (ta sama liczba
    graczy i nowe ustawienia), wyjście. Zwraca True jeśli trzeba wyświetlić
    menu."""
    game_font = pygame.font.SysFont("monospace", 30)
    game_font.set_bold(True)
    if after_race_event == "Crash":
        text_to_show = game_font.render("Crash!", False, RED, WHITE)
        screen.blit(text_to_show, text_to_show.get_rect(center=(WIDTH/2, HEIGHT/2-40)))
    elif after_race_event == "Winning":
        text_to_show = game_font.render("Winning!", False, RED, WHITE)
        screen.blit(text_to_show, text_to_show.get_rect(center=(WIDTH/2, HEIGHT/2-40)))
    elif after_race_event == "Out":
        text_to_show = game_font.render("Next move out of screen!", False, RED, WHITE)
        screen.blit(text_to_show, text_to_show.get_rect(center=(WIDTH/2, HEIGHT/2-40)))
    text_to_show = game_font.render("Play again", False, WHITE, BLACK)
    screen.blit(text_to_show, text_to_show.get_rect(center=(WIDTH/2, HEIGHT/2+40)))
    text_to_show = game_font.render("Menu", False, WHITE, BLACK)
    screen.blit(text_to_show, text_to_show.get_rect(center=(WIDTH/2, HEIGHT/2+80)))
    text_to_show = game_font.render("Exit", False, WHITE, BLACK)
    screen.blit(text_to_show, text_to_show.get_rect(center=(WIDTH/2, HEIGHT/2+120)))
    pygame.display.flip()
    
    menu_loop = True
    while menu_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseclick = pygame.mouse.get_pos()
                if mouseclick[0] > 300 and mouseclick[0] < 500 and mouseclick[1] > 320 and mouseclick[1] < 360:
                    return False
                elif mouseclick[0] > 360 and mouseclick[0] < 440 and mouseclick[1] > 360 and mouseclick[1] < 400:
                    return True
                elif mouseclick[0] > 360 and mouseclick[0] < 440 and mouseclick[1] > 400 and mouseclick[1] < 440:
                    pygame.quit()
                    sys.exit()


def init_cars_rand(players):
    """Zwraca listę pojazdów (cars) w zależności od liczby graczy (players).
    Pojazdy ustawiane są losowo na linii ([400, 40], [400, 140])."""
    cars = []
    colors = [RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA]
    y_positions = [40, 60, 80, 100, 120, 140]
    for _ in range(players):
        y = y_positions[random.randint(0, len(y_positions)-1)]
        y_positions.remove(y)
        color = colors[random.randint(0, len(colors)-1)]
        colors.remove(color)
        cars.append(Car(400, y, color))
    return cars


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


def get_allowed_car_positions(cars, i):
    """Zwraca listę punktów, na które może przemieścić się samochód cars[i]
    oraz usuwa pozycje, na których znajduje się pojazd przeciwnika)."""
    positions = cars[i].get_allowed_positions()
    for c in cars:
        position_to_remove = ((c.xpos, c.ypos))
        if position_to_remove in positions:
            positions.remove(position_to_remove)
    return positions


def check_crossing_lines(first_img, second_img, rectbegin, rectend, first_color, second_color):
    """Zwraca True jeśli na prostokątnym obszarze (rectbegin) X (rectend) na
    obrazkach first_img i second_img przecinają się linie o kolorach
    odpowiednio: first_color i second_color."""
    # Ustawia prawidłowy prostokąt LG X PD
    xbegin = min(rectbegin[0], rectend[0])
    ybegin = min(rectbegin[1], rectend[1])
    xend = max(rectbegin[0], rectend[0])
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


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PapeRace")

    imgfile = os.path.join(os.path.split(__file__)[0], 'plansza\plansza.png')
    background = pygame.image.load(imgfile).convert()
    
    main()
