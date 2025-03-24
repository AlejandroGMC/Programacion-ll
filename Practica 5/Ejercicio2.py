import math

def promedio(numeros):
    return sum(numeros) / len(numeros)

def desviacion(numeros, media):
    suma_cuadrados = sum((x - media) ** 2 for x in numeros)
    return math.sqrt(suma_cuadrados / (len(numeros) - 1))

def calcular_estadisticas():
    numeros = list(map(float, input("Ingrese 10 números: ").split()))
    media = promedio(numeros)
    desviacion_std = desviacion(numeros, media)
    print(f"El promedio es {media:.2f}")
    print(f"La desviación estándar es {desviacion_std:.5f}")

# Ejecutar el programa 
calcular_estadisticas()
