# supposedly reminiscent of childhood game where children would sit in a cicle and count from 1 to 100, replacing the numeral with "Fizz" if the number is divisible by 3, "Buzz" if the number is divisible by 5, and "FizzBuzz" if the number is divisible by 3 and 5. 

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

