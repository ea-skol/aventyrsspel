#classes
class StandardAbility:
    def __init__(self,name,desc,proficiency,value,cost,type,target):
        self.name = name
        self.desc = desc        
        self.expType = proficiency
        self.value = value
        self.cost = cost
        self.type = type
        self.target = target

class AdvancedAbility:
    def __init__(self,name,desc,cost,type,target):
        self.name = name
        self.desc = desc
        self.cost = cost
        self.type = type
        self.target = target

class EnemyAbility:
    def __init__(self,name,desc,type,value,target):
        self.name = name
        self.desc = desc
        self.type = type
        self.value = value
        self.target = target

class Character:
    def __init__(self,name,desc,melee,ranged,medicine,tactic,health,armour,shield,super):
        self.name = name
        self.desc = desc
        self.lvl = 1
        self.melee = melee
        self.range = ranged
        self.med = medicine
        self.tactic = tactic
        self.hp = health
        self.armour = armour
        self.shield = shield
        self.ability = []
        self.super = super
        self.energy = 0

class Enemy:
    def __init__(self,name,desc,health,armour,shield):
        self.name = name
        self.desc = desc
        self.hp = health
        self.armour = armour
        self.shield = shield
        self.ability = []
        self.energy = 0

#melee
Punch = StandardAbility("Punch","A fairly weak but universal form of hating someone.","melee",40,0,"kinetic","enemy")
Swift_strike = AdvancedAbility("Swift strike","A swift double strike",0,"kinetic","enemy")
#Swift_strike = StandardAbility("Swift strike","A swift double strike.","melee",20,0,"kinetic")

#ranged
LROne_Blaster = StandardAbility("LR-1 Blaster","A standard issue energy blaster.","ranged",30,1,"energy","enemy")

#tactical
Railgun = StandardAbility("Railgun","A powerful railgun which accelerates a bullet to immense speeds.","ranged",150,0,"kinetic","enemy")

#characters
Rangewave = Character("Rangewave","Proficient fighter.",2,1,1,2,1250,0,20,Railgun)
Rangewave.ability = [Punch,Swift_strike,LROne_Blaster]

#enemy abilities
Pounce = EnemyAbility("Pounce","A quick and easy pounce","melee",20,"team")

#enemies
Spider = Enemy("Spider","A spider",500,0,0)
Spider.ability = [[Pounce,100]]

# print(f"The weight of this spiders pounce is {Spider.ability[0][1]}")
#how multiple enemies??? They would all be the same, how copy objects

# enemies = [Spider,Spider]
# print(enemies[0].ability[0][1])
# enemy1 = Spider
# enemy1.ability[0][1] = 1
# print("weight:",enemy1.ability[0][1])

#functions
def listText(list,prepend,append):
    if prepend != "":
        q = f"[{prepend}, 1. {list[0].name}"
    else:
        q = f"[1. {list[0].name}"
    for x in range (1,len(list)):
        q = (f"{q}, {x+1}. {list[x].name}")
    if append != "":
        x += 1
        q = (f"{q}, {x+1}. {append}")
    else:
        q = (f"{q}]")
    return q

def findTarget(side):
    q = listText(side,"cancel","")
    while True:
        answer = (input(f"Choose a target: {q}"))
        if answer == "cancel":
            return "cancel"
        try: 
            answer = int(answer)
        except ValueError:
            input("You must write a valid number.")
        if answer > len(side):
            input("You must write a valid number.")
            continue
        return answer-1

def attack(character,ability,team):
    character = team[character-1]
    ability = ability-1
    while True:
        if type(character.ability[ability]) == StandardAbility:
            if character.ability[ability].target == "enemy":
                target = findTarget(enemies)
            else:
                target = findTarget(team)
            if target == "cancel":
                return "cancel"
            if character.ability[ability].expType == "melee":
                proficiency = character.melee
            if character.ability[ability].expType == "ranged":
                proficiency = character.range
            if character.ability[ability].expType == "medicine":
                proficiency = character.med
            if character.ability[ability].expType == "tactic":
                proficiency = character.tactic
            if character.ability[ability].type == "kinetic":
                damage = character.ability[ability].value * proficiency - enemies[target].armour
            if character.ability[ability].type == "energy":
                damage = character.ability[ability].value * proficiency - enemies[target].shield
            if damage < 0:
                damage = 0
            print(f"The enemies health was {enemies[target].hp}")
            enemies[target].hp -= damage
            print(f"The enemies health is now {enemies[target].hp}")
            return ""


def choose(character,team):
    q = listText(team[character-1].ability,"cancel",f"{team[character-1].super.name} ({tactical}%)")
    while True:
        answer = input(f"Which ability would you like to use? {q}")
        if answer == "cancel":
            return ""
        if answer == "1":
            value = attack(character,1,team)
            break
        elif answer == "2":
            value = attack(character,2,team)
            break
        elif answer == "3":
            value = attack(character,3,team)
            break
        elif answer == "4" and tactical != 100:
            input("The ability must charge to 100% before it can be used. ")
        elif answer == "4":
            value = attack(character,team[character-1].super,team)
            break
        else:
            input("You must write a valid number.")
    if value == "":
        return character
    else:
        return ""


def combat(team):
    activeTeam = team
    livingTeam = team
    character = ""
    while len(livingTeam) > 0 or len(enemies) > 0:
        while len(livingTeam) > 0:
            activeTeam = fullTeam
            character = ""
            q = listText(activeTeam,"","")
            answer = input(f"Which character would you like to act? {q}")
            if answer == "1":
                character = choose(1,livingTeam)
            elif answer == "2" and len(activeTeam) > 1:
                character = choose(2,livingTeam)
            elif answer == "3" and len(activeTeam) > 2:
                character = choose(3,livingTeam)
            else:
                input("You must write a valid number.")
                continue
            if len(enemies) <= 0:
                break
            if character != "":
                print("1",fullTeam)
                activeTeam.pop(character-1)
                print("2",fullTeam)
            if activeTeam == []:
                break
        print("Your turn has ended.")
        break
        while len(enemies) > 0:
            break



def main():
    # if type(Railgun) == AdvancedAbility:
    #     print("success")
    pass

fullTeam = [Rangewave]
enemies = [Spider]
tactical = 0
combat(fullTeam)
main()