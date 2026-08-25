

class Bankkonto:
    def __init__(self):
        self.kontohavare = None
        self.saldo = 0

k = Bankkonto()
k.kontohavare = Person()
k.kontohavare.förnamn = 'Hjalmar'