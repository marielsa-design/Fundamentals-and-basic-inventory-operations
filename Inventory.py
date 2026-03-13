# Programa para registrar un producto en un inventario.

# Solicitar el nombre del producto
nombre = input("Ingresar el nombre del producto: ")

# Validar el precio
while True:
    try:
        precio = float(input("Ingresar el precio del producto: "))
        break
    except ValueError:
        print("Valor no válido. Ingrese un número válido para el precio.")

# Validar la cantidad
while True:
    try:
        cantidad = int(input("Ingresar la cantidad del producto: "))
        break
    except ValueError:
        print("Valor no válido. Ingrese un número entero válido para la cantidad.")

# Calcular costo total
costo_total = precio * cantidad

# Mostrar resultados
print("Resumen del producto registrado:")
print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")

# Este programa solicita al usuario el nombre, precio y cantidad de un producto.
# Luego calcula el costo total multiplicando el precio por la cantidad
# y muestra el resultado en la consola.