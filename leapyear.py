# leap year calendar. this will let you know if a year is a leap year or not. this is actually useful

print("welcome to the noble leap year calculator.")

year = int(input("what year would you like to know whether or not it was a leap year?"))

if (year % 100 == 0) and (year % 400 == 0):
    print(f"{year} was a leap year.")
elif (year & 4 == 0) and (year % 100 != 0):
    print(f"{year} was a leap year.")
else:
    print(f"{year} was not a leap year.")
