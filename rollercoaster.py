# I had a little fun with the titling of this one. as someone having a midlife crisis, i just want someone to pay for me to ride rollercoasters

print("welcome to the worst rollercoaster in the universe, the pants shitter!")
height = int(input("what is your height in feet? "))
bill = 0

if height >= 4:
  print("you can ride the rollercoaster")
  age = int(input("how old are you? "))
  if age < 12:
    bill = 5
    print("child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("youth tickets are $7.")
  elif age >= 45 and <= 55:
    print("you seem to be having a midlife crisis; why don't you go on ahead--free of charge.")
  else:  
    bill = 12
    print("average adult tickets are $12.")
  photo = input("would you like a photo taken of the moment you shit your pants? y or n ")
  if photo == "Y":
    bill += 3

  print(f"for the ride and a picture, that will be ${bill}, please.")  
else:
  print("sorry, you have to grow taller before you can ride.")
