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
    def __init__(self,name,desc,cost,target):
        self.name = name
        self.desc = desc
        self.cost = cost
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
        self.lvl = 0
x = ""
#melee
Punch = StandardAbility("Punch","A fairly weak but universal form of hating someone.","melee",40,0,"kinetic","enemy")
Swift_strike = AdvancedAbility("Swift strike","A swift double strike",0,"enemy")
#Swift_strike = StandardAbility("Swift strike","A swift double strike.","melee",20,0,"kinetic")

#ranged
LROne_Blaster = StandardAbility("LR-1 Blaster","A standard issue energy blaster.","ranged",30,1,"energy","enemy")

#tactical
Railgun = StandardAbility("Railgun","A powerful railgun which accelerates a bullet to immense speeds.","ranged",150,0,"kinetic","enemy")

#characters
Rangewave = Character("Rangewave","Proficient fighter.",1,1,1,1,1250,0,20,Railgun)
Rangewave.ability = [Punch,Swift_strike,LROne_Blaster,Railgun]
Rangewave.lvl = 1

#enemy abilities
Pounce = EnemyAbility("Pounce","A quick and easy pounce","melee",20,"team")

#enemies
Spider = Enemy("Spider","A spider",500,0,0)
Spider.ability = [[Pounce,100]]
Spider.lvl = 1

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
        # q = (f"{q}, {x+1}. {append}")
        q = (f"{q} {append}")
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

# def attack(character,ability,team,enemies):
#     character = team[character-1]
#     ability = ability-1
#     while True:
#         if type(character.ability[ability]) == StandardAbility:
#             if character.ability[ability].target == "enemy":
#                 target = findTarget(enemies)
#             else:
#                 target = findTarget(team)
#             if target == "cancel":
#                 return "cancel"
#             if character.ability[ability].expType == "melee":
#                 proficiency = character.melee
#             if character.ability[ability].expType == "ranged":
#                 proficiency = character.range
#             if character.ability[ability].expType == "medicine":
#                 proficiency = character.med
#             if character.ability[ability].expType == "tactic":
#                 proficiency = character.tactic
#             if character.ability[ability].type == "kinetic":
#                 damage = character.ability[ability].value * proficiency - enemies[target].armour
#             if character.ability[ability].type == "energy":
#                 damage = character.ability[ability].value * proficiency - enemies[target].shield
#             if damage < 0:
#                 damage = 0
#             print(f"The enemies health was {enemies[target].hp}")
#             enemies[target].hp -= damage
#             print(f"The enemies health is now {enemies[target].hp}")
#             return ""

# def choose(mcharacter,team,tactical,enemies):
    # q = listText(team[character-1].ability,"cancel",f"{team[character-1].super.name} ({tactical}%)")
    # while True:
    #     answer = input(f"Which ability would you like to use? {q}")
    #     if answer == "cancel":
    #         cancel = True
    #         break
    #     if answer == "1":
    #         ability = 0
    #         # value = attack(character,1,team,enemies)
    #         break
    #     elif answer == "2":
    #         ability = 1
    #         # value = attack(character,2,team,enemies)
    #         break
    #     elif answer == "3":
    #         ability = 2
    #         # value = attack(character,3,team,enemies)
    #         break
    #     elif answer == "4" and tactical != 100:
    #         input("The ability must charge to 100% before it can be used. ")
    #     elif answer == "4":
    #         ability = 3
    #         # value = attack(character,team[character-1].super,team,enemies)
    #         break
    #     else:
    #         input("You must write a valid number.")
    #         character = team[character-1]
    #     ability = ability-1
    #     while True:
    #         if type(character.ability[ability]) == StandardAbility:
    #             if character.ability[ability].target == "enemy":
    #                 target = findTarget(enemies)
    #             else:
    #                 target = findTarget(team)
    #             if target == "cancel":
    #                 cancel = True
    #                 break
    #             if character.ability[ability].expType == "melee":
    #                 proficiency = character.melee
    #             if character.ability[ability].expType == "ranged":
    #                 proficiency = character.range
    #             if character.ability[ability].expType == "medicine":
    #                 proficiency = character.med
    #             if character.ability[ability].expType == "tactic":
    #                 proficiency = character.tactic
    #             if character.ability[ability].type == "kinetic":
    #                 damage = character.ability[ability].value * proficiency - enemies[target].armour
    #             if character.ability[ability].type == "energy":
    #                 damage = character.ability[ability].value * proficiency - enemies[target].shield
    #             if damage < 0:
    #                 damage = 0
    #             print(f"The enemies health was {enemies[target].hp}")
    #             enemies[target].hp -= damage
    #             print(f"The enemies health is now {enemies[target].hp}")
    # if cancel == True:
    #     return character
    # else:
    #     return ""
        
def combat(team,enemies):
    energy = 0
    tactical = 0
    cancel = False
    activeTeam = team
    livingTeam = team
    for i in range(len(team)):
        team[i].hp = team[i].hp * team[i].lvl
    for i in range(len(enemies)):
        enemies[i].hp = enemies[i].hp * enemies[i].lvl
    character = ""
    while len(livingTeam) > 0 or len(enemies) > 0:
        energy += 1
        while len(livingTeam) > 0:
            cancel = False
            activeTeam = team
            character = ""
            q = listText(activeTeam,"inspect","")
            answer = input(f"Which character would you like to act? {q}")
            if answer == "1":
                characterID = 0
            elif answer == "2" and len(activeTeam) > 1:
                characterID = 1
            elif answer == "3" and len(activeTeam) > 2:
                characterID = 2
            elif answer == "inspect":
                print("\nYour team consists of:")
                for i in range(len(enemies)):
                    print(f'''  -{livingTeam[i].name} with {livingTeam[i].hp} health.''')
                print(f"The tactcial ability is at {tactical}%.")
                print(f"The energy is at {energy}.")
                print("\nThe enemies are:")
                for i in range(len(enemies)):
                    print(f'''  -{enemies[i].name} with {enemies[i].hp} health.\n''')
                continue
            else:
                input("You must write a valid number.")
                continue
            q = listText(team[characterID].ability,"cancel",f"({tactical}%)")
            while True:
                answer = input(f"Which ability would you like to use? {q}")
                if answer == "cancel":
                    cancel = True
                    break
                if answer == "1":
                    ability = 0
                    if team[characterID].ability[ability].cost > energy:
                        input(f"This ability costs {team[characterID].ability[ability].cost} energy but you only have {energy} energy.")
                    elif team[characterID].ability[ability].cost > 0:
                        answer = input(f"This ability has a cost of {energy} energy. Type y to proceed:")
                        if answer == "y":
                            break
                elif answer == "2":
                    ability = 1
                    if team[characterID].ability[ability].cost > energy:
                        input(f"This ability costs {team[characterID].ability[ability].cost} energy but you only have {energy} energy.")
                    elif team[characterID].ability[ability].cost > 0:
                        answer = input(f"This ability has a cost of {energy} energy. Type y to proceed:")
                        if answer == "y":
                            break
                elif answer == "3":
                    ability = 2
                    if team[characterID].ability[ability].cost > energy:
                        input(f"This ability costs {team[characterID].ability[ability].cost} energy but you only have {energy} energy.")
                    elif team[characterID].ability[ability].cost > 0:
                        answer = input(f"This ability has a cost of {energy} energy. Type y to proceed:")
                        if answer == "y":
                            break
                elif answer == "4" and tactical != 100:
                    input("The ability must charge to 100% before it can be used. ")
                elif answer == "4":
                    ability = 3
                    break
                else:
                    input("You must write a valid number.")
            if cancel == True:
                continue
            character = team[characterID]
            while True:
                if type(character.ability[ability]) == StandardAbility:
                    if character.ability[ability].target == "enemy":
                        target = findTarget(enemies)
                    else:
                        target = findTarget(team)
                    if target == "cancel":
                        cancel = True
                        break
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
                    tactical += int((damage/10))
                    print(f"Tactical: {tactical}%")
                    energy -= team[characterID].ability[ability].cost
                    break
                if type(character.ability[ability]) == AdvancedAbility:
                    if character.ability[ability].target == "enemy":
                        target = findTarget(enemies)
                    else:
                        target = findTarget(team)
                    if target == "cancel":
                        cancel = True
                        break
                    abilityValue = character.ability[ability]
                    if abilityValue == Swift_strike:
                        for i in range(2):
                            proficiency = character.melee
                            damage = 20 * proficiency - enemies[target].armour
                            if damage < 0:
                                damage = 0
                            print(f"The enemies health was {enemies[target].hp}")
                            enemies[target].hp -= damage
                            print(f"The enemies health is now {enemies[target].hp}")
                            tactical += int((damage/10))
                            print(f"Tactical: {tactical}%")  
                    energy -= team[characterID].ability[ability].cost
                    break
            if cancel == True:
                continue
            if len(enemies) <= 0:
                break
            if character != "":
                print("1",team)
                activeTeam.pop(characterID)
                print("2",team)
            if activeTeam == []:
                break
        print("Your turn has ended.")
        break
        while len(enemies) > 0:
            break

def main():
    fullTeam = [Rangewave]
    enemies = [Spider]
    combat(fullTeam,enemies)

main()