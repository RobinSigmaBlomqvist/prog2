import copy

class Person:
    def __init__(self):
        self.förnamn = ''
        self.efternamn = ''

person1 = Person()
person1.förnamn = 'Hjalmar'

person2 = Person()
person2.förnamn = 'Kent'

class Bil:
    def __init__(bil, reg='', ägare=Person() ,fab='', årsmodell='', tjänstvikt='', motor=''):
        bil.reg = reg
        bil.ägare = ägare
        bil.fab = fab
        bil.årsmodell = årsmodell
        bil.tjänstvikt = tjänstvikt
        bil.motor = motor

bil1 = Bil('DEU23G', person1.förnamn,'Kia','2023','2 530 kg','1000hk')

bil2 = Bil('SKI BID',person2.förnamn,'Lambo','1885','1000kg','0.5hk')

print(f'Första bilen har, Regnummer [{bil1.reg}], Ägare [{bil1.ägare}], fabrikat [{bil1.fab}], årsmodell [{bil1.årsmodell}], tjänstevikt [{bil1.tjänstvikt}], motorefeckt [{bil1.motor}]')
print(f'Andra bilen har, Regnummer [{bil2.reg}], Ägare [{bil2.ägare}], fabrikat [{bil2.fab}], årsmodell [{bil2.årsmodell}], tjänstevikt [{bil2.tjänstvikt}], motorefeckt [{bil2.motor}]')