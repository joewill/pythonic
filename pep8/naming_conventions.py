# NAMES SHOULD BE DESCRIPTIVE
# DON'T MAKE ME GUESS WHAT THIS DOES

# Rule of thumb: If you need a comment to describe what a thing does.
# It probably needs a better name


# module  data_access

# constant, not changed at runtime
TRANSCATION_MODE = 'serializable'


class CustomerRepository:

    def __init__(self):
        self.db = create_db()
        self.mode = 'dev'

        def create_customer(self, name, email):
          #...


class RepositoryError(Exception):  # Exception classes should end in 'Error'
    pass


# Modules have short, lower case names
# Constants are uppercase
# Classes have CapWord names
# Variable and arguments are always lower case (use_underscores)
# Functions, methods are lowercase (use_underscores)
