m = int(input("Enter matric marks:"))  # taking input
f = int(input("Enter first year marks:"))  # taking input
e = int(input("Enter Ecat numbers:"))  # taking input

merit = (m/1100*25)+(f/505*45)+(e/400*30)  # calculting merit
if merit > 60:
    print("Student is eligible")
else:
    print("Student is not eligible")
