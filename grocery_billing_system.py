print("-------------RELIANCE FRESH--------------")

name = input("Enter your name: ")
contact_number = input("Enter your contact number: ")


cart = []
while True:

    print("\n1. Add Product")
    print("2. View Cart")
    print("3. Checkout")
    print("4. Exit")

    choice= input("Enter your choice (1-4): ")
    
    if choice=='1':
        product_name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per unit: "))
        cart.append((product_name, quantity, price))
        print("Product added to cart successfully!")
    elif choice=='2':
        if not cart:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            for product in cart:
                name, qty, prc = product
                print(f"- {name}: {qty} x ${prc:.2f} = ${qty * prc:.2f}")

    elif choice=='3':
        if not cart:
            print("Your cart is empty. Please add products before checkout.")
        else:
            total_amount = sum(qty * prc for _, qty, prc in cart)
            print(f"Total amount: ${total_amount:.2f}")
            print("Thank you for shopping with us!")
            break
    elif choice=='4':
        print("Thank you for visiting Reliance Fresh!")
        break
    else:
        print("Invalid choice. Please try again.")
