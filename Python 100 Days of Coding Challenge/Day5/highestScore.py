# Example input: 150 142 185 120 171 184 149 199
# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
highestScore = 0

for score in student_scores:
  if score > highestScore:
    highestScore = score
  else:
    highestScore

print(f"The highest score in the class is: {highestScore}")