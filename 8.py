# Desarrolle un algoritmo que resuelva y calcule el área de un círculo. Luego debe mostrar el resultado por pantalla.

def area_circulo():
    r = float(input('Ingresa el r del circulo: '))
    result = 3.1415 * r ** 2 #el doble asterisco significa que estoy elevando al cuadrado
    print(f'El area del circulo es {result:.2f}')

area_circulo()