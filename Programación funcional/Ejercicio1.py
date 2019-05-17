# Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio.
# Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta

def descuento (precio, porcentaje):
    return precio - precio * porcentaje/100

def iva (precio, porcentaje):
    return precio  + precio * porcentaje/100

def aplica(cesta, funcion):
    total = 0
    for precio, porcentaje in cesta.items():
        total += funcion(precio, porcentaje)
    return total

print ('El precio tras aplicar descuentos es:', aplica({1000:20, 500:10, 100:1}, descuento))
print ('El precio tras aplicar iva es:', aplica({1000:20, 500:10, 100:1}, iva))
