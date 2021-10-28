from is_leap_year import *


print("This program will tell if you if a year is a leap year")
year = int(input("Enter the year do you want to check: "))

if is_leap_year(year):
    print(str(year) + " is a leap year")
else:
    print(str(year) + " is not a leap year")


