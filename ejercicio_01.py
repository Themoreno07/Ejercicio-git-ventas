#RETO,cliente solicita un programa donde ingrese el precio de un producto, y la cantidad
#y que el programa devuelva un subtotal aplique descuento si amerita y marque el total

Precio = 50
cantidad = int(input("cuantos quiere? "))

def calcular_subtotal(cantidad):
    return cantidad * 50

subtotal = calcular_subtotal(cantidad)

def calcular_descuento(subtotal):
    return subtotal * 0.10

if subtotal >=100:
    descuento = calcular_descuento(subtotal)
    print("se aplico un descuento del 10%")
else:
    descuento = 0
    print("No se aplico descuento")

total = subtotal - descuento
impuestos = total * 0.15
print(f"subtotal es : $ {subtotal}")
print(f"descuento es : $ {descuento}")
print(f"total a pagar es : $ {total}")
print(f"pago de impuestos : $ {impuestos}")
