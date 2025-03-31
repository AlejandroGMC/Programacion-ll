import math

class AlgebraVectorial:
    def __init__(self, vector_a, vector_b):
        self.vector_a = vector_a
        self.vector_b = vector_b

    def son_perpendiculares(self):
        producto_punto = sum(a * b for a, b in zip(self.vector_a, self.vector_b))
        return producto_punto == 0

    def son_paralelos(self):
        factor = [a / b if b != 0 else None for a, b in zip(self.vector_a, self.vector_b)]
        return len(set(factor)) == 1

    def proyeccion(self):
        producto_punto = sum(a * b for a, b in zip(self.vector_a, self.vector_b))
        magnitud_b = sum(b ** 2 for b in self.vector_b)
        escalar = producto_punto / magnitud_b
        return [escalar * b for b in self.vector_b]

    def componente(self):
        producto_punto = sum(a * b for a, b in zip(self.vector_a, self.vector_b))
        magnitud_b = math.sqrt(sum(b ** 2 for b in self.vector_b))
        return producto_punto / magnitud_b

# Ejemplo de uso
vector_a = [3, 4]
vector_b = [4, -3]

algebra = AlgebraVectorial(vector_a, vector_b)
print("¿Son perpendiculares?", algebra.son_perpendiculares())
print("¿Son paralelos?", algebra.son_paralelos())
print("Proyección de A sobre B:", algebra.proyeccion())
print("Componente de A en dirección de B:", algebra.componente())
