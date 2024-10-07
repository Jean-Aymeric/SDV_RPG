from Character import Character
from characteristic.Dexterity import Dexterity
from characteristic.Strength import Strength
from job.Warrior import Warrior
from race.Elf import Elf
from race.Human import Human

tom = Character("Tom", Warrior(), Elf())

print(tom.getMeleeAttack())
print(tom.getModifierFromCharacteristic(Strength()))
print(tom.getValueFromCharacteristic(Strength()))
print(tom.getValueFromCharacteristic(Dexterity()))
