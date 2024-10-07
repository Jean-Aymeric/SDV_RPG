from characteristic.Dexterity import Dexterity
from characteristic.Strength import Strength
from race.Race import Race


class Elf(Race):
    def __init__(self):
        super().__init__("Elfe")
        self.addBonusCharacteristic(Strength(), -2)
        self.addBonusCharacteristic(Dexterity(), +2)
