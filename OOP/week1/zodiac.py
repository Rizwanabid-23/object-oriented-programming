D = int(input("Enter date of birth:"))  # taking input
month = input("Enter month of birth ")  # taking input in string
if((month == "JAN" and D >= 21) or (month == "FEB" and D <= 19)):
    print("the zodiac sign is aquarius")
if((month == "DEC" and D >= 22) or (month == "JAN" and D <= 20)):
    print("the zodiac sign is capricon")
if((month == "FEB" and D >= 20) or (month == "MAR" and D <= 20)):
    print("the zodiac sign is pisces")
if((month == "MAR" and D >= 21) or (month == "APR" and D <= 19)):
    print("the zodiac sign is aries")
if((month == "MAR" and D >= 20) or (month == "MAY" and D <= 20)):
    print("the zodiac sign is tayrus")
if((month == "MAY" and D >= 21) or (month == "JUN" and D <= 21)):
    print("the zodiac sign is gemini")
if((month == "JUN" and D >= 22) or (month == "JUL" and D <= 23)):
    print("the zodiac sign is cancer")
if((month == "JUL" and D >= 24) or (month == "AUG" and D <= 23)):
    print("the zodiac sign is leo")
if((month == "AUG" and D >= 24) or (month == "SEP" and D <= 22)):
    print("the zodiac sign is virgo")
if((month == "SEP" and D >= 23) or (month == "OCT" and D <= 22)):
    print("the zodiac sign is libra")
if((month == "OCT" and D >= 23) or (month == "NOV" and D <= 22)):
    print("the zodiac sign is scorpio")
if((month == "NOV" and D >= 23) or (month == "DEC" and D <= 20)):
    print("the zodiac sign is sagitarius")
