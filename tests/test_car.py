import pytest
from paperace.car import Car
from paperace.const import BLACK

def test_car_init():
    """Sprawdzenie, czy objekt Car jest prawidłowo inicjalizowany"""
    car = Car(60, 60, BLACK)
    assert car.xpos == 60
    assert car.ypos == 60
    assert car.xv == 0
    assert car.yv == 0
    assert car.color == BLACK

def test_car_move():
    """Sprawdzanie czy pojazd porusza się prawidłowo w dwóch kierunkach"""
    car = Car(60, 60, BLACK)
    car.move((80, 80))
    assert car.xpos == 80
    assert car.ypos == 80
    assert car.xv == 20
    assert car.yv == 20
    car.move((60, 60))
    assert car.xpos == 60
    assert car.ypos == 60
    assert car.xv == -20
    assert car.yv == -20
