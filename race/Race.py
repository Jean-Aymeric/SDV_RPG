from abc import ABC
from BonusCharacteristic import BonusCharacteristic
from Named import Named
from characteristic.Characteristic import Characteristic


class Race(Named, ABC):
    def __init__(self, name: str):
        super().__init__(name)
        self.__bonusCharacteristics = []

    def addBonusCharacteristic(self, characteristic: Characteristic, bonus : int):
        self.__bonusCharacteristics.append(BonusCharacteristic(characteristic, bonus))

    def getBonusFromCharacteristic(self, characteristic: Characteristic):
        for bonusCharacteristic in self.__bonusCharacteristics:
            if bonusCharacteristic.Characteristic.Name == characteristic.Name:
                return bonusCharacteristic.Bonus
        return 0
