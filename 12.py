# Escribir un algoritmo que calcule y realice un porcentaje de descuento al precio de un artículo.  El usuario debe ingresar ambos datos por teclado. Mostrar por pantalla el nuevo precio con el descuento.

def descuento():
    precio = float(input('Ingrese el valor del producto: '))
    descuento = float(input('Ingrese el descuento a aplicar: '))
    precio_final = precio - (precio * (descuento / 100))
    print(f'El precio final a pagar es de ${precio_final:.2f}')
descuento()
    