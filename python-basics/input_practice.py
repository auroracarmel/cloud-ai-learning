try:
    laptops = int(input("How many laptops are in stock? "))
    print("You entered:", laptops)
except ValueError:
    print("Please enter a whole number, such as 12.")