class Animal:
    def __init__(self, age):
        self.age = age
    def eat(self):
        return "nom nom"

class Dog(Animal):
    def __init__(self, age, name = "Bilbo Waggins"):
        super().__init__(age)
        self.name = name
    def eat(self):
        return("Gobble Gobble")

fido = Dog()
print(fido.eat())
