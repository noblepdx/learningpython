print("Welcome to the Super Simple Leap Year Calculator.")

year = int(input("What year would you like to know whether or not it was a leap year?"))

if (year % 100 == 0) and (year % 400 == 0):
    print(f"{year} was a leap year.")
elif (year & 4 == 0) and (year % 100 != 0):
    print(f"{year} was a leap year.")
else:
    print(f"{year} was not a leap year.")
