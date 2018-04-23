import pytest
from paperace.__main__ import get_nearest_point
import pygame
from paperace.__main__ import check_crossing_lines
import os
import sys

@pytest.mark.parametrize('mousexy, answerxy', [
    ((0, 0), (0, 0)),
    ((800, 600), (800, 600)),
    ((19, 84), (20, 80)),
    ((50, 95), (60, 100)),
])
def test_get_nearest_point(mousexy, answerxy):
    """Sprawdzenie czy metoda podaje najbliższy punkt (przecięcie kratki) po kliknięciu myszą"""
    point = get_nearest_point(mousexy)
    assert point == answerxy

@pytest.mark.parametrize('begin, end, colorscr, colorbgd, answer', [
    ((0, 0), (10, 10), (0, 0, 0, 255), (0, 0, 255, 255), True), # BLACK, BLUE
    ((10, 0), (20, 10), (0, 0, 0, 255), (0, 0, 255, 255), False), # BLACK, BLUE
    ((20, 0), (30, 10), (255, 0, 0, 255), (0, 0, 255, 255), True), # RED, BLUE
])
def test_check_crossing_lines(begin, end, colorscr, colorbgd, answer):
    """Sprawdza czy metoda prawidłowo wskazuje przecięte linie o zadanych kolorach"""
    screen = pygame.image.load(os.path.join(sys.path[0], 'poziome.png'))
    background = pygame.image.load(os.path.join(sys.path[0], 'pionowe.png'))
    assert check_crossing_lines(screen, background, begin, end, colorscr, colorbgd) == answer