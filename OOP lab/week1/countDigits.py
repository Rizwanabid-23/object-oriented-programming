num = int(input("Enter a number:"))
counter = 0
while(num != 0):
    digit = int(num/10)
    num = digit
    counter += 1
print("The number of digits are: ", counter)
