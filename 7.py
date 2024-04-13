# Desarrolle un algoritmo que calcule la suma de dos fracciones.

def suma_fracciones():
    f1u = int(input('Ingrese el numero de arriba de la primera fraccion: '))
    f1d = int(input('Ingrese el numero de abajo de la primera fraccion: '))
    f2u = int(input('Ingrese el numero de arriba de la primera fraccion: '))
    f2d = int(input('Ingrese el numero de abajo de la primera fraccion: '))
    
    nfu = (f1u * f2d) + (f1d * f2u)
    nfd = (f1d * f2d)
    print(f'El resutaldo es {nfu}/{nfd}')
suma_fracciones()