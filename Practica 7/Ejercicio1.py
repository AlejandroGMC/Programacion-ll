import random

class Juego:
    def __init__(self, numeroDeVidas):
        self.numeroDeVidas = numeroDeVidas
        self.record = 0

    def reiniciaPartida(self):
        self.numeroDeVidas = 3
        print("\nSe reinició la partida.")

    def actualizaRecord(self):
        self.record += 1
        print(f"¡Nuevo récord! Total de partidas ganadas: {self.record}")

    def quitaVida(self):
        self.numeroDeVidas -= 1
        print(f"Vidas restantes: {self.numeroDeVidas}")
        return self.numeroDeVidas > 0


class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = 0

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        print("\n--- Adivina el número entre 0 y 10 ---")

        while True:
            try:
                entrada = int(input("Ingresa tu número: "))
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue

            if entrada == self.numeroAAdivinar:
                print("¡Acertaste!")
                self.actualizaRecord()
                break
            else:
                if self.numeroAAdivinar > entrada:
                    print("El número a adivinar es mayor.")
                else:
                    print("El número a adivinar es menor.")

                if not self.quitaVida():
                    print(f"¡Perdiste! El número era {self.numeroAAdivinar}.")
                    break


class Aplicacion:
    @staticmethod
    def main():
        print("\n--- Juego Adivina Número ---")
        juego = JuegoAdivinaNumero(3)
        juego.juega()


# Solo ejecutar si es el archivo principal
if __name__ == "__main__":
    Aplicacion.main()
