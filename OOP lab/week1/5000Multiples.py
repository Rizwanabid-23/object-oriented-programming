a = 7
b = 3
c = 8
x = 0
y = 0
z = 0
for i in range(1, 5001):
    a1 = a*i
    x = x+a1

    b1 = b*i
    y = y+b1

    c1 = c*i
    z = z+c1

print("The sum of 5000 multiples is:", x+y+z)
