base = int(input("Enter base value:"))
power = int(input("Enter power value:"))
ans = 1
for i in range(1, power+1):
    ans = base*ans
    # base=ans
print("The answer is: ", ans)
