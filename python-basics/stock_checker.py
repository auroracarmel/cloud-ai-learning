try:
    laptops = int(input("How many laptops are in stock? "))

    if laptops < 3:
        print("Low stock")
    else:
        print("Stock available")

except ValueError:
    print("Please enter a whole number, such as 12.")