# Desarrolle un algoritmo que resuelva y calcule el área y perímetro de un rectángulo y nos muestre el resultado por pantalla.

def area_perimetro_reactangulo():
    b = float(input('Ingrese la base del rectangulo: '))
    h = float(input('Ingrese la altura del rectangulo: '))
    a = b * h
    p = 2 * (b + h)
    print(f'El area del rectangulo es {a} y el perimetro es {p}')
    
area_perimetro_reactangulo()