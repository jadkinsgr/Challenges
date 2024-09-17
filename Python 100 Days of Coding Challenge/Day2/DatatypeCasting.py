num_char = len(input("What is your name?"))
print(type(num_char))

newNumChar = str(num_char)
print(type(newNumChar))

# normal
print("your name has " + newNumChar + " charecters")
# f-string
print(f"your name has {newNumChar} characters")
