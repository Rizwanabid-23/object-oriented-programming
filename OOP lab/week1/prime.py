a = int(input("Enter positve number:"))
if(a < 0):
    print("You have entered a negative number!")
else:
    for i in range(2, a):
        if a % i == 0:
            print("It is not a prime number.")
            break
        else:
            print("It is a prime number.")
            break
