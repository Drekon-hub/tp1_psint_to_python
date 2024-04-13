# Se necesita sumar dos números leídos desde el teclado (los ingresa el usuario) y mostrar el resultado por pantalla.

def suma():
    a = int(input('Ingrese el primer numero: '))
    b = int(input('Ingrese el segundo numero: '))
    r = a + b
    print(f'El resultado de la suma es {r}')

suma()