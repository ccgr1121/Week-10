class Dog:
    def __init__(self, class_=None):
        self.class_ = class_
    def bark(self):
        return("woof")
    def get_name(self):
        return self._name
    def set_name(self, name):
        self_name = name
    def __str__(self_):
        return "Grrr"

fido = Dog("fido")
print(fido.class_)


# bilbo_waggins = Dog("Furlock Bones")
# print(bilbo_waggins._name)
# print(bilbo_waggins.bark())