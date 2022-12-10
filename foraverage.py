# This lesson was to show how the sum() and len() functions operate under the hood with for loops

numbers = input("Input numbers you need the average for:\n")

for n in range(0, len(numbers)):
    numbers[n] = int(numbers[n])

start = 0
for added in numbers:
    start += added 
average = round(start / (n + 1))
print(average)

