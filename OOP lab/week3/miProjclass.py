import os

data = []  # declaring an array to store packed data


class product():  # declaring a class
    name = ""
    price = 0
    category = ""
    stock = 0
    minimum = 0


def showHeader():  # shows main Heading
    print(" ***********************************")
    print("      STORE MANAGEMENT SYSTEM       ")
    print(" ***********************************")


def showMenu():  # shows main menu
    print("1: Add product")
    print("2: View all products")
    print("3: Find product with highest price")
    print("4: View sales tax of all products")
    print("5: Products to be ordered")
    print("6: Sold a product")
    print("7: Exit")
    print(" ")
    option = int(input("Enter your option: "))
    return option


def showSubheader(heading):  # shows required heading
    print(" ")
    if heading == 1:
        print("Add new product")
    if heading == 2:
        print("View all products")
    if heading == 3:
        print("Highest priced products")
    if heading == 4:
        print("Sales tax")
    if heading == 5:
        print("Products to be ordered")
    if heading == 6:
        print("Sell a product")
    print("--------------------------")


def addProduct():
    p = product()  # calls the class
    p.name = input("Enter name of product: ")
    p.price = int(input("Enter price of product: "))
    p.category = input("Enter category of product: ")
    p.stock = int(input("Enter available stock: "))
    p.minimum = int(input("Enter minimum stock: "))
    data.append(p)  # puts all data in data list


def viewProducts(data):
    print("Product", "\t", "\t", "Category", "\t",
          "Price", "\t", "Stock", "\t", "Minimum")
    print("----------------------------------------------------------------")
    for i in data:
        print(i.name, "\t", "\t", "\t", i.category, "\t",
              i.price, "\t", i.stock, "\t", i.minimum)


def getHighPriceProduct(data):
    largest = -9999999
    idx = 0
    for i in data:
        if i.price > largest:
            largest = i.price  # stores the entity with greatest price
            idx = i  # stores the index of entity with largest price
    print(idx.name, "\t", idx.price)


def calculateTax(data):
    print("Product", "\t", "\t", "Category", "\t", "Price", "\t", "Tax")
    print("-----------------------------------------------")
    for i in data:
        if i.category == "grocery":
            print(i.name, "\t", "\t", i.category, "\t",
                  i.price, "\t", i.price+(i.price*0.1))
        elif i.category == "fruit":
            print(i.name, "\t", "\t", i.category, "\t",
                  i.price, "\t", i.price+(i.price*0.05))


def productsToBeOrdered(data):
    print("Product", "\t", "Category", "\t", "\t", "Stock", "\t", "Minimum")
    print("----------------------------------------------------------------")
    for i in data:
        if i.stock < i.minimum:  # compares available stock with minimum stock
            print(i.name, "\t", i.category, "\t",
                  "\t", i.stock, "\t", i.minimum)


def sellProduct(data):
    viewProducts(data)  # shows user how much products are available
    product = input("Enter your product to buy: ")
    qty = int(input("Enter your quantity: "))
    alpha = 0
    beta = 0
    for i in data:
        if i.name == product and i.stock >= qty:
            alpha = i.stock  # storing number of stock in a variable
            beta = alpha-qty  # subtracting entered quantity from available
            i.stock = beta  # replacing new stock in original place


def drivercode():
    option = 0
    while option != 7:  # option 7 means exit
        os.system("cls")  # clears screen
        option = showMenu()  # shows menu
        if option == 1:
            os.system("cls")
            showHeader()
            showSubheader(option)
            addProduct()
            ch = input("press enter to continue...")
        elif option == 2:
            os.system("cls")
            showHeader()
            showSubheader(option)
            viewProducts(data)
            ch = input("press enter to continue...")
        elif option == 3:
            os.system("cls")
            showHeader()
            showSubheader(option)
            getHighPriceProduct(data)
            ch = input("press enter to continue...")
        elif option == 4:
            os.system("cls")
            showHeader()
            showSubheader(option)
            calculateTax(data)
            ch = input("press enter to continue...")
        elif option == 5:
            os.system("cls")
            showHeader()
            showSubheader(option)
            productsToBeOrdered(data)
            ch = input("press enter to continue...")
        elif option == 6:
            os.system("cls")
            showHeader()
            showSubheader(option)
            sellProduct(data)
            ch = input("press enter to continue...")


drivercode()
