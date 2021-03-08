import os
reg_list = []
regPin_list = []
total = 0
ownername_list = []
ownerplate_list = []
ownermodel_list = []
vehicleCounter = 0
importedCounter = 0
importedname_list = []
importedplate_list = []
importedyear_list = []
final = []
duplicate = []
tax_list = []

counter = 0


def adminMenu():
    print("** Admin Menu**")
    print("   ----------  ")
    print(" ")
    print("1:Add a registrar")
    print("2:Change password of registrar")
    print("3:View all registrars")
    print("4:Log out")
    print(" ")
    adminOption = int(input("Enter your option: "))
    return adminOption


def addReg():
    print("Add a registrar")
    print("---------------")

    Reg = input("Enter name of registrar: ")

    Pin = input("Enter password of registrar: ")
    ch = input("Press enter to continue...")
    global reg_list
    reg_list.append(Reg)
    global regPin_list
    regPin_list.append(Pin)
    global total
    total += 1


def changeReg():
    print("Change password of registrar")
    print("----------------------------")
    name = input("Enter name of registrar: ")
    for i in range(0, counter):
        if name == reg_list[i]:
            newpin = input("Enter new password: ")
            regPin_list[i] = newpin
    ch = input("Press any key to continue...")


def viewReg():
    print("Following registrars are enrolled:")
    print(" ")
    print("Name", "\t", "Pin")
    for i in range(0, counter):
        print(reg_list[i], "\t", regPin_list[i])
    ch = input("Press any key to continue...")


def regMenu():
    print("**Registrar Menu**")
    print(" ")
    print("1: Add vehicle.")
    print("2: Change vehicle owner.")
    print("3: View all vehicles.")
    print("4: Sort vehicles with latest being first.")
    print("5: Register an imported vehicle.")
    print("6: View all imported vehicles.")
    print("7: View imported cars tax defaulters.")
    print("8: Log out.")
    print(" ")
    regOption = int(input("Enter your option: "))
    return regOption


def addVehicle():
    print("Add a new vehicle")
    name = input("Enter name of owner: ")
    plate = input("Enter number plate of vehicle: ")
    model = int(input("Enter model year of vehicle: "))
    global ownername_list
    global ownerplate_list
    global ownermodel_list
    ownername_list.append(name)
    ownerplate_list.append(plate)
    ownermodel_list.append(model)
    global counter
    counter += 1
    global duplicate
    global final
    duplicate.append(model)
    final.append(model)
    ch = input("Press any key to continue...")


def changeOwner():
    print("Change vehicle owner")
    check = input("Enter name of owner: ")
    for i in range(0, counter):
        if check == ownername_list[i]:
            newname = input("Enter new name of owner:")
            ownername_list[i] = newname
    ch = input("Press any key to continue...")


def viewVehicles():
    print("View all vehicles")
    print("Following vehicles are registered:")
    print("Owner", "\t", "Plate number", "\t", "Model year")
    for i in range(0, counter):
        print(ownername_list[i], "\t", ownerplate_list[i],
              "\t","\t", ownermodel_list[i])
    print(" ")
    ch = input("Press any key to continue...")


def latestFunction():
    print("Owner", "\t", "Plate number", "\t", "Model year")
    latest = -99999
    global idx
    idx = 0
    for id in range(0, counter):
        for i in range(0, counter):
            if duplicate[i] > latest:
                latest = duplicate[i]
                idx = i
        duplicate[idx] = -1
        final[id] = latest
    for index in range(0, final):
        print(ownername_list[index], "\t",
              ownerplate_list[index], "\t", final[index])
    ch = input("Press any key to continue...")


def addImported():
    importedName = input("Enter name of owner: ")
    importedPlate = int(input("Enter plate of vehicle: "))
    importedModel = int(input("Enter model year of vehicle: "))
    tax = input("Is tax paid? (yes/no):")
    global importedname_list
    global importedplate_list
    global importedyear_list
    global tax_list
    importedname_list.append(importedName)
    importedplate_list.append(importedPlate)
    importedyear_list.append(importedModel)
    tax_list.append(tax)
    global importedCounter
    importedCounter += 1
    ch = input("Press any key to continue...")


def viewImported():
    print("View all imported vehicles")
    print("Following imported vehicles are registered:")
    print("Owner", "\t", "Plate number", "\t", "Model year", "\t", "Tax")
    for i in range(0, importedCounter):
        print(importedname_list[i], "\t", importedplate_list[i],
              "\t","\t", importedyear_list[i], "\t", tax_list[i])
    ch = input("Press any key to continue...")


def taxFunction():
    print("Owner", "\t", "Plate number", "\t",  "Model year", "\t", "Tax")
    for i in range(0, importedCounter):
        if tax_list[i] == "no":
            print(importedname_list[i], "\t", importedplate_list[i],"\t",
                  "\t", importedyear_list[i], "\t", tax_list[i])
    ch = input("Press any key to continue...")


while True:
    os.system("cls")
    print("*** Vehicle Registration Center")
    print(" ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    global adminOption
    global regOption

    if username == "riz" and password == "abc":
        adminOption = 0
        while adminOption != 4:
            os.system("cls")
            adminOption = adminMenu()
            if adminOption == 1:
                os.system("cls")
                addReg()
            elif adminOption == 2:
                os.system("cls")
                changeReg()
            elif adminOption == 3:
                os.system("cls")
                viewReg()
    else:
        for i in range(0, total):
            if username == reg_list[i] and password == regPin_list[i]:
                
                OP = 0
                while OP != 8:
                    OP = regMenu()
                    if OP == 1:
                        os.system("cls")
                        addVehicle()
                    elif OP == 2:
                        os.system("cls")
                        changeOwner()
                    elif OP == 3:
                        os.system("cls")
                        viewVehicles()
                    elif OP == 4:
                        os.system("cls")
                        latestFunction()
                    elif OP == 5:
                        os.system("cls")
                        addImported()
                    elif OP == 6:
                        os.system("cls")
                        viewImported()
                    elif OP == 7:
                        os.system("cls")
                        taxFunction()
