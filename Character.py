from Named import Named
from characteristic.Characteristic import Characteristic
from characteristic.Strength import Strength
from job.Job import Job
from race.Race import Race


class Character(Named):
    def __init__(self, name: str, job : Job, race : Race):
        super().__init__(name)
        self.__characteristics = []
        self.__job = job
        self.__race = race
        self.__characteristics.append((Strength(),12))

    @property
    def Characteristics(self):
        return self.__characteristics

    @property
    def Job(self):
        return self.__job

    @property
    def Race(self):
        return self.__race

    def getValueFromCharacteristic(self, characteristic : Characteristic)-> int:
        for characteristicValue in self.__characteristics:
            if characteristicValue[0].Name == characteristic.Name:
                return characteristicValue[1] + self.getRaceBonusFromCharacteristic(characteristic)
        return 0 + self.getRaceBonusFromCharacteristic(characteristic)

    def getModifierFromCharacteristic(self, characteristic : Characteristic)-> int :
        return (self.getValueFromCharacteristic(characteristic) //2) -5

    def getMeleeAttack(self):
        return self.getModifierFromCharacteristic(Strength())+1

    def getRaceBonusFromCharacteristic(self, characteristic) -> int:
        return self.__race.getBonusFromCharacteristic(characteristic)





