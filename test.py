# Programa para registrar un producto en un inventario.


# Solicitar el nombre de producto
print("# * 25")
nombre = input("Ingrese el nombre del producto: ")
print("# * 25")
# Solicitar y validar de "el precio"

while True:
    try:
        precio = float(input("Ingresar el precio de producto: "))
        break
    except ValueError:
        print("Valor no válido. Ingresar un número válido para el precio.")

# Solicitar y validar de "la cantidad"

while True:
    try:
        cantidad = int(input("Ingresar la cantidad de producto: "))
        break
    except ValueError:
        print("Valor no válido. Introduzca un valor válido para la cantidad.")

# Calcular costo total (Operación matemática)

costo_total = precio * cantidad

