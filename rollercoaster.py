print("Welcome to the worst rollercoaster in the universe, the Pants Shitter!")
height = int(input("What is your height in feet? "))
bill = 0

if height >= 4:
  print("You can ride the rollercoaster!")
  age = int(input("And how old are you? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and <= 55:
    print("You seem to be having a midlife crisis; why don't you go on ahead--free of charge.")
  else:  
    bill = 12
    print("Adult tickets are $12.")
  photo = input("Would you like a photo taken of the moment you shit your pants? Y or N. ")
  if photo == "Y":
    bill += 3

  print(f"For the ride and a picture, that will be ${bill}, please.")  
else:
  print("Sorry, you have to grow taller before you can ride.")
