inventario = 5
producto = ["vacio"] * inventario

option = 1
print("Bienvenido al Sistema de Inventario")

while True:
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Ver productos")
    print("4. Salir")

    try:
        opcion = int(input("Elige una opción: "))
    except ValueError:
        print("Por favor ingresa un número válido.")
        continue

    match opcion:
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

        case _:
            print("Opción inválida. Por favor elige entre 1 y 4")