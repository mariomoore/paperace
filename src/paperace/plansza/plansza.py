import pygame
from math import pi

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (47, 79, 79)

WIDTH = 800
HEIGHT = 600
SIZE = 20 # rozmiar kratki

img = pygame.Surface((WIDTH, HEIGHT))
img.fill(WHITE)

# Linie poziome i pionowe
for i in range(SIZE, WIDTH, SIZE):
    pygame.draw.line(img, GRAY, [i, 0], [i, HEIGHT])
for j in range(SIZE, HEIGHT, SIZE):
    pygame.draw.line(img, GRAY, [0, j], [WIDTH, j])

# Linia startu
pygame.draw.line(img, RED, [400, 20], [400, 160], 3)

# Zewnętrzna banda
pygame.draw.arc(img, BLACK, [20, 20, 560, 560], pi/2, 3*pi/2, 3)
pygame.draw.arc(img, BLACK, [WIDTH-20-560, 20, 560, 560], 3*pi/2, pi/2, 3)
pygame.draw.line(img, BLACK, [300, 20], [WIDTH-20-560/2+10, 20], 3)
pygame.draw.line(img, BLACK, [300-11, 580], [WIDTH-20-560/2, 580], 3)

# Wewnętrzna banda
pygame.draw.arc(img, BLACK, [160, 160, 280, 280], pi/2, 3*pi/2, 3)
pygame.draw.arc(img, BLACK, [WIDTH-20-420, 160, 280, 280], 3*pi/2, pi/2, 3)
pygame.draw.line(img, BLACK, [300, 160], [500+5, 160], 3)
pygame.draw.line(img, BLACK, [300-5, 440], [500, 440], 3)

pygame.image.save(img, 'plansza.png')

pygame.quit()