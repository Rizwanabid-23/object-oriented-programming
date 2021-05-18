a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter ending number"))
d = a+b
print("The fabonacci series is:")
print(a)
print(b)
print(d)
ans = 0
counter = 0
for i in range(a, c):
    counter = counter+1
    if(counter >= c-2):
        exit()
    else:
        ans = b+d
        b = d
        d = ans
        print(ans)
