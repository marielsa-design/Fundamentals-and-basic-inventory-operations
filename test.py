# Programa para registrar un producto en un inventario.


# Solicitar el nombre de producto

nombre = input("Ingresar el nombre del producto: ")

# Validar «el precio»

while True:
    try:
        precio = float(input("Ingresar el precio de producto: "))
        break
    except ValueError:
        print("Valor no válido. Ingresar un número válido para el precio.")

# Validar «la cantidad»

while True:
    try:
        cantidad = int(input("Ingresar la cantidad de producto: "))
        break
    except ValueError:
        print("Valor no válido. Introduzca un valor válido para la cantidad.")

##################################################################################