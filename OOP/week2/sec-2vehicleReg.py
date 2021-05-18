while True:
    print("*** Vehicle Registration Center")
    print(" ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    global adminOption
    global regOption

    if username=="riz" and password=="abc":
        adminOption=0
        while adminOption!=4:
            print("** Admin Menu**")
            print("   ----------  ")
            print(" ")
            print("1:Add a registrar")
            print("2:Change password of registrar")
            print("3:View all registrars")
            print("4:Log out")
            print(" ")
            adminOption =int(input("Enter your option: "))
            if adminOption==1:
                print("Add a registrar")
                print("---------------")
                global Reg
                Reg=input("Enter name of registrar: ")
                global Pin
                Pin=input("Enter password of registrar: ")
                ch=input("Press any key to continue...")
            elif adminOption==2:
                print("Change password of registrar")
                print("----------------------------")
                name=input("Enter name of registrar: ")
                newpin=input("Enter new password: ")
                if name==Reg:
                    Pin=newpin
                ch=input("Press any key to continue...")
            elif adminOption==3:
                print("Following registrars are enrolled:")
                print(" ")
                print(Reg,"\t",Pin)
                ch=input("Press any key to continue...")
    elif username==Reg and password==Pin:
        regOption=0
        while regOption!=8:
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
            regOption=int(input("Enter your option: "))
            if regOption==1:
                print("Add a new vehicle")
                name=input("Enter name of owner: ")
                plate=input("Enter number plate of vehicle: ")
                model=input("Enter model year of vehicle: ")
                ch=input("Press any key to continue...")
            elif regOption==2:
                print("Change vehicle owner")
                check=input("Enter name of owner: ")
                if check==name:
                    newname=input("Enter new name for vehicle:")
                    name=newname
                else:
                    print("Wrong information")
                ch=input("Press any key to continue...")
            elif regOption==3:
                print("View all vehicles")
                print("Following vehicles are registered:")
                print(name,"\t",plate,"\t",model)
                ch=input("Press any key to continue...")
            elif regOption==4:
                print("The sorting is not possible now")
                ch=input("Press any key to continue...")
            elif regOption==5:
                importedName=input("Enter name of owner: ")
                importedPlate=input("Enter plate of vehicle: ")
                importedModel=input("Enter model year of vehicle: ")
                tax=input("Is tax paid? (yes/no):")
                ch=input("Press any key to continue...")
            elif regOption==6:
                print("View all imported vehicles")
                print("Following imported vehicles are registered:")
                print(importedName,"\t",importedPlate,"\t",importedModel)
                ch=input("Press any key to continue...")
            elif regOption==7:
                if tax=="no":
                    print(importedName,"\t",importedPlate,"\t",importedModel)
                    ch=input("Press any key to continue...")
                else:
                    print("taxes are paid")














