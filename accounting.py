account = {"balance": 0}
warehouse_status = {}
product_list = {}
acc_review = {}
balance = 0
sale = 0
purchase = 0
product_name = ""

operations = []

while True:
    print("Please enter your command: balance/ sale/ purchase/ account/ list/ warehouse/ review/ end")
    command = input()

    if command == "balance":
        product_quantity = int(input("Enter quantity of item to add/ subtract:"))
        account["balance"] += product_quantity
        operations.append(f"added/subtracted balance: product_quantity")
        print("Added/ Subtracted balance", account["balance"])
    elif command == "sale":
        product_name = input("Enter the product name: A/ B/ C/ D:")
        price = float(input("Enter the selling price:"))
        quantity = int(input("Enter the quantity sold:"))

        if product_name in warehouse_status:
            product = warehouse_status[product_name]
            if product["quantity"] >= quantity:
                total_price = quantity * price
                account["balance"] -= total_price
                product["quantity"] -= quantity
                operations.append(f"Sale:{quantity}{product_name} at {price} ")
                print("Sale recorded")
            else:
                print("Insufficient stock.")

        else:
            print("Product not found.")

    elif command == "purchase":
        product_name = input("Enter product name: A/ B/ C/ D")
        price = float(input("Enter purchasing price"))
        quantity = int(input("Enter the quantity purchased"))

        if price < 0 or quantity < 0:
            print("Invalid input.")
            continue

        total_price = price * quantity
        if account["balance"] >= total_price:
            account["balance"] -= total_price
            if product_name in warehouse_status:
                warehouse_status[product_name] += quantity
            else:
                warehouse_status[product_name] = {"price": price, "quantity": quantity}
            operations.append(f"Purchase: {quantity} {product_name} at {price}")
            print("Purchase recorded.")

        else:
            print("Insufficient fund, transaction failed, order cancelled.")
            continue

    elif command == "account":
        for index, product_name in enumerate(account):
            print(f"Current account balance is\n{index}: {product_name}, ${account['balance']}")

    elif command == "list":
        if len(warehouse_status) == 0:
            print("Empty stock")
        else:
            print("Warehouse status:")
            for product_name, product in warehouse_status.items():
                print("\nProduct:", product_name)
                print("\n Price: $", product['price]'])
                print("Quantity:", product['quantity'])
    elif command == "warehouse":
        item_check = input("Enter the product name:")
        product = warehouse_status[product_name]
        if item_check in warehouse_status:
            item_check = warehouse_status[item_check]
            print("Product:", item_check)
            print("\n Price: $", product['price'])
            print("\n Quantity:", product['quantity'])

        else:
            print("Product not found")

    elif command == "end":
        break

    else:
        print("Error message.")

print("Program terminated.")
