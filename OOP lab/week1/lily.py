age=int(input("Enter age of lily:"))
price=float(input("Enter price of a toy:"))
machine=float(input("Enter price of washing machine:"))

odd_count=0
for i in range(1,age+1,2):
    odd_count+=1
FT=odd_count*price
even_count=0
for i in range(2,age+1,2):
    even_count+=1
x=0
l=0
for i in range(1,even_count+1):
    x=x+10   
    l=l+x
total=l+FT
total=total-even_count
print("total =",total)
if machine>total:
    print("The money is not enough")
else:
    print("She can buy the machine")


