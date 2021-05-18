a = int(input("Enter total number of classes:"))  # taking input
b = int(input("Enter number of classes attended:"))  # taking input
c = (b/a)*100  # calculating percentage

if(c >= 75):
    print("Percentage is:", c, ".The student is allowed to sit in exam")
else:
    print("Percentage is:", c, "The student is not allowed to sit in exam hall")
