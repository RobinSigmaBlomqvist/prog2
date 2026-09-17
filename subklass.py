class Fordon:
    def __init__(self, fordonstyp, regnr):
        self.fordonstyp = fordonstyp
        self.regnr = regnr

class Lastbil(Fordon):
    def __init__(self, fordontyp, regnr, maxvikt):
        super().__init__(fordontyp, regnr)
        self.maxvikt = maxvikt

    def Honk(self):
        print('*Hoooooonk*')

class Motorcykel(Fordon):
    def __init__(self, fordonstyp, regnr, senastbesiktad):
        super().__init__(fordonstyp, regnr)
        self.senastbesiktad = senastbesiktad

    def Wheelie(self):
        print('*Sick ass wheelie*')



f1 = Lastbil("Lastbil", "ABC 123",'5000kg')
f2 = Motorcykel("Motorcykel", "sik 067", 1867)

print(vars(f1))
f1.Honk()

print(vars(f2))
f2.Wheelie()