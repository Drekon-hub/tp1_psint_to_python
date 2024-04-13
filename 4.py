# Se necesita saber el perímetro de un triángulo equilátero del cual se desconoce el valor de su lado.

def perimetro():
    l = float(input('Ingresa la longitud del lado del triángulo equilátero en centímetros: '))
    r = 3 * l
    print(f'El perimetro del triangulo equilatero es de {r} cm')

perimetro()