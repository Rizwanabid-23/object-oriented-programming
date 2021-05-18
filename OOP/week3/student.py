import os


class student:      #declaring a class
    name = ""
    roll_no = 0
    Gpa = 0.0
    isHostellite = ""
    department = ""


counter = 0     #initializing a counter to count number of enteries
while True:
    print("1: Add student: ")
    print("2: Show students: ")
    print("3: List top student: ")
    option = int(input("Enter your option: "))

    if option == 1:
        if counter == 0:
            os.system("cls")
            s1 = student()          #initializing a counter to count number of enteries
            s1.name = input("Enter name of student: ")
            s1.roll_no = int(input("Enter roll number: "))
            s1.Gpa = float(input("Enter GPA of student: "))
            s1.isHostellite = input("Is student hostellite? (Yes/No): ")
            s1.department = input("Enter your department: ")
        elif counter == 1:
            os.system("cls")
            s2 = student()
            s2.name = input("Enter name of student: ")
            s2.roll_no = int(input("Enter roll number: "))
            s2.Gpa = float(input("Enter GPA of students: "))
            s2.isHostellite = input("Is student hostellite? (Yes/No): ")
            s2.department = input("Enter your department: ")
        elif counter == 2:
            os.system("cls")
            s3 = student()
            s3.name = input("Enter name of student: ")
            s3.roll_no = int(input("Enter roll number: "))
            s3.Gpa = float(input("Enter GPA of students: "))
            s3.isHostellite = input("Is student hostellite? (Yes/No): ")
            s3.department = input("Enter your department: ")
        counter += 1
        ch = input("Press enter to continue...")
    elif option == 2:
        print("Following students are enrolled:")
        print(s1.name)
        print(s2.name)
        print(s3.name)
        ch = input("Press enter to continue...")
    elif option == 3:
        if s1.Gpa > s2.Gpa:
            print(s1.name)
        elif s2.Gpa > s1.Gpa:
            print(s2.name)
        elif s1.Gpa > s2.Gpa and s1.Gpa > s3.Gpa:
            print(s1.name)
        elif s2.Gpa > s1.Gpa and s2.Gpa > s3.Gpa:
            print(s2.name)
        elif s3.Gpa > s1.Gpa and s3.Gpa > s2.Gpa:
            print(s3.name)
        ch = input("Press enter to continue...")
