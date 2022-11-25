# welcome line
print("Welcome to the tip calculator.")

# define user generated variables
bill = float(input("What was the total bill? $"))
percent = int(input("What percentage would you like to tip? 10, 12, or 15? "))
people = int(input("How many people split the bill? "))

# math that sh*t out
total = percent / 100 * bill + bill
each = total / people

# if it don't make static two digit floats, it don't make cents
each_fl = "{:.2f}".format(each)

# tell dem what dey owe
print(f"Each person owes ${each_fl}")
