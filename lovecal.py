# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


name1_lower = name1.lower()
name2_lower = name2.lower()

T = name1_lower.count("t") + name2_lower.count("t")
R = name1_lower.count("r") + name2_lower.count("r")
U = name1_lower.count("u") + name2_lower.count("u")
E = name1_lower.count("e") + name2_lower.count("e")

score1 = T + R + U + E 

L = name1_lower.count("l") + name2_lower.count("l")
O = name1_lower.count("o") + name2_lower.count("o")
V = name1_lower.count("v") + name2_lower.count("v")
E2 = name1_lower.count("e") + name2_lower.count("e")
score2 = L + O + V + E2

score = str(score1) + str(score2)

if int(score) < 10 or int(score) > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif int(score) >= 40 and int(score) <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")


