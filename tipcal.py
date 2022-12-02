print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
percent = int(input("What percentage would you like to tip? 10, 12, or 15? "))
people = int(input("How many people split the bill? "))

total = percent / 100 * bill + bill
each = total / people

each_fl = "{:.2f}".format(each)

print(f"Each person owes ${each_fl}")
