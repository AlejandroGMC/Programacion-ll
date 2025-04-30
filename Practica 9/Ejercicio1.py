class Boleto:
    def __init__(self, numero):
        self.numero = numero
    
    def __str__(self):
        return f"Número: {self.numero}, Precio: {self.precio:.1f}"


class Palco(Boleto):
    def __init__(self, numero):
        super().__init__(numero)
        self.precio = 100.0
    
    def __str__(self):
        return super().__str__()


class Platea(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        self.dias_anticipacion = dias_anticipacion
        self.precio = 50.0 if dias_anticipacion >= 10 else 60.0
    
    def __str__(self):
        return super().__str__()


class Galeria(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        self.dias_anticipacion = dias_anticipacion
        # El precio es el 50% del costo de palco (100) con diferentes valores según días
        self.precio = 25.0 if dias_anticipacion >= 10 else 30.0
    
    def __str__(self):
        return super().__str__()


# Ejemplo de uso del sistema
def main():
    print("Sistema de Boletos del Teatro Municipal")
    print("--------------------------------------")
    
    # Crear algunos boletos de ejemplo
    boleto_palco = Palco(1)
    boleto_platea1 = Platea(2, 15)  # Comprado con 15 días de anticipación
    boleto_platea2 = Platea(3, 5)   # Comprado con 5 días de anticipación
    boleto_galeria1 = Galeria(4, 12) # Comprado con 12 días de anticipación
    boleto_galeria2 = Galeria(5, 8)  # Comprado con 8 días de anticipación
    
    # Mostrar la información de los boletos
    print(boleto_palco)
    print(boleto_platea1)
    print(boleto_platea2)
    print(boleto_galeria1)
    print(boleto_galeria2)


if __name__ == "__main__":
    main()
