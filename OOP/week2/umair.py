import time
import os


os.system('cls' if os.name == 'nt' else 'clear')  # clearing screen
#function to validate input password..
def password_validator(enter_password):
    flag = False

    length = len(enter_password)
    """Password length must be 8"""
    if length >= 8:
        for i in range(length):
            if enter_password[i] >= 'A' and enter_password[i] <= 'Z': #one uppercase letter
                flag = True
                break
        if flag == True:
            for j in range(length):
                if enter_password[j] >= "a" and enter_password[j] <= "z": #lower case letters  
                    flag = True
                    break
                else:
                    flag = False
        if flag == True:
            for k in range(length):
                if enter_password[k] == "#" or enter_password[k] == "&" or enter_password[k] == "$": #one special symbol
                    flag = True
                    break
                else:
                    flag = False
        if flag == True:
            for l in range(length):
                if enter_password[l] >= "0" and enter_password[l] <= "9": # atleast one number
                    flag = True
                    break
                else:
                    flag = False

    if flag == True :
        return True

    else :
        return False

#function to validate input email
def validate_ID(email):
    is_true = True
    length = len(email)
    idx = 0
    """Must contain ".com" at the end"""
    if email[length-1] != "m":
        is_true = False
        
    if email[length-2] != "o":
        is_true = False
        
    if email[length-3] != "c":
        is_true = False

    if email[length-4] != ".":
        is_true = False
    if is_true == True:
        if email[0] != "@": # "@" at any index other than first index 
            while idx < length:
               if email[idx] == "@":
                  is_true = True
                  break
               else:
                  is_true = False           
               idx += 1
    for i in range(length):
        if email[i] == " ": # No space must be in email name
            is_true = False
            break
    if is_true == True:    
        return True
    else :
        return False

#function to write on file
def write(id , pin):
    myfile = open("data.txt","a")
    print(id,pin,file=myfile,sep=" ")


#function to read data line by line
def read_data(email, password):
    isFound = False
    myfile = open("data.txt","r")
    records = myfile.read().splitlines()
    for i in records:
        id = get_ID(i, 0)
        pin = get_ID(i, 1)
        #compare id and password with exisiting record
        if email == id and password == pin :
            print("User verified!")
            time.sleep(0.70)
            print("Logged in successfully...")
            isFound = True
            input("press any key to continue")
    
    if isFound == False :
        print("Wrong ID or Password try Again")
        input("press any key return to main page and try again..")


# funtion to find and distinguish email and Password        
def get_ID(dataTocheck, postion):
    idx = 0
    spaceFound = 0
    name = ""
    while idx < len(dataTocheck):
        c = dataTocheck[idx]
        if c == ' ':
           spaceFound += 1

        elif (spaceFound == postion):
           name = name + c
            
        idx += 1
    return name

# printing options
opt = 0
while opt != 3:
    os.system('cls' if os.name == 'nt' else 'clear')  # clearing screen
    print("\t", "Sign-up OR login")
    print("\t", "1- Sign Up")
    print("\t", "2- Log in")
    print("\t", "3- Exit")
    opt = int(input("Enter your option: "))

    # taking input and validating it...
    if opt == 1:
        os.system('cls' if os.name == 'nt' else 'clear')  # clearing screen
        valid_email = False
        valid_email = bool(valid_email)
        ID = input("Enter your email Address: ")
        while valid_email != True : # Checking email...
            valid_email = validate_ID(ID)
            if valid_email == False:
                print("Correct format ->(someone@gmail.com)")
                input("Press any key to enter again...")
                ID = input("Enter your email Address: ")
              
        valid_pin = False
        valid_pin = bool(valid_pin)
        if valid_email == True:
           print("Password length must be 8 or higher include one Uppercase(A-Z), one special symbol and one number(0-9)") 
           passkey = input("Enter your password: ")
           # checking Pin  
           while valid_pin != True :
            valid_pin = password_validator(passkey)
            if valid_pin == False:
                print("Please! enter valid Password...")
                input("Password length must be 8 or higher include one Uppercase(A-Z), one special symbol and one number(0-9)")
                passkey = input("Enter Password: ")

        if valid_email == True and valid_pin == True:   
            write(ID,passkey)

    # read and check data from file
    if opt == 2:
        os.system('cls' if os.name == 'nt' else 'clear')  # clearing screen
        email = input("Log in ID: ")
        password = input("Password: ")
        read_data(email, password)



