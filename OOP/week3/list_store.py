import os

store_list = []
keepadding="yes"

def showAllProducts(store_list):        # a function which print all the products with their details
    for i in store_list:
        print(i.Id, "\t", i.name, "\t","\t", i.price, "\t",      #a loop will run and print all enteries at specific indices
              i.category, "\t", i.brandName, "\t", i.country)


def getstore():     #a function to store new items
    s = store()     #calls a class
    s.Id = int(input("Enter ID of product: "))
    s.name = input("Enter name of product: ")
    s.price = float(input("Enter price of product:"))
    s.category = input("Enter category of product: ")
    s.brandName = input("Enter brand of product: ")
    s.country = input("Enter country of manufacture: ")
    return s        # 's' contains all the entered data in it


def worth(store_list):      #a function to calculate price of all products
    keemat = 0
    for i in store_list:
        keemat = keemat+i.price
    return keemat


class store():  # declaring a class
    Id = 0
    name = ""
    price = 0.0
    category = ""
    brandName = ""
    country = ""


while True:
    os.system("cls")
    print("1: Add product: ")
    print("2: Show product: ")
    print("3: Show total worth of store: ")
    option = int(input("Enter your option: "))

    if option == 1:
        while keepadding=="yes":
            os.system("cls")        #clears screen
            s = getstore()          #receives a pack of enteries from function
            store_list.append(s)        #puts enteries in a list
            keepadding=input("Do you want to add more entity? (yes/no): ")
    elif option == 2:
        os.system("cls")
        print("Following products are available: ")
        print("ID", "\t", "Name", "\t", "\t", "Price", "\t",
              "Category", "\t", "Brand", "\t", "Country")
        showAllProducts(store_list)
        ch = input("Press enter to continue...")
    elif option == 3:
        os.system("cls")
        print("The total worth of store is:")
        ahmiyat = 0
        ahmiyat = worth(store_list)         #calls a function to calculate total amount of products
        print(ahmiyat)
        ch = input("Press enter to continue...")
