# Se necesita un programa que calcule el área de cualquier triángulo conociendo su base y altura.

def area():
    b = float(input('Ingrese la base de su triangulo: '))
    h = float(input('Ingrese la altura de su triangulo: '))
    r = b * h
    print(f'El area del triangulo es {r}')

area()