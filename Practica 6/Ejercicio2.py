import math

class AlgebraVectorial3D:
    def __init__(self, vector_a, vector_b):
        self.vector_a = vector_a
        self.vector_b = vector_b

    def suma_vectores(self):
        return [a + b for a, b in zip(self.vector_a, self.vector_b)]

    def producto_escalar(self):
        return sum(a * b for a, b in zip(self.vector_a, self.vector_b))

    def producto_cruz(self):
        x1, y1, z1 = self.vector_a
        x2, y2, z2 = self.vector_b
        return [
            y1 * z2 - z1 * y2,
            z1 * x2 - x1 * z2,
            x1 * y2 - y1 * x2
        ]

    def magnitud_vector(self, vector):
        return math.sqrt(sum(coord ** 2 for coord in vector))

# Ejemplo de uso
vector_a = [1, 2, 3]
vector_b = [4, 5, 6]

algebra = AlgebraVectorial3D(vector_a, vector_b)
print("Suma de los vectores:", algebra.suma_vectores())
print("Producto escalar:", algebra.producto_escalar())
print("Producto cruz:", algebra.producto_cruz())
print("Magnitud de A:", algebra.magnitud_vector(vector_a))
print("Magnitud de B:", algebra.magnitud_vector(vector_b))
