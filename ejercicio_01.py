#RETO,cliente solicita un programa donde ingrese el precio de un producto, y la cantidad
#y que el programa devuelva un subtotal aplique descuento si amerita y marque el total

Precio = 50

def calcular_subtotal(cantidad):
    return cantidad * 50

def calcular_descuento(subtotal):
    return subtotal_acomulado * 0.25

subtotal_acomulado = 0

while True:
    cantidad = int(input("cuantos quiere? "))

    subtotal_acomulado += calcular_subtotal(cantidad)

    respuesta = input("Desea agregar mas productos.? s/n ") 
    if respuesta == 'n':
        break

if subtotal_acomulado >=100:
    descuento = calcular_descuento(cantidad)
    print("se aplico un descuento del 25%")
else:
    descuento = 0
    print("No se aplico descuento")

total = subtotal_acomulado - descuento
impuestos = total * 0.15

print(f"subtotal es : $ {subtotal_acomulado}")
print(f"descuento es : $ {descuento}")
print(f"total a pagar es : $ {total}")
print(f"pago de impuestos : $ {impuestos}")

