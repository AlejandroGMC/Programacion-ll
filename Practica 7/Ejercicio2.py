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

    def validaNumero(self, numero):
        return 0 <= numero <= 10

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

            if not self.validaNumero(entrada):
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


class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if 0 <= numero <= 10:
            if numero % 2 == 0:
                return True
            else:
                print("Error: el número debe ser PAR.")
                return False
        else:
            print("Error: el número debe estar entre 0 y 10.")
            return False


class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if 0 <= numero <= 10:
            if numero % 2 != 0:
                return True
            else:
                print("Error: el número debe ser IMPAR.")
                return False
        else:
            print("Error: el número debe estar entre 0 y 10.")
            return False


class Aplicacion:
    @staticmethod
    def main():
        print("\n--- Juego Adivina Número ---")
        juego = JuegoAdivinaNumero(3)
        juego.juega()

        print("\n--- Juego Adivina Número PAR ---")
        juegoPar = JuegoAdivinaPar(3)
        juegoPar.juega()

        print("\n--- Juego Adivina Número IMPAR ---")
        juegoImpar = JuegoAdivinaImpar(3)
        juegoImpar.juega()


# Solo ejecutar si es el archivo principal
if __name__ == "__main__":
    Aplicacion.main()
