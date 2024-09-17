# Input a Python list of student heights for example 123, 124, 234 
student_heights = input().split(',')
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
countListValues = len(student_heights)
#print(student_heights)
#print(countListValues)

num = 0
for x in student_heights:
  num = num + int(x)
  
print(f"total height = {num}")
print(f"number of students = {countListValues}")
print(f"average height = {round(num/countListValues)}")