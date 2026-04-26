#PROBLEM STATEMENT 03
#WAP to check if the year entered by the user is a leap year or not
import calendar 
year = int(input("Enter a year:"))

if calendar.isleap(year):
    print("Yes, it is a leap year")
else:
    print("No, it's not a leap year")