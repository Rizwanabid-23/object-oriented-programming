import os

#declaring global lists
user_list = []
prod_list = []
order_list = []
saved_list = []
qty_list = []


class signup_class:
    name = ""
    password = ""
    global user_list

    def __init__(self, name, password):
        self.name = name
        self.password = password


class users:
    def __init__(self, username, password):
        self.user = username
        self.pin = password

    def check_user(self):       #a function to check if entered information is user or wrong information
        for i in range(0, len(user_list)):
            if self.user == user_list[i].name and self.pin == user_list[i].password:
                return "user"

    def changePass(self, new):     #a function to change password of user
        for i in range(0, len(user_list)):
            if self.user == user_list[i].name and self.pin == user_list[i].password:
                user_list[i].password = new
                return True


class admin:
    __user = ""
    __pin = ""

    def __init__(self, username, password):
        self.__user = username
        self.__pin = password

    def check_admin(self):  #check if it is admin or not
        if self.__user == "riz" and self.__pin == "abc":
            return "admin"
        else:   #if its not admin then...
            check = users(self.__user, self.__pin)
            a = check.check_user()
            return a


class product:
    name = ""
    price = 0
    stock = 0

    global prod_list
    global order_list

    def __init__(self, naam, keemat, qty):
        self.name = naam
        self.price = keemat
        self.stock = qty


class order:
    name = ""
    qty = 0

    def __init__(self, naam, mikdaar):
        self.name = naam
        self.qty = mikdaar


class final:
    product = ""
    price = 0
    qty = 0
    date = ""
    card = 0

    def __init__(self, naam, qeemat, tadaad, tareekh, number):
        self.product = naam
        self.price = qeemat
        self.qty = tadaad
        self.date = tareekh
        self.card = number


def addOrder(name, qty):    #a function which reduces the products quantity from prod_list
    for i in range(0, len(prod_list)):
        if name == prod_list[i].name:
            prod_list[i].stock = prod_list[i].stock-int(qty)


def cancelOrder():  #if order is cancelled put the ordered quantity back to prod_list
    for i in range(0, len(prod_list)):
        if order_list[i].name == prod_list[i].name:
            prod_list[i].stock = prod_list[i].stock+order_list[i].qty
    order_list.clear()  #once the order is cancelled ,order_list is also empty


def log():  #first screen
    os.system("cls")
    print("1: Login")
    print("2: Sign up")
    option = int(input("Enter your option: "))
    return option


def loginScreen():  #2nd screen
    os.system("cls")
    print("---Store Management System---")
    print()
    print("--Log in-- ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    type = admin(username, password)
    check = type.check_admin()
    return check


def admin_menu():
    os.system("cls")
    print("1: Add product")
    print("2: Show all products")
    print("3: View all orders")
    print("4: Log out")
    print()
    option = int(input("Enter your option: "))
    return option


def addProduct():
    os.system("cls")
    name = input("Enter product name: ")
    price = int(input("Enter product price: "))
    stock = int(input("Enter stock: "))

    p = product(name, price, stock)
    prod_list.append(p) #puts in list of prod_list


def viewProduct():
    os.system("cls")
    print("Following products are available: ")
    print()
    print("Names", "     ", "Price", "     ", "Stock")
    for i in range(0, len(prod_list)):
        print(prod_list[i].name, "         ",
              prod_list[i].price, "        ", prod_list[i].stock)
    a = input("press enter to continue...")


def signUp():
    os.system("cls")
    print("--Sign up--")
    print()
    uname = input("Enter username: ")
    upin = input("Enter password: ")
    s = signup_class(uname, upin)
    user_list.append(s)     #puts in list of use_list


def userMenu():
    os.system("cls")
    print("1: New order")
    print("2: Change password")
    print("3: Payment")
    print("4: Current shopping cart")
    print("5: Log out")
    print()

    option = int(input("Enter your option: "))
    return option



def newOrder():
    print("-New Order-")
    print("-----------")
    print()
    print("The available products are:")
    print("Names", "     ", "Price", "     ", "Stock")
    viewProduct()
    print()
    pname = input("Enter name of product: ")
    qty = int(input("Enter quantity: "))
    qty_list.append(qty)

    addOrder(pname, qty)
    p = order(pname, qty)
    order_list.append(p)
    a = input("press enter to continue...")


def changePass():
    print("Change password")
    print("---------------")
    print()
    name = input("Enter the name of user: ")
    pin = input("Enter previous password: ")
    newPin = input("Enter new password:")
    u = users(name, pin)
    alpha = u.changePass(newPin)
    if alpha == True:
        print("Password was changed")
    else:
        print("Password was not changed")
    a = input("Press enter to continue...")


def payment():
    date = "4-4-2021"
    global saved_list
    print("Payment")
    print("---------")
    print()
    price = 0
    print("The bill details are as follows:")
    print("Product", "   ", "Quantity", "    ", "Price")
    for i in range(0, len(order_list)):
        if prod_list[i].name == order_list[i].name:
            price = prod_list[i].price
        print(order_list[i].name, "      ", order_list[i].qty,
              "       ", price*int(order_list[i].qty))
    print()
    print("Pay thorugh:")
    print("1: Cheque")
    print("2: Credit/debit card")
    print("OR")
    print("3: Cancel order")
    option = int(input("Enter your option: "))
    if option == 1:
        cheque = int(input("Enter cheque number: "))
        for i in range(0, len(order_list)):
            if prod_list[i].name == order_list[i].name: #getting product name,price and its quantity
                price = prod_list[i].price
                name = order_list[i].name
                qty = order_list[i].qty
                f = final(name, price, qty, date, cheque)
                saved_list.append(f)
        print("Payment was made by cheque. Thank you!!")
        order_list.clear()
    if option == 2:
        card = int(input("Enter debit card number: "))
        for i in range(0, len(order_list)):
            if prod_list[i].name == order_list[i].name:
                price = prod_list[i].price
                name = order_list[i].name
                qty = order_list[i].qty
                f = final(name, price, qty, date, card)
                saved_list.append(f)
        print("The payment was made through debit card. Thank you!!")
        order_list.clear()
    if option == 3:
        cancelOrder()
    a = input("press enter to continue...")


def cart():
    print("Here is your cart:")
    print("Product", "   ", "Price", "    ", "Quantity")
    for i in range(0, len(order_list)):
        if prod_list[i].name == order_list[i].name:
            price = prod_list[i].price
            name = order_list[i].name
            qty = order_list[i].qty
            print(name, "     ", price*int(qty), "         ", qty)
    a = input("press enter to continue...")


def allOrders():
    print("All the orders are as follows: ")
    print()
    print("Product", "   ", "Price", "    ", "Quantity", "   ", "Card/Cheque")
    for i in range(0, len(saved_list)):
        print(saved_list[i].product, "    ", saved_list[i].price,
              "        ", saved_list[i].qty, "       ", saved_list[i].card)
    a = input("press enter to continue...")


def driver_code():
    while True:

        fscreen = 0
        os.system("cls")
        while fscreen != 3:
            fscreen = log()
            if fscreen == 1:
                os.system("cls")
                person = loginScreen()
                os.system("cls")
                if person == "admin":
                    os.system("cls")
                    option = 0
                    while option != 4:
                        option = admin_menu()
                        if option == 1:
                            addProduct()
                        if option == 2:
                            viewProduct()
                        if option == 3:
                            allOrders()
                elif person == "user":
                    os.system("cls")
                    uoption = 0
                    while uoption != 5:
                        uoption = userMenu()
                        if uoption == 1:
                            newOrder()
                        if uoption == 2:
                            changePass()
                        if uoption == 3:
                            payment()
                        if uoption == 4:
                            cart()
                else:
                    print("You have entered wrong information...")

            elif fscreen == 2:
                os.system("cls")
                signUp()


driver_code()
