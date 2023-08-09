# Give year leap year or not
y = int(input("Enter a year : "))
if ( y % 4 == 0 and y % 100 != 0 ) or ( y % 400 == 0 ) :
    print("Given year", y, "is LEAP YEAR")
else:
    print("Given year", y, "is NOT LEAP YEAR")
