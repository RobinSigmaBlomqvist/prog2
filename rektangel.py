class Rektangel:
    def __init__(self, x, y, höjd, bredd):
        self.x=x
        self.y=y
        self.höjd=höjd
        self.bredd=bredd

    def set_höjd(self, höjd):
        self.höjd = höjd

    def set_bredd(self, bredd):
            self.höjd = bredd

    def area(self):
         return self.höjd * self.bredd
    
    def omkrets(self):
        return 2 * (self.höjd + self.bredd)

r = Rektangel(10, 20, 5, 8)

print("Area:", r.area())
print("Omkrets:", r.omkrets())

r.set_höjd(10)
r.set_bredd(12)

print("Ny Area:", r.area())
print("Ny Omkrets:", r.omkrets())