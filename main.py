import copy

class Person:
    def __init__(self):
        self.förnamn = ''

person1 = Person()
person1.förnamn = 'Hjalmar'

person2 = Person()
person2.förnamn = ''

class Bil:
    def __init__(bil):
        bil.reg = ''
        bil.ägare = Person()
        bil.fab = ''
        bil.årsmodell = ''
        bil.tjänstvikt = ''
        bil.motor = ''

bil1 = Bil()
bil1.reg = 'DEU23G'
bil1.ägare = person1.förnamn
bil1.fab = 'Kia'
bil1.årsmodell = '2023'
bil1.tjänstvikt = '2 530 kg'
bil1.motor = '1000hk'

bil2 = Bil()
bil2.reg = 'SKI BID'
bil2.ägare = person2.förnamn
bil2.fab = 'Lambo'
bil2.årsmodell = '1885'
bil2.tjänstvikt = '1000kg'
bil2.motor = '0.5hk'

print(f'Första bilen har, Regnummer [{bil1.reg}], Ägare [{bil1.ägare}], fabrikat [{bil1.fab}], årsmodell [{bil1.årsmodell}], tjänstevikt [{bil1.tjänstvikt}], motorefeckt [{bil1.motor}]')
print(f'Andra bilen har, Regnummer [{bil2.reg}], Ägare [{bil2.ägare}], fabrikat [{bil2.fab}], årsmodell [{bil2.årsmodell}], tjänstevikt [{bil2.tjänstvikt}], motorefeckt [{bil2.motor}]')