inventory = 5
product = [ "empty"] * inventory

option = 1
print("Welcome to the Inventory System")

while True:
    print("1. Add item")
    print("2. Remove item")
    print("3. View products")
    print("4. Exit")

    try:
        option = int(input("Choose an option: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    match option:
        case 1:
            if product.count("empty") > 0:
                new_product = input("Enter the product name\n").upper()
                if new_product in product:
                    print("That product alreday exists")
                else:
                    index = product.index("empty")
                    product[index] = new_product
                    print(f"Product '{new_product}' added successfully")
            else:
                print("Inventory is full")

        case 2:
            remove = input("Enter the product name to remove\n").upper()
            if remove in product:
                index = product.index(remove)
                product[index] = "empty"
                print(f"Product '{remove}' removed successfully")
            else:
                print("Product not found")

        case 3:
            print("\ncurrent inventory:")
            for i, item in enumerate(product):
                print(f" slot {i+1}: {item}")

        case 4:
            print("Goodbye!")
            break

        case _:
            print("Invalid option. Please choose between 1 and 4")