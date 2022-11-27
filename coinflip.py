#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random       	 
#Write the rest of your code below this line 👇
print("Heads or Tails?")
coin_flip = random.randint(0, 1)
if coin_flip == 0:
    print("Tails")
else:
    print("Heads")
