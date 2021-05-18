#one problem: program wont run correctly if only one type(grocery,fruit) is entered.Both are compulsory!
import os
option = 0
counter = 0
counter2 = 0
prod = " "
grocery = []
fruits = []
grocery_price = []
grocery_stock = []
grocery_minimum = []
fruit_price = []
fruit_stock = []
fruit_minimum = []

def showHeader():       #shows main Heading
    print(" ***********************************")
    print("      STORE MANAGEMENT SYSTEM       ")
    print(" ***********************************")

def showMenu():     #shows main menu
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

def showSubheader(heading):     #shows required heading
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

def addProductUI():
    global prod
    global grocery
    global fruits
    name = input("Enter product name: ")
    prod = input("Enter type of product (grocery/fruit):")
    if prod == "grocery":
        grocery.append(name)        #adds element in list
    elif prod == "fruit":
        fruits.append(name)     #adds elements in list

def addProduct():
    global counter
    global counter2
    global grocery_price
    global grocery_stock
    global grocery_minimum
    global fruit_price
    global fruit_stock
    global fruit_minimum

    price = int(input("Enter product price: "))
    stock = int(input("Enter product stock: "))
    minimum = int(input("Enter minimum stock: "))
    if prod == "grocery":
        grocery_price.append(price)
        grocery_stock.append(stock)
        grocery_minimum.append(minimum)
        counter = counter+1         #counts number of elemnts in grocery list
    elif prod == "fruit":
        fruit_price.append(price)
        fruit_stock.append(stock)
        fruit_minimum.append(minimum)
        counter2 = counter2+1       #counts number of elements in fruits list
    ch = input("press enter to continue...")

def viewProducts():
    print("Product", "\t", "Category", "\t",
          "Price", "\t", "Stock", "\t", "Minimum")
    print("----------------------------------------------------------------")
    for i in range(0, counter):
        print(*grocery[i], "\t", "\t", "grocery", "\t", *str(grocery_price[i]),
              "\t", *str(grocery_stock[i]), "\t", *str(grocery_minimum[i]))
    for i in range(0, counter2):
        print(*fruits[i], "\t", "\t", "fruits", "\t", *str(fruit_price[i]),
              "\t", *str(fruit_stock[i]), "\t", *str(fruit_minimum[i]))
    ch = input("press enter to continue...")


def getHighPriceProduct():
    highest = -999999
    highest2 = -999999
    idx = 0             #idx and idx2 represent specific indexes positions
    idx2 = 0
    print("Product", "\t", "Category", "\t",
          "Price", "\t", "Stock", "\t", "Minimum")
    print("----------------------------------------------------------------")
    for i in range(0, counter):
        if(grocery_price[i] > highest):
            highest = grocery_price[i]
            idx = i
    for i in range(0, counter2):
        if(fruit_price[i] > highest2):
            highest2 = fruit_price[i]
            idx2 = i

    if grocery_price[idx] > fruit_price[idx2]:      #if available stock is less than required then condition is true
        print(*grocery[idx], "\t", "grocery", "\t", *str(grocery_price[idx]),
              "\t", *str(grocery_stock[idx]), "\t", *str(grocery_minimum[idx]))
    elif fruit_price[idx2] > grocery_price[idx]:        #if available stock is less than required then condition is true
        print(*fruits[idx2], "\t", "fruits", "\t", *str(fruit_price[idx2]),
              "\t", *str(fruit_stock[idx2]), "\t", *str(fruit_minimum[idx2]))
    ch = input("press enter to continue...")


def calculateTax():
    print("Product", "\t", "\t", "Category", "\t", "Price", "\t", "Tax")
    print("-----------------------------------------------")
    for i in range(0, counter):
        print(*grocery[i], "\t", "\t", "grocery", "\t", *
              str(grocery_price[i]), "\t", (grocery_price[i]*0.1))
    for i in range(0, counter2):
        print(*fruits[i], "\t", "\t", "fruit", "\t", *
              str(fruit_price[i]), "\t", (fruit_price[i]*0.05))

    ch = input("press enter to continue...")

def productsToBeOrdered():
    print("Product", "\t", "Category", "\t", "\t", "Stock", "\t", "Minimum")
    print("----------------------------------------------------------------")
    for i in range(0, counter):
        if grocery_stock[i] < grocery_minimum[i]:           #finding the products to be ordered
            print(*grocery[i], "\t", "\t", "grocery", *
                  str(grocery_stock[i]), "\t", *str(grocery_minimum[i]))
    for i in range(0, counter2):
        if fruit_stock[i] < fruit_minimum[i]:               #finding the products to be ordered
            print(*fruits[i], "\t", "\t", "fruit", *
                  str(fruit_stock[i]), "\t", *str(grocery_minimum[i]))
    ch = input("press enter to continue...")

def sellProduct():
    viewProducts()
    alpha = 0
    beta = 0
    product = input("Enter your product to buy: ")
    qty = int(input("Enter your quantity: "))
    for i in range(0, counter):
        if product == fruits[i] and fruit_stock[i] > 0:
            alpha = fruit_stock[i]                      #saving the quantity to a variable
            beta = alpha-qty                            #subtracting the entered quantity from available quantity
            fruit_stock[i] = beta                       #storing the new quantity in the original place
    for i in range(0, counter2):
        if product == grocery[i] and grocery_stock > 0:
            alpha = grocery_stock[i]                    #saving the quantity to a variable
            beta = alpha-qty                            #subtracting the entered quantity from available quantity
            grocery_stock[i] = beta                     #storing the new quantity in the original place

def drivercode():
    global option
    while option != 7:          #option 7 means exit
        os.system("cls")        #clears screen
        option = showMenu()      
        if option == 1:
            os.system("cls")
            showHeader()
            showSubheader(option)
            addProductUI()
            addProduct()
        elif option == 2:
            os.system("cls")
            showHeader()
            showSubheader(option)
            viewProducts()
        elif option == 3:
            os.system("cls")
            showHeader()
            showSubheader(option)
            getHighPriceProduct()
        elif option == 4:
            os.system("cls")
            showHeader()
            showSubheader(option)
            calculateTax()
        elif option == 5:
            os.system("cls")
            showHeader()
            showSubheader(option)
            productsToBeOrdered()
        elif option == 6:
            os.system("cls")
            showHeader()
            showSubheader(option)
            sellProduct()

drivercode()
