

from string import ascii_letters

with open('input.in', encoding='utf-8-sig') as file:
    data = [i.replace(" ", "") for i in file.read().strip().split("\n")]

# View data - testing access
#print(data)


# ==== PART 1 ====

# # Iterate through out dataset
totalSum = 0
for entry in data:
    # Get the half way mark
    half = len(entry)//2

    # Split up the string
    leftSide = set(entry[:half])
    rightSide = set(entry[half:])

    # print(leftSide, rightSide)
    for value, character in enumerate(ascii_letters):
        if character in leftSide and character in rightSide:
            totalSum += value + 1

print("Answer to part 1: ", totalSum)

# ==== PART 2 ====
totalSum = 0
j = 3
for i in range(0, len(data), 3):
    entry = data[i:j]
    j += 3

    for value, character in enumerate(ascii_letters):
        if character in entry[0] and character in entry[1] and character in entry[2]:
            totalSum += value + 1


print("Answer to part 2: ", totalSum)
