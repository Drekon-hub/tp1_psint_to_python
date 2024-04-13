# Un supermercado ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra.

def descuento():
    v = float(input('Ingrese el valor del producto: '))
    d = v * 0.85
    print(f'El total a pagar con el descuento del 15% aplicado es de ${d}')
    
descuento()