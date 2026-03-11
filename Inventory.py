# Programa to register a product in an inventory



# Ask for the product name

name = input("Enter the product name: ")

# Validate "the Price"

while True:
    try:
        price = float(input("Enter the product price: "))
        break
    except ValueError:
        print("Invalid value. Please enter a valid number for the price.")

# Validate "the Quantity"

while True:
    try:
        quantity = int(input("Enter the product quantity: "))
        break
    except ValueError:
        print("Invalid value. Please enter a valid enter for the quantity.")