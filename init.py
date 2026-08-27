from math import pi

class Person:
    def __init__(self):
        self.förnamn = ''
        self.efternamn = ''

class Bok:
    def __init__(self):
        self.boktyp = ''
        self.ägare = None

bok=Bok()
bok.boktyp = 'Yaoi'

klas = Person()
klas.förnamn = 'Klas'
klas.efternamn = 'Olsson'
bok.ägare = klas

class O:
    def __init__(self, x=0, y=0, r=0.0):
        self.x=0
        self.y=0
        self.r=0

    def set_r(self, r):
        assert r > 0
        self.r = r

    def area(self):
        return pi * self.r ** 2

    def omkr(self):
        return 2* pi * self.r

cirkel = O()
input = float(input("Radie?"))

cirkel.set_r(input)

print("Area", cirkel.area())