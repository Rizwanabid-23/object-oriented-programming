money = float(input("Enter paisa:"))
year = int(input("Enter ending year:"))
age = 18
count = 0
for i in range(1800, year+1):
    count += 1
Fage = count+18
for i in range(1801, year+1, 2):
    money = money-(12000+50*Fage)
for i in range(1800, year+1, 2):
    money = money-12000

print(money)
if(money > 0):
    print("yes he can survive with ", money, "rupees")
else:
    print("no,he will have ", -money, "short")
