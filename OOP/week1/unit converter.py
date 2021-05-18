print("***Unit converter***")
V = int(input("Enter value to convert: "))  # Taking input
unit = input("Enter your unit: ")  # Taking input in string
X = V*1000
if(unit == "kg"):  # checking conditions
    print("the converted value is ", X)
if(unit == "kg"):  # checking conditions
    print("the new unit is gram")
Y = V/1000
if(unit == "gram"):  # checking conditions
    print("the converted value is ", Y)
if(unit == "gram"):  # checking conditions
    print("the new unit is kg")
L = V*100
if(unit == "meters"):  # checking conditions
    print("the converted value is ", L)
if(unit == "meters"):  # checking conditions
    print("the converted unit is centimeters")
T = V*60
if(unit == "seconds"):  # checking conditions
    print("the converted value is ", T)
if(unit == "seconds"):  # checking conditions
    print("the converted unit is seconds")
C = V*163.15
if(unit == "USD"):  # checking conditions
    print("the converted value is ", C)
if(unit == "USD"):  # checking conditions
    print("the converted currency is PKR")
