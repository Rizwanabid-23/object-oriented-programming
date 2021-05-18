import os


class store:        #declaring a class
    Id = 0
    name = ""
    price = 0.0
    category = ""
    brandName = ""
    country = ""


counter = 0     #initializing a counter to count number of enteries
while True:
    os.system("cls")
    print("1: Add product: ")
    print("2: Show product: ")
    print("3: Show total worth of store: ")
    option = int(input("Enter your option: "))

    if option == 1:
        os.system("cls")
        if counter == 0:
            s1 = store()        #calls the class to store following enteries
            s1.Id = int(input("Enter ID of product: "))
            s1.name = input("Enter name of product: ")
            s1.price = float(input("Enter price of product: "))
            s1.category = input("Enter category of product: ")
            s1.brandName = input("Enter brand name: ")
            s1.country = input("Enter country of manufacture: ")
        if counter == 1:
            s2 = store()
            s2.Id = int(input("Enter ID of product: "))
            s2.name = input("Enter name of product: ")
            s2.price = float(input("Enter price of product: "))
            s2.category = input("Enter category of product: ")
            s2.brandName = input("Enter brand name: ")
            s2.country = input("Enter country of manufacture: ")
        if counter == 2:
            s3 = store()
            s3.Id = int(input("Enter ID of product: "))
            s3.name = input("Enter name of product: ")
            s3.price = float(input("Enter price of product: "))
            s3.category = input("Enter category of product: ")
            s3.brandName = input("Enter brand name: ")
            s3.country = input("Enter country of manufacture: ")
        if counter == 3:
            s4 = store()
            s4.Id = int(input("Enter ID of product: "))
            s4.name = input("Enter name of product: ")
            s4.price = float(input("Enter price of product: "))
            s4.category = input("Enter category of product: ")
            s4.brandName = input("Enter brand name: ")
            s4.country = input("Enter country of manufacture: ")
        if counter == 4:
            s5 = store()
            s5.Id = int(input("Enter ID of product: "))
            s5.name = input("Enter name of product: ")
            s5.price = float(input("Enter price of product: "))
            s5.category = input("Enter category of product: ")
            s5.brandName = input("Enter brand name: ")
            s5.country = input("Enter country of manufacture: ")
        counter += 1                                                #counter will increase every time
        ch = input("Press enter to continue...")
    elif option == 2:
        os.system("cls")
        print("Following products are available: ")
        print(s1.name, "\t", s1.price)
        print(s2.name, "\t", s2.price)
        print(s3.name, "\t", s3.price)
        print(s4.name, "\t", s4.price)
        print(s5.name, "\t", s5.price)
        ch = input("Press enter to continue...")
    elif option == 3:
        os.system("cls")
        print("The total worth of store is:", s1.price +
              s2.price+s3.price+s4.price+s5.price)
        ch = input("Press enter to continue...")
