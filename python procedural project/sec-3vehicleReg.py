reg_list=[]
regPin_list=[]
counter=0
ownername_list=[]
ownerplate_list=[]
ownermodel_list=[]
vehicleCounter=0
importedCounter=0
importedname_list=[]
importedplate_list=[]
importedyear_list=[]
final=[]
duplicate=[]
tax_list=[]

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
                ch=input("Press enter to continue...")
                reg_list.append(Reg)
                regPin_list.append(Pin)
                counter += 1               
            elif adminOption==2:
                print("Change password of registrar")
                print("----------------------------")
                name=input("Enter name of registrar: ")
                for i in range(0,counter):
                    if name==reg_list[i]:
                        newpin=input("Enter new password: ")
                        regPin_list[i]=newpin
                ch=input("Press any key to continue...")
            elif adminOption==3:
                print("Following registrars are enrolled:")
                print(" ")
                print("Name","\t","Pin")
                for i in range(0,counter):
                    print(reg_list[i],"\t",regPin_list[i])
                ch=input("Press any key to continue...")
    else:
        for i in range(0,counter+1):
            if username==reg_list[i] and password==regPin_list[i]:
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
                        model=int(input("Enter model year of vehicle: "))
                        ownername_list.append(name)
                        ownerplate_list.append(plate)
                        ownermodel_list.append(model)
                        vehicleCounter += 1           
                        duplicate.append(model)   
                        final.append(model)         
                        ch=input("Press any key to continue...")
                    elif regOption==2:
                        print("Change vehicle owner")
                        check=input("Enter name of owner: ")
                        for i in range (0,vehicleCounter):
                            if check==ownername_list[i]:
                                newname=input("Enter new name of owner:")
                                ownername_list[i]=newname
                        ch=input("Press any key to continue...")
                    elif regOption==3:
                        print("View all vehicles")
                        print("Following vehicles are registered:")
                        print("Owner","\t","Plate number","\t","\t","Model year")
                        for i in range(0,vehicleCounter):
                            print(ownername_list[i],"\t",ownerplate_list[i],"\t",ownermodel_list[i])
                        print(" ")
                        ch=input("Press any key to continue...")
                    elif regOption==4:
                        print("Owner","\t","Plate number","\t","\t","Model year")
                        latest=-99999
                        global idx
                        idx=0
                        for id in range(0,vehicleCounter):
                            
                            for i in range(0,vehicleCounter):
                                if duplicate[i]>latest:
                                    latest=duplicate[i]
                                    idx=i
                            duplicate[idx]=-1
                            final[id]=latest
                            
                        for index in range(0,final):                            
                            print(ownername_list[index],"\t",ownerplate_list[index],"\t",final[index])
                        ch=input("Press any key to continue...")
                    elif regOption==5:
                        importedName=input("Enter name of owner: ")
                        importedPlate=int(input("Enter plate of vehicle: "))
                        importedModel=int(input("Enter model year of vehicle: "))
                        tax=input("Is tax paid? (yes/no):")
                        importedname_list.append(importedName)
                        importedplate_list.append(importedPlate)
                        importedyear_list.append(importedModel)
                        tax_list.append(tax)
                        importedCounter += 1
                        ch=input("Press any key to continue...")
                    elif regOption==6:
                        print("View all imported vehicles")
                        print("Following imported vehicles are registered:")
                        print("Owner","\t","Plate number","\t","\t","Model year","\t","Tax")
                        for i in range(0,importedCounter):
                            print(importedname_list[i],"\t",importedplate_list[i],"\t",importedyear_list[i],"\t",tax_list[i])                       
                        ch=input("Press any key to continue...")
                    elif regOption==7:
                        print("Owner","\t","Plate number","\t","\t","Model year","\t","Tax")
                        for i in range(0,importedCounter):
                            if tax_list[i]=="no":
                                print(importedname_list[i],"\t",importedplate_list[i],"\t",importedyear_list[i],"\t",tax_list[i])
                            ch=input("Press any key to continue...")
                        else:
                            print("taxes are paid")





























