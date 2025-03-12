import math
def calcular_area(*args):
    if len(args) == 1:  # Círculo
        radio = args[0]
        return math.pi * radio ** 2
    elif len(args) == 2:  # Rectángulo
        base, altura = args
        return base * altura
    elif len(args) == 3:  # Triángulo rectángulo
        base, altura, _ = args
        return (base * altura) / 2
    elif len(args) == 4:  # Trapecio
        base_mayor, base_menor, altura, _ = args
        return ((base_mayor + base_menor) * altura) / 2
    elif len(args) == 5:  # Pentágono 
        lado, apotema, _, _, _ = args
        return (5 * lado * apotema) / 2
    else:
        return "Parámetros inválidos"
print(calcular_area(5)) 
print(calcular_area(4, 6))  
print(calcular_area(3, 4, 0))  
print(calcular_area(6, 4, 5, 0))  
print(calcular_area(4, 3, 0, 0, 0))
