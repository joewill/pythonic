name = 'Paige'
age = 4

# Create the string "Hi, I'm Micheal and I'm 43 years old."

# Bad Bad Not Good:
# print("Hi, I'm " + name + " and I'm " + age + " years old.")

# works, but not great
print("Hi, I'm " + name + " and I'm " + str(age) + " years old.")

# better
print("Hi, I'm %s and I'm %d years old." % (name, age))

# pythonic
print("Hi, I'm {} and I'm {} years old.".format(name, age))

data = {'day': 'Saturday', 'office': 'Home office', 'other': 'UNUSED'}
# print: On Saturday I was working in my Home office!
print("On {day} I was working in my {office}".format(**data))
