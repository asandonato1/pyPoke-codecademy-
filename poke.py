def isCounter(x, y):
    if x == "Fire" and y == "Water":
        return False
    elif x == "Water" and y == "Fire":
        return True
    elif x == "Fire" and y == "Grass":
        return True
    elif x == "Grass" and y == "Fire":
        return False
    else:
        return False
class Pokemon:
    def __init__(self, type, maxHp, currentHp, knock = False):
        self.type = type
        self.maxHp = maxHp
        self.currentHp = currentHp
        self.knock : bool= knock
    def loseHealth(self, currentHp, atk, type, enType):
        if atk > currentHp:
            self.knock = True
            print("Your Pokemon fainted!")
        elif self.type == "Fire" and enType == "Water":
            self.currentHp = currentHp - atk * 1.5
            print("Your pokemon has {} HP!".format(self.currentHp))
        elif self.type == enType:
            self.currentHp = currentHp - atk
            print("Your pokemon has {} HP!".format(self.currentHp))
        elif self.type == "Water" and enType == "Fire":
            print('You were attacked! It wasn\'t so effective... You didn\'t lose HP!')
        else:
            self.currentHp = currentHp - atk
            print("Your pokemon has {} HP!".format(self.currentHp))
    def regainHealth(self, currentHp, regain):
        gotBack = regain + currentHp
        print("You healed " + str(regain) +  "HP. You now have " + str(gotBack) + " HP")
    def attack(self, type, enType, enHP, pokeAtk):
        if isCounter(type, enType) == True and pokeAtk > enHP:
            atkTotal = pokeAtk * 1.5
            print("You knocked the other Pokemon out! You dealt " + str(atkTotal) + " damage!")
        elif isCounter(type, enType) == True:
            enHP = enHP - pokeAtk * 1.5
            print("You dealt " + str(pokeAtk) + " damage. The enemy Pokemon has " + str(enHP) + " HP")
        elif isCounter(type, enType) == False and pokeAtk > enHP:
            enHP = enHP - pokeAtk * 0.25
            pokeAtk = pokeAtk * 0.25
            print("You dealt " + str(pokeAtk) + " damage. The enemy has " + str(enHP) + " HP")
        elif type == enType:
            enHP = enHP - pokeAtk
            print("You dealt " + str(pokeAtk) + " damage. The enemy has " + str(enHP) + " HP")
        else:
            print("You didn'\t deal any damage.")

class Trainer(Pokemon):
    def __init__(self, pokeCount, name, potions, activePoke):
        self.pokeCount = pokeCount
        self.name = name
        self.potions = potions
        self.activePoke : int = activePoke

poke = Pokemon("Fire", 150, 100)
poke.loseHealth(currentHp=poke.currentHp, atk=50, type="Fire", enType="Fire")
poke.regainHealth(currentHp=poke.currentHp, regain=50)
poke.attack(type="Fire", enType="Fire", enHP=100, pokeAtk=150)
