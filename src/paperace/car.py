from paperace.const import WIDTH, HEIGHT


class Car:
    """Obiekt car reprezentujący pojazd gracza.
    Funkcje: get_allowed_positions, move
    Atrybuty: xpos, ypos, xv, yv, color"""
    def __init__(self, xpos, ypos, color):
        self.xpos = xpos
        self.ypos = ypos
        self.xv = 0
        self.yv = 0
        self.color = color

    def get_allowed_positions(self):
        """Zwraca listę wszystkich 9-ciu punktów (lub mniej), na jakie może się
        przesunąć pojazd"""
        pos = []
        for y in [-20, 0, 20]:
            for x in [-20, 0, 20]:
                cx = self.xpos+self.xv+x
                cy = self.ypos+self.yv+y
                if cx >= 0 and cx <= WIDTH and cy >= 0 and cy <= HEIGHT:
                    pos.append(tuple((cx, cy)))
        return pos

    def move(self, destination):
        """Przesuwa pojazd gracza na zadaną pozycję (destination). Modyfikuje
        wektor prędkości."""
        self.xv = destination[0] - self.xpos
        self.yv = destination[1] - self.ypos
        self.xpos = destination[0]
        self.ypos = destination[1]
