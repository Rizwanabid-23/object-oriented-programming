a=int(input("Enter number of books: "))     #taking input
b=a*100
if (b>1000):
    c=b-(b*0.1)         #calculating discount
    print(c)
else:
    print(b)
