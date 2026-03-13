# Datos de inventario

producto = ["vacio"] * 5

print("Inventario de productos")

while True:
    
    print("Menu")
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