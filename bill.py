#!/usr/bin/env python3

# This lesson takes it cue from British executives putting their business cards in a bowl and pulling at random to see who pays the bill. 
# So this takes input (names) and randomly selects a string from the list, and outputs it.

import random

names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

random_num = random.randint(0, (len(names) - 1))
print(f"{names[random_num]} is going to buy the meal today!")
