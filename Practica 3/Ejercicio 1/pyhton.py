class Pila:
    def __init__(self, n):
        self.arreglo = [None] * n  # Inicializar con espacio fijo
        self.top = -1  # Indica que la pila está vacía
        self.n = n  # Capacidad de la pila

    def push(self, e):
        if self.isFull():
            raise Exception("La pila está llena")
        self.top += 1
        self.arreglo[self.top] = e

    def pop(self):
        if self.isEmpty():
            raise Exception("La pila está vacía")
        elemento = self.arreglo[self.top]
        self.top -= 1
        return elemento

    def peek(self):
        if self.isEmpty():
            raise Exception("La pila está vacía")
        return self.arreglo[self.top]

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.n - 1


# Ejemplo de uso
pila = Pila(5)
pila.push(10)
pila.push(20)
print("Elemento superior:", pila.peek())  # Debe imprimir 20
print("Elemento eliminado:", pila.pop())  # Debe imprimir 20
print("¿La pila está vacía?", pila.isEmpty())  # Debe ser False
