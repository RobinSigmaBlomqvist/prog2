#Superclass
class Djur:
    def låta(self):
        print("Player attacks")

#Subclass
class Cat(Djur):
    def låta(self):
        print("Meouw Meouw")

class Dog(Djur):
    def låta(self):
        print("Whof Whof")

class Human(Djur):
    def låta(self):
        print("Hejsan svejsan")


players = [
    Cat(),
    Dog(),
    Human()
]

for djur in players:
    djur.låta()
