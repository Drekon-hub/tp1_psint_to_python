# Se necesita saber el perímetro de un cuadrado cuyo lado lo ingresa el usuario.

def perimetro():
    lado = float(input('Ingrese la longitud del lado en cm: '))
    r = lado * 4
    print(f'El perimetro del cuadrado es {r}cm')

perimetro()