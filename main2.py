inventory = 5
product = ["vacio"] * inventory

option = 1
print("Bienvenido al Sistema de Inventario")

while True:
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Ver productos")
    print("4. Salir")

    try:
        option = int(input("Elige una opción: "))
    except ValueError:
        print("Por favor ingresa un número válido.")
        continue

    match option:
        case 1:
            if product.count("vacio") > 0:
                new_product = input("Ingresa el nombre del producto\n").upper()
                if new_product in product:
                    print("Ese producto ya existe")
                else:
                    index = product.index("vacio")
                    product[index] = new_product
                    print(f"Producto '{new_product}' agregado correctamente")
            else:
                print("El inventario está lleno")

        case 2:
            remove = input("Ingresa el nombre del producto a eliminar\n").upper()
            if remove in product:
                index = product.index(remove)
                product[index] = "vacio"
                print(f"Producto '{remove}' eliminado correctamente")
            else:
                print("Producto no encontrado")

        case 3:
            print("\nInventario actual:")
            for i, item in enumerate(product):
                print(f" Espacio {i+1}: {item}")

        case 4:
            print("¡Adiós!")
            break

        case _:
            print("Opción inválida. Por favor elige entre 1 y 4")