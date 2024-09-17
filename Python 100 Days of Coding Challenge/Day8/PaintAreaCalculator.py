#Write your code below this line 👇
import math
def paint_calc(height, width, cover):
    area = height * width
    coverage_area = area / coverage
    coverage_area_rounded = math.ceil(coverage_area)
    print(f"You will need approixmently {coverage_area} cans of paint, its best to get {coverage_area_rounded} cans just incase.")


#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
# 🚨 Don't change the code above 👆