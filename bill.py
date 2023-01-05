# bill randomizer
# in case you go out to eat with a bunch of rich friends who can afford to get everybody's meal

import random

names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

random_num = random.randint(0, (len(names) - 1))
print(f"{names[random_num]} is going to buy the meal today!")
