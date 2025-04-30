import abc
import math
import random

# a) Interfaz Coloreado
class Coloreado(abc.ABC):
    @abc.abstractmethod
    def comoColorear(self):
        pass

# b) Clase abstracta Figura
class Figura(abc.ABC):
    def __init__(self, color="negro"):
        self.color = color
    
    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def __str__(self):
        return f"Figura de color {self.color}"
    
    @abc.abstractmethod
    def area(self):
        pass
    
    @abc.abstractmethod
    def perimetro(self):
        pass

# c) Clase Cuadrado
class Cuadrado(Figura, Coloreado):
    def __init__(self, lado, color="negro"):
        super().__init__(color)
        self.lado = lado
    
    def area(self):
        return self.lado ** 2
    
    def perimetro(self):
        return 4 * self.lado
    
    def comoColorear(self):
        return "Colorear los cuatro lados"
    
    def __str__(self):
        return f"Cuadrado de lado {self.lado}, color {self.color}"

# d) Clase Circulo
class Circulo(Figura):
    def __init__(self, radio, color="negro"):
        super().__init__(color)
        self.radio = radio
    
    def area(self):
        return math.pi * (self.radio ** 2)
    
    def perimetro(self):
        return 2 * math.pi * self.radio
    
    def __str__(self):
        return f"Círculo de radio {self.radio}, color {self.color}"

# f) Programa de prueba
def main():
    figuras = []
    
    # Crear 5 figuras aleatorias
    for i in range(5):
        tipo = random.randint(1, 2)
        
        if tipo == 1:  # Cuadrado
            lado = random.uniform(1.0, 10.0)
            figuras.append(Cuadrado(lado))
        else:  # Circulo
            radio = random.uniform(1.0, 10.0)
            figuras.append(Circulo(radio))
    
    # Mostrar información de cada figura
    for i, figura in enumerate(figuras, 1):
        print(f"\nFigura {i}: {figura}")
        print(f"Área: {figura.area():.2f}")
        print(f"Perímetro: {figura.perimetro():.2f}")
        
        # Verificar si tiene el método comoColorear
        if isinstance(figura, Coloreado):
            print(f"Método colorear: {figura.comoColorear()}")
        else:
            print("Esta figura no implementa cómo colorearse")

if __name__ == "__main__":
    main()
