import os

students_list = []  #a list which stores all data of students as single entity
duplicate = []      #a duplicate list for gpa
keepadding="yes"

class student:  # declaring a class
    name = ""
    roll_no = 0
    Gpa = 0.0
    isHostellite = ""
    department = ""


def getstudent():       #a function for entering data of new student
    s = student()       #calls the custom class
    s.name = input("Enter name of student: ")
    s.roll_no = int(input("Enter roll number of student: "))
    s.Gpa = float(input("Enter GPA of student: "))
    duplicate.append(s.Gpa)
    s.isHostellite = input("Is student a hostellite? (yes/no): ")
    s.department = input("Enter the department: ")
    return s


def showStudents(students_list):        #a function toprint out all students
    for i in students_list:
        print(i.name, "\t", i.roll_no, "\t", "\t", i.Gpa,
              "\t", i.isHostellite, "\t", i.department)


def topstudent(students_list):      #a function to find the top student
    largest = -9999                 #initializing a variable with a small value
    idx = 0                         #initialing a variable which will store indexes
    name = []                       #initializing a list to store names of students
    marks = []                      #initializing a list to store marks of students
    for i in range(0, len(duplicate)):
        if duplicate[i] > largest:
            largest = duplicate[i]
            idx = i                 #storing index of largest value
    for i in students_list:         
        name.append(i.name)         #storing names in name list
        marks.append(i.Gpa)         #storing marks in marks list
    print(name[idx], "\t", marks[idx])  


while True:
    os.system("cls")
    print("1: Add student: ")
    print("2: Show students: ")
    print("3: List top student: ")
    option = int(input("Enter your option: "))
    if option == 1:
        while keepadding=="yes":
            os.system("cls")
            shagird = getstudent()
            students_list.append(shagird)
            keepadding=input("Do you want to add more entery? (yes/no): ")
    elif option == 2:
        os.system("cls")
        print("Following students are enrolled:")
        print("Name", "\t", "Roll no.", "\t", "GPA",
              "\t", "Residance", "\t", "Department")
        showStudents(students_list)
        ch = input("Press enter to continue...")
    elif option == 3:
        os.system("cls")
        print("The top student is:")
        print("Name","\t","GPA")
        topstudent(students_list)
        ch = input("Press enter to continue...")
