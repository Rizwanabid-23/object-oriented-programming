import os
option = -10

# Function that add the new user in file
def addUserInFile():
# open the file for write user data in file
    myfile = open("userdata.txt","a")
    userNameUI = input("Enter User Name ->")
    for vN in range(0 , len(userNameUI)):
        chN = userNameUI[vN]
# Check that user name contain only alphabet
        if (chN >= "a" and chN <= "z") or (chN >= "A" and chN <= "Z"):
            userName = userNameUI
        else:
            print("Enter Name in only alphabets")
            input("press any key to continue")
            return 0
    userPasswordUI = input("Enter User Password ->")
    pinLength = 0
    specialCharacter = 0
    for vP in range(0 , len(userPasswordUI)):
        chP = userPasswordUI[vP]
        pinLength = pinLength+1
# Check that user Password contain only special character
        if (chP >= "!" and chP <= "/") or (chP >= ":" and chP <= "@"):
            specialCharacter = specialCharacter+1

    if (pinLength >= 8 and pinLength <=14) and (specialCharacter >=2 and specialCharacter <=4):
        userPassword = userPasswordUI
    else:
        print("Password should be at leat 8 characters or at most 14 characters includin at lest 2 and at most 4 special characters")
        input("press any key to continue")
        return 0

    record = userName+","+userPassword
    print(record,file=myfile,sep="\n")
    myfile.close()

# Function that enter user from console on sign in
def enterYourName(): 
    existNmOrNot = input("Enter Your Name ->")
    existPasOrNot = input("Enter Your Password ->")

    userExistOrnot(existNmOrNot,existPasOrNot)

# This Function will check that user exist or not1

def userExistOrnot(name,pin):
    myfile = open("userdata.txt","r")
    userData = myfile.read().splitlines()

    for i in range(0 ,len(userData)):

        dt = userData[i]
        eName = ""
        ePin = ""
        commaFound = 0
        for idx in range(0 ,len(dt)):
            c = dt[idx]


            if c == ',':
                commaFound = commaFound+1
            
            elif commaFound == 0:
                eName = eName+c

            elif commaFound == 1:
                ePin = ePin+c    

                if name == eName and pin == ePin:
                    print("Valid User")
                    input("press any key to continue")
                    return 0              
    print("InValid User")
    input("press any key to continue")
    myfile.close()


while True:
    os.system('cls' if os.name=='nt' else 'clear') 
    print("1-SIGN UP")
    print("2-SIGN IN")
    option = int(input("Select your option from following ->"))
    if option == 1:
        os.system('cls' if os.name=='nt' else 'clear') 
        addUserInFile()
    if option == 2:
        os.system('cls' if os.name=='nt' else 'clear') 
        enterYourName()