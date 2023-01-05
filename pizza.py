# this could be used with any product that has more than one variable. an excercise in dealing a number of moving variables

print("welcome to noble's pizza deliveries")
size = input("what size pizza do you want? s, m, or l ")
add_pepperoni = input("do you want pepperoni? y or n ")
extra_cheese = input("do you want extra cheese? y or n ")

bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
else:
    bill += 0

if extra_cheese == "Y":
    bill += 1
else:
    bill += 0

print(f"Your final bill is ${bill}.")
