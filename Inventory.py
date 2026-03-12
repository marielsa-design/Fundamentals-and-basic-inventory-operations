# Programa para registrar un producto en un inventario.

# Datos de inventario

producto = ["vacio"] * 5

print("Inventario de productos")

while True:
    
    print("\nMenu")
    print("1. Agregar producto.")
    print("2. Ver los productos.")
    print("3. Actualizar los productos.")
    print("4. Eliminar producto.")
    print("5. Salir")
    opcion = int(input("Escoge una opcion: "))

    try:
        opcion = int(input("Escoge una opcion: "))
    except ValueError:
        print("Ingrese un numero valido")
        continue


    match opcion:

        # Agregar producto
        case 1:
            if producto.count("vacio") > 0:

                new_producto = input("Ingresa el nombre del producto\n").upper()
                
                if new_producto in producto:
                    print("Ese producto ya existe")
                
                else:
                    index = producto.index("vacio")
                    producto[index] = new_producto
                    print(f"Producto '{new_producto}' agregado correctamente")
            else:
                print("El inventario está lleno")
        #Ver inventario
        
        case 2:
            remove = input("Ingresa el nombre del producto a eliminar\n").upper()
            if remove in producto:
                index = producto.index(remove)
                producto[index] = "vacio"
                print(f"Producto '{remove}' eliminado correctamente")
            else:
                print("Producto no encontrado")

        case 3:
            print("nventario actual:")
            for i, objeto in enumerate(producto):
                print(f" Espacio {i+1}: {objeto}")

        case 4:
            print("¡Adiós!")
            break

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

# Calcular costo total

costo_total = precio * cantidad

# Mostrar resultados

print("producto", nombre, "| precio:", precio, "| cantidad:" , cantidad, " | Total:" , costo_total)