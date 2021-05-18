a = int(input("Enter marks out of 100: "))      #taking input
if a > 80 and a <= 100:
    print("The grade is: A")
if a > 60 and a <= 80:
    print("The grade is: B")
if a > 50 and a <= 60:
    print("The grade is: C")
if a > 45 and a <= 50:
    print("The grade is: D")
if a > 25 and a <= 45:
    print("The grade is: E")
if a < 25:
    print("The grade is: F")
if a > 100:
    print("Invalid marks")
