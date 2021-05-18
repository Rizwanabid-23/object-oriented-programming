a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
x = int(input("Enter number of multiples:"))
c = 0
e = 0
for i in range(1, x+1):
    z = a*i
    c = c+z

    d = b*i
    e = e+d

print(c+e)
