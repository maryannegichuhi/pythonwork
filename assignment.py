# create a python program to check if the years is leap or not
# leap year is divisible by 4 but not divisible by 100
# except if its also divisible by 400
yr = int(input("Enter year:"))
if yr % 4 == 0 and (yr % 100 != 0 or yr % 400 == 0):
    print(yr, "is a leap year")
else:
    print(yr, "is not a leap year")


