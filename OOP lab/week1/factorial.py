a = int(input("Enter your number:"))
b = 1
for i in range(a, 0, -1):
    b = b*a
    a = a-1
print("The answer is: ", b)