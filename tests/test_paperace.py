import pytest
from paperace.__main__ import get_nearest_point

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