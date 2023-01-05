# in case looking at a list wasn't enough to find a high score

scores = input("Input a list of scores ").split()
for n in range(0, len(scores)):
  scores[n] = int(scores[n])

highest = None
for score in scores:
    if highest is None or score > highest:
        highest = score
print(highest)

