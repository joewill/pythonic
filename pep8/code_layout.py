def some_method():
    var x = 1  # indent spaces not tabs


def other_method():  # two blank lines between each method
    pass


def third_method():
    x = 1

    if x > 2:  # one blank line between logical groupings within a method
        return 1
    else:
        return 2


def forth_method():
    goodline = "Do your best not to have more than 79 characters in one line."


class AClass:
    def method_one(self):
        pass

    def method_two(self):  # One blank line between methods within a class
        pass

    def method_three(self):
        pass
