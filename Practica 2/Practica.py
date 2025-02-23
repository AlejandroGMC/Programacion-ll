import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coord_cartesianas(self):
        return self.x, self.y

    def coord_polares(self):
        r = math.sqrt(self.x ** 2 + self.y ** 2)
        theta = math.atan2(self.y, self.x)
        return r, math.degrees(theta)

    def __str__(self):
        return f"Punto({self.x}, {self.y})"

class Linea:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"Linea desde {self.p1} hasta {self.p2}"

    def dibujaLinea(self):
        print(self)

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def __str__(self):
        return f"Circulo con centro en {self.centro} y radio de {self.radio:.2f}"

    def dibujaCirculo(self):
        print(self)

if __name__ == "__main__":
    p1 = Punto(0, 3)
    p2 = Punto(3, 4)
    print(p1)
    print("Coordenadas Cartesianas:", p1.coord_cartesianas())
    print("Coordenadas Polares:", p1.coord_polares())

    linea = Linea(p1, p2)
    linea.dibujaLinea()

    circulo = Circulo(p1, 5)
    circulo.dibujaCirculo()
