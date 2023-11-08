class StandardAbility:
    def __init__(self,name,desc,proficiency,value,cost,type):
        self.name = name
        self.desc = desc        
        self.expType = proficiency
        self.value = value
        self.cost = cost
        self.type = type

class AdvancedAbility:
    def __init__(self,name,desc,type):
        self.name = name
        self.desc = desc
        self.type = type

class Character:
    def __init__(self,name,desc,level,melee,ranged,medicine,tactic,health,armour,shield):
        self.name = name
        self.desc = desc
        self.lvl = level
        self.melee = melee
        self.range = ranged
        self.med = medicine
        self.tactic = tactic
        self.hp = health
        self.armour = armour
        self.shield = shield

#melee
Punch = StandardAbility("Punch","A fairly weak but universal form of hating someone.","melee",40,0,"kinetic")
Swift_strike = StandardAbility("Swift strike","A swift double strike.","melee",20,0,"kinetic")

#ranged
LROne_Blaster = StandardAbility("LR-1 Blaster","A standard issue energy blaster.","ranged",30,1,"energy")

#tactical
Railgun = StandardAbility("Railgun","A powerful railgun which accelerates a bullet to immense speeds.","ranged",150,0,"kinetic")

def main():
    if type(Railgun) == AdvancedAbility:
        print("success")

main()