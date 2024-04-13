# Escribir un algoritmo que calcule la edad de una persona.

def edad():
    n = int(input('Ingrese el ano que naciste: '))
    a = int(input('Ingrese el ano acutal: '))
    r = a - n
    print(f'Tu edad es {r}')

edad()