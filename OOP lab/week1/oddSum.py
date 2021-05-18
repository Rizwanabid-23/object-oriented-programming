a = int(input("ENter first number:"))
b = int(input("Enter second number:"))
print("The sum of numbers are: ")
sum = 0
if a % 2 == 0:
    a = a+1
    for i in range(a, b, 2):
        sum = sum+i
    print(sum)
else:
    for i in range(a, b, 2):
        sum = sum+i
    print(sum)
