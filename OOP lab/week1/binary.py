a = int(input("Enter the number:"))
counter = 0
while counter != 8:
    counter = counter+1
    mod = a % 2
    a = a/2
    print(mod)
