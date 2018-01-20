False   # false false
[]      # empty lists/arrays are false
{}      # empty dictionaries are false
""      # empty strings are false
0       # zero ints are false
0.0     # zero floats are false
None    # None / null / nil pointers are false
Custom  # Custom __bool__ / __nonzero__


# Everything else is true!

class AClass:
    def __init__(self):
        self.data = []

    def add(self, item):
        self.data.append(item)

    def __bool__(self):
        # use inherent truthiness here. self.data empty is inherently false. With items, inherently true
        return True if self.data else False


a = AClass()

# a = FALSE

a.add("Thing")

# a = TRUE
