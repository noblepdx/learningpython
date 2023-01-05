# tip calculator. this could be really useful.

print("welcome to noble's tip calculator")

bill = float(input("what was the total bill? $"))
percent = int(input("what percentage would you like to tip? 15, 20, or 25? "))
people = int(input("how many people split the bill? "))

total = percent / 100 * bill + bill
each = total / people

each_fl = "{:.2f}".format(each)

print(f"each person owes ${each_fl}")
