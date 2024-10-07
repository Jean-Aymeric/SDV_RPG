class BonusCharacteristic:
    def __init__(self, characteristic, bonus):
        self.__characteristic = characteristic
        self.__bonus = bonus

    @property
    def Characteristic(self):
        return self.__characteristic
    @property
    def Bonus(self):
        return self.__bonus

