print(" sunday=1, mon=2, tues=3, wed=4, thurs=5, fri=6, sat=7")
D = int(input("Enter day of week:"))  # taking input
A = int(input("Enter your age:"))  # taking input
if(D == 2):
    print("the museum is closed")
if(D == 3 or D == 5):
    print("everyone gets half price")
if(D == 4 and A >= 13 and A <= 20):
    print("you will get discount")
if(A < 6 or A > 65):
    print("your admission is free")
if(D == 1 or D == 7 and (A >= 6 and A <= 12)):
    print("your admission is half priced")
