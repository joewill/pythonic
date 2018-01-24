import random

letters = "abcdefghijklmnopqrstuvwxyz1234567890"

# Bad: C-style
index = random.randint(0, len(letters) - 1)
item = letters[index]
print(item)

# Pythonic version
py_item = random.choice(letters)
print(py_item)
