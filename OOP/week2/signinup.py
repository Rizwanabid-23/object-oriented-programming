import os
def signup():
    os.system('cls')
    file1 = open("data.txt", "a")  # opens the given file
    username = input("Enter username: ")  # asks from user
    length=len(username)
    idx=0
    for i in range(0, len(username)):
        name = username[i]
        # verifying if user has entered required format or not
        if username[length-1] =="m"  and username[length-2] == "o" and username[length-3] =="c" and username[length-4] == "." :
            name = username
        else:
            # prompts user to enter required format
            print("Enter email in proper format")
            ch=input("Press any key to try again...")
            signup()
    print("Note:Password must be of 8 caharacters and must have digits and special characters!")
    userpassword = input("Enter your password: ")
    
    spec = 0
    PinL = 0
    for i in range(0, len(userpassword)):
        pin = userpassword[i]
        # verifying if user has entered required format or not
        if pin == "@" or pin == "!" or pin == "." or pin == "$" or pin == "&" or pin == "%" or pin == "#":
            spec += 1
        PinL += 1  # pinL means length of pin
    if PinL >= 8 and spec >= 1:
        pin = userpassword
    else:
        # prompts user to enter required format
        print(
            "Password is either less than 8 character or there are no special characters.")
    record = name+","+pin  # storing name and pin in a single variable with comma
    print(record, file=file1, sep="\n")  # writing in file
    file1.close()

def signin():
    os.system('cls')
    username = input("Enter yor username: ")  # asks from user
    password = input("Enter your password: ")  # asks from user
    checkUser(username, password)

def checkUser(name, pin):
    count=0
    file1 = open("data.txt", "r")  # opens file
    # reads every line separately and stores each line in variable "data"
    data = file1.read().splitlines()
    for i in range(0, len(data)):
        count+=1
        # reads line character by character and stores in another vaiable "userdata"
        userdata = data[i]
        comma = 0
        username = ""
        password = ""
        for id in range(0, len(userdata)):
            d = userdata[id]
            if d == ',':  # detects the separation between username and password
                comma += 1
            if comma == 0:
                username = username+d
            if comma == 1:
                # separates username and password and removes comma
                password = password.replace(',', '')
                password = password+d
        # print("name",name,"username",username,"passw",password,"pin",pin)
        if name == username and pin == password:  # verifying id name and password match each other
            a = True
        else:
            a = False

        if a == True:
            print("Valid user")
            break
        if a == False and count==len(data):
            print("Invalid user")
    file1.close()
    
option = 0
while(option != 3):  # option 3 means exit program
    
    # shows main menu
    print("1:Sign up")
    print("2:Sign in")
    print("3:Exit")
    option = int(input("Enter your option:"))
    if option == 1:
        signup()  # refers to signup function
    if option == 2:
        signin()  # refers to sign in function
