student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

highest = None
for score in student_scores:
    if highest is None or score > highest:
        highest = score
print(highest)

