class Cola:
    def __init__(self, n):
        self.arreglo = [None] * n  # Inicializamos con un espacio fijo
        self.inicio = 0  # Índice del frente de la cola
        self.fin = -1  # Índice del final de la cola
        self.n = n  # Capacidad de la cola
        self.size = 0  # Tamaño actual de la cola

    def insertar(self, e):
        if self.esta_llena():
            raise Exception("La cola está llena")
        self.fin = (self.fin + 1) % self.n  # Movimiento circular
        self.arreglo[self.fin] = e
        self.size += 1

    def eliminar(self):
        if self.esta_vacia():
            raise Exception("La cola está vacía")
        elemento = self.arreglo[self.inicio]
        self.inicio = (self.inicio + 1) % self.n  # Movimiento circular
        self.size -= 1
        return elemento

    def frente(self):
        if self.esta_vacia():
            raise Exception("La cola está vacía")
        return self.arreglo[self.inicio]

    def esta_vacia(self):
        return self.size == 0

    def esta_llena(self):
        return self.size == self.n


# Ejemplo de uso
cola = Cola(5)
cola.insertar(10)
cola.insertar(20)
print("Elemento al frente:", cola.frente())  # Imprime 10
print("Elemento eliminado:", cola.eliminar())  # Imprime 10
print("¿La cola está vacía?", cola.esta_vacia())  # Debe ser False
