from copy import *
import random as rand

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
    def __init__(self,name,desc,value,expType,cost,type,target):
        self.name = name
        self.desc = desc
        self.value = value
        self.expType = expType
        self.cost = cost
        self.type = type
        self.target = target

class StandardEnemyAbility:
    def __init__(self,name,desc,type,value,target):
        self.name = name
        self.desc = desc
        self.type = type
        self.value = value
        self.target = target
        self.weight = 0

class Character:
    def __init__(self,name,desc,melee,ranged,medicine,tactic,health,armour,shield,super):
        self.name = name
        self.desc = desc
        self.lvl = 1
        self.defaultValues = [melee,ranged,medicine,tactic,health]
        self.melee = melee
        self.range = ranged
        self.med = medicine
        self.tactic = tactic
        self.xp = 0
        self.maxhp = health
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
        self.maxhp = health
        self.armour = armour
        self.shield = shield
        self.ability = []
        self.energy = 0
        self.lvl = 1

#melee
Punch = StandardAbility("Punch","A fairly weak but universal form of hating someone.","melee",40,0,"kinetic","enemy")
Swift_strike = AdvancedAbility("Swift strike","A swift double strike",20,"melee",0,"kinetic","enemy")
Energy_blade = AdvancedAbility("Energy blade","A blade of energy.",10,"melee",0,"energy","")

#ranged
LROne_Blaster = StandardAbility("LR-1 Blaster","A standard issue energy blaster.","ranged",30,2,"energy","enemy")
Flame_blast = StandardAbility("Flame blast","A lunge of fire.","ranged",20,0,"kinetic","enemy")

#ability
Restoration = AdvancedAbility("Restoration","Restore some health.",40,"medicine",1,"","team")

#tactical
Railgun = StandardAbility("Railgun","A powerful railgun which accelerates a bullet to immense speeds.","ranged",150,0,"kinetic","enemy")
Powerblade = StandardAbility("Powerblade","A blade of pure power.","melee",130,0,"energy","enemy")

#characters
Rangewave = Character("Rangewave","Proficient fighter.",2,1,1,1,950,0,20,Railgun)
Rangewave.ability = [Punch,Swift_strike,LROne_Blaster,Railgun]

Firefly = Character("Firefly","Fiery warrior",1,2,1,2,800,10,0,Powerblade)
Firefly.ability = [Flame_blast,Restoration,LROne_Blaster,Powerblade]

Caveman = Character("Caveman","Is caveman.",1,1,1,1,1250,0,20,Railgun)
Caveman.ability = [Punch,Swift_strike,LROne_Blaster,Railgun]

#enemy abilities
Pounce = StandardEnemyAbility("Pounce","A quick and easy pounce","kinetic",20,"team")
Shoot = StandardEnemyAbility("Shoot","Shoots","energy",30,"team")
Charge = StandardEnemyAbility("Charge","Charges","kinetic",40,"team")

#enemies
Spider = Enemy("Spider","A spider",300,0,0)
Spider.ability = [copy(Pounce)]
Spider.ability[0].weight = 1

Bullseye = Enemy("Bullseye","Famed bounty hunter",600,20,10)
Bullseye.ability = [copy(Shoot),copy(Charge)]
Bullseye.ability[0].weight = 3
Bullseye.ability[1].weight = 1


# print(f"The weight of this spiders pounce is {Spider.ability[0][1]}")

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
    q = listText(side,"c(ancel)","")
    while True:
        answer = (input(f"Choose a target: {q}"))
        if answer == "c":
            return "c"
        try: 
            answer = int(answer)
        except ValueError:
            input("You must write a valid number.")
            continue
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
        
def filterList(list,antiFilter):
    returnValue = []
    for i in range(len(list)):
        if list[i] not in antiFilter:
            returnValue.append(list[i])
    return returnValue

def dealDamage(caster,abilityID,casterList,targetList,targetID):
    if caster.ability[abilityID].expType == "melee":
        proficiency = caster.melee
    if caster.ability[abilityID].expType == "ranged":
        proficiency = caster.range
    if caster.ability[abilityID].expType == "medicine":
        proficiency = caster.med
    if caster.ability[abilityID].expType == "tactic":
        proficiency = caster.tactic
    if caster.ability[abilityID].type == "kinetic":
        damage = caster.ability[abilityID].value * proficiency - targetList[targetID].armour
    if caster.ability[abilityID].type == "energy":
        damage = caster.ability[abilityID].value * proficiency - targetList[targetID].shield
    if damage < 0:
        damage = 0
    print(f"The enemy's health was {targetList[targetID].hp}")
    targetList[targetID].hp -= damage
    if targetList[targetID].hp < 1:
        targetList[targetID].hp = 0
    print(f"The enemy's health is now {targetList[targetID].hp}")
    return targetList,damage

def tacticalCalc(inputDamage,charge):
    if charge + int(inputDamage/6) > 100:
        return 100-charge
    else:
        return int(inputDamage/6)

def combat(team,enemies):
    xp = 0
    energy = 0
    tactical = 0
    cancel = False
    activeTeam = copy(team)
    livingTeam = team
    turnCounter = 0
    for i in range(len(team)):
        team[i].hp = team[i].hp * team[i].lvl
    for i in range(len(enemies)):
        enemies[i].hp = enemies[i].hp * enemies[i].lvl
    character = ""
    while len(livingTeam) > 0 and len(enemies) > 0:
        turnCounter += 1
        energy += 1
        activeTeam = copy(team)
        while len(livingTeam) > 0:
            cancel = False
            character = ""
            q = listText(activeTeam,"i(nspect)","")
            answer = input(f"Which character would you like to act? {q}")
            if answer == "1":
                characterID = 0
            elif answer == "2" and len(activeTeam) > 1:
                characterID = 1
            elif answer == "3" and len(activeTeam) > 2:
                characterID = 2
            elif answer == "i":
                print("\nYour team consists of:")
                for i in range(len(livingTeam)):
                    print(f'''  -{livingTeam[i].name} with {livingTeam[i].hp} of {livingTeam[i].maxhp} hp.''')
                print(f"The tactical ability is at {tactical}%.")
                print(f"The energy is at {energy}.")
                print("\nThe enemies are:")
                for i in range(len(enemies)):
                    print(f'''  -{enemies[i].name} with {enemies[i].hp} of {enemies[i].maxhp} hp.''')
                print()
                continue
            else:
                input("You must write a valid number.")
                continue
            q = listText(activeTeam[characterID].ability,"c(ancel)",f"({tactical}%)")
            while True:
                answer = input(f"Which ability would you like to use? {q}")
                if answer == "c":
                    cancel = True
                    break
                if answer == "1":
                    ability = 0
                    if activeTeam[characterID].ability[ability].cost > energy:
                        input(f"This ability costs {activeTeam[characterID].ability[ability].cost} energy but you only have {energy} energy.")
                    elif activeTeam[characterID].ability[ability].cost > 0:
                        answer = input(f"This ability has a cost of {activeTeam[characterID].ability[ability].cost} energy and you have {energy} energy. Type y to proceed:")
                        if answer == "y":
                            break
                    else:
                        break
                elif answer == "2":
                    ability = 1
                    if activeTeam[characterID].ability[ability].cost > energy:
                        input(f"This ability costs {activeTeam[characterID].ability[ability].cost} energy but you only have {energy} energy.")
                    elif activeTeam[characterID].ability[ability].cost > 0:
                        answer = input(f"This ability has a cost of {activeTeam[characterID].ability[ability].cost} energy and you have {energy} energy. Type y to proceed:")
                        if answer == "y":
                            break
                    else:
                        break
                elif answer == "3":
                    ability = 2
                    if activeTeam[characterID].ability[ability].cost > energy:
                        input(f"This ability costs {activeTeam[characterID].ability[ability].cost} energy but you only have {energy} energy.")
                    elif activeTeam[characterID].ability[ability].cost > 0:
                        answer = input(f"This ability has a cost of {activeTeam[characterID].ability[ability].cost} energy and you have {energy} energy. Type y to proceed:")
                        if answer == "y":
                            break
                    else:
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
            character = activeTeam[characterID]
            while True:
                if type(character.ability[ability]) == StandardAbility:
                    if character.ability[ability].target == "enemy":
                        targetID = findTarget(enemies)
                    elif character.ability[ability].target == "team":
                        targetID = findTarget(enemies)
                    if targetID == "c":
                        cancel = True
                        break
                    enemies,damage = dealDamage(character,ability,activeTeam,enemies,targetID)
                    # if character.ability[ability].target == "enemy":
                    #     target = findTarget(enemies)
                    # else:
                    #     target = findTarget(team)
                    # if target == "c":
                    #     cancel = True
                    #     break
                    # if character.ability[ability].expType == "melee":
                    #     proficiency = character.melee
                    # if character.ability[ability].expType == "ranged":
                    #     proficiency = character.range
                    # if character.ability[ability].expType == "medicine":
                    #     proficiency = character.med
                    # if character.ability[ability].expType == "tactic":
                    #     proficiency = character.tactic
                    # if character.ability[ability].type == "kinetic":
                    #     damage = character.ability[ability].value * proficiency - enemies[target].armour
                    # if character.ability[ability].type == "energy":
                    #     damage = character.ability[ability].value * proficiency - enemies[target].shield
                    # if damage < 0:
                    #     damage = 0
                    # print(f"The enemy's health was {enemies[target].hp}")
                    # enemies[target].hp -= damage
                    # if enemies[target].hp < 1:
                    #     enemies[target].hp = 0
                    # print(f"The enemy's health is now {enemies[target].hp}")
                    tactical += tacticalCalc(damage,tactical)
                    if ability == 3:
                        tactical = 0
                    print(f"Tactical: {tactical}%\n")
                    energy -= activeTeam[characterID].ability[ability].cost
                    break
                if type(character.ability[ability]) == AdvancedAbility:
                    # if character.ability[ability].target == "enemy":
                    #     target = findTarget(enemies)
                    # elif character.ability[ability].target == "team":
                    #     target = findTarget(livingTeam)
                    # else:
                    #     target = ""
                    # if target == "c":
                    #     cancel = True
                    #     break
                    abilityValue = character.ability[ability]
                    if abilityValue == Swift_strike:
                        if character.ability[ability].target == "enemy":
                            targetID = findTarget(enemies)
                        elif character.ability[ability].target == "team":
                            targetID = findTarget(enemies)
                        if targetID == "c":
                            cancel = True
                            break
                        enemies,damage = dealDamage(character,ability,activeTeam,enemies,targetID)
                        tactical += tacticalCalc(damage,tactical)
                        print(f"Tactical: {tactical}%\n")
                        enemies,damage = dealDamage(character,ability,activeTeam,enemies,targetID)
                        # proficiency = character.melee
                        # damage = character.ability[ability].value * proficiency - enemies[target].armour
                        # if damage < 0:
                        #     damage = 0
                        # print(f"The enemy's health was {enemies[target].hp}")
                        # enemies[target].hp -= damage
                        # if enemies[target].hp < 1:
                        #     enemies[target].hp = 0
                        # print(f"The enemy's health is now {enemies[target].hp}")
                        tactical += tacticalCalc(damage,tactical)
                        print(f"Tactical: {tactical}%\n")
                    if abilityValue == Restoration:
                        livingTeam[target].hp += abilityValue.value
                        if livingTeam[target].hp > livingTeam[target].maxhp:
                            livingTeam[target].hp = livingTeam[target].maxhp
                        input(f"{livingTeam[target].name} was healed to {livingTeam[target].hp} health.")
                    if abilityValue == Energy_blade:
                        for i in range(len(enemies)):
                            proficiency = character.melee
                            damage = character.ability[ability].value * proficiency - enemies[i].armour
                            if damage < 0:
                                damage = 0
                            print(f"The enemy's health was {enemies[i].hp}")
                            enemies[i].hp -= damage
                            if enemies[i].hp < 1:
                                enemies[i].hp = 0
                            print(f"The enemy's health is now {enemies[i].hp}")
                            tactical += tacticalCalc(damage,tactical)
                            print(f"Tactical: {tactical}%\n")

                    energy -= livingTeam[characterID].ability[ability].cost
                    break
            if cancel == True:
                continue
            if character != "":
                activeTeam.pop(characterID)
                i = 0
                while True:
                    if enemies[i].hp <= 0:
                        xp += (enemies[i].maxhp)/10
                        xp = int(xp)
                        enemies.pop(i)
                    else:
                        i += 1
                    if i >= len(enemies):
                        break
            if activeTeam == []:
                break
            if len(enemies) <= 0:
                break
        input("Your turn has ended.")
        while len(enemies) > 0:
            for i in range(len(enemies)):
                totalWeight = 0
                addedWeight = 0
                for p in range(len(enemies[i].ability)):
                    totalWeight += enemies[i].ability[p].weight
                weight = rand.randint(1,totalWeight)
                for p in range(len(enemies[i].ability)):
                    addedWeight += enemies[i].ability[p].weight
                    if enemies[i].ability[p].weight > addedWeight-weight:
                        ability = p
                target = rand.randint(1,len(livingTeam))
                target -= 1
                if type(enemies[i].ability[ability]) == StandardEnemyAbility:
                    if enemies[i].ability[ability].type == "kinetic":
                        damage = enemies[i].ability[ability].value * enemies[i].lvl - livingTeam[target].armour
                    if enemies[i].ability[ability].type == "energy":
                        damage = enemies[i].ability[ability].value * enemies[i].lvl - livingTeam[target].shield
                    if damage < 0:
                        damage = 0
                    print()
                    print(f"{enemies[i].name} uses {enemies[i].ability[ability].name} against {livingTeam[target].name}.")
                    print(f"{livingTeam[target].name}'s health was {livingTeam[target].hp}")
                    livingTeam[target].hp -= damage
                    if livingTeam[target].hp < 1:
                        livingTeam[target].hp = 0
                    print(f"{livingTeam[target].name}'s health is now {livingTeam[target].hp}")
                    tactical += tacticalCalc(damage,tactical)
                    if tactical > 100:
                        tactical = 100
                    input(f"Tactical: {tactical}%")
                i = 0
                while True:
                    if livingTeam[i].hp <= 0:
                        livingTeam.pop(i)
                    else:
                        i += 1
                    if i >= len(livingTeam):
                        break
                if livingTeam == []:
                    break
            print()
            break
    if livingTeam == []:
        input("You failed!")
    elif enemies == []:
        input(f"Your characters gained {xp}xp!")
        for i in range(len(team)):
            team[i].xp += xp
            if team[i].xp > team[i].lvl*100:
                while team[i].xp > team[i].lvl*100:
                    team[i].xp -= team[i].lvl*100
                    team[i].lvl += 1
                team[i].melee = team[i].defaultValues[0] * team[i].lvl
                team[i].range = team[i].defaultValues[1] * team[i].lvl
                team[i].med = team[i].defaultValues[2] * team[i].lvl
                team[i].tactic = team[i].defaultValues[3] * team[i].lvl
                team[i].hp = team[i].defaultValues[4] + 100 * team[i].lvl
                team[i].maxhp = team[i].defaultValues[4] + 100 * team[i].lvl
        return team

def edit(team,all,abilities):
    while True:
        answer = input("Would you like to edit your characters or change your team? [exit, e(dit), c(hange)]")
        if answer == "exit":
            return team,all
        elif answer == "e": 
            while True:
                q = listText(all,"c(ancel)","")
                answer = (input(f"Choose a team member: {q}"))
                if answer == "c":
                    break
                try:
                    answer = int(answer)
                except ValueError:
                    input("You must write a valid number.")
                    continue
                answer -= 1
                characterID = answer
                if characterID > len(all):
                    input("You must write a valid number.")
                    continue
                while True:
                    q = listText(all[characterID].ability,"c(ancel)","")
                    answer = input(f"Choose an ability to edit or inspect: {q}")
                    if answer == "c":
                        break
                    try:
                        answer = int(answer)
                    except ValueError:
                        input("You must write a valid number.")
                        continue
                    answer -= 1
                    abilityID = answer
                    if abilityID > 3:
                        input("You must write a valid number.")
                        continue
                    if abilityID == 3:
                        input(f"{all[characterID].ability[abilityID].name}: {all[characterID].ability[abilityID].desc} (This ability can not be replaced)")
                    else:
                        while True:
                            answer = input(f"Inspect or replace {all[characterID].ability[abilityID].name}? [c(ancel), i(nspect), r(eplace)]")
                            if answer == "c":
                                break
                            elif answer == "i":
                                input(f"{all[characterID].ability[abilityID].name}: {all[characterID].ability[abilityID].desc} This ability costs {all[characterID].ability[abilityID].cost} energy to use.")
                            elif answer == "r":
                                availableAbilities = filterList(abilities,all[characterID].ability)
                                if availableAbilities != []:
                                    q = listText(availableAbilities,"c(ancel)","")
                                    answer = input(f"Chose an ability to replace {all[characterID].ability[abilityID].name} with: {q}")
                                    if answer == "c":
                                        break
                                    try:
                                        answer = int(answer)
                                    except ValueError:
                                        input("You must write a valid number.")
                                        continue
                                    if answer > len(availableAbilities):
                                        input("You must write a valid number.")
                                        continue
                                    answer -= 1
                                    all[characterID].ability[abilityID] = availableAbilities[answer]
                                    q = listText(all[characterID].ability,"","")
                                    input(f"{all[characterID].name}'s abilities are now {q}.")
                                    break
                                else:
                                    input("You don't have any available abilities to replace this ability with.")
                            else:
                                input("You must write a valid input.")
                                continue
        elif answer == "c":
            while True:
                while True:
                    if len(team) != 3:
                        add_character = Character("Add character","There is currently no character in this slot.",0,0,0,0,0,0,0,"n/a")
                        team.append(add_character)
                    else:
                        break
                q = listText(team,"c(ancel)","")
                answer = input(f"Choose a team member to replace: {q}")
                if answer == "c":
                    break
                try:
                    answer = int(answer)
                except ValueError:
                    input("You must write a valid input.")
                    continue
                if answer > len(team):
                    input("You must write a valid input.")
                    continue
                characterID = answer-1
                if characterID+1 > len(team):
                    while True:
                        q = listText(all,"c(ancel)","")
                        answer == input(f"Which character would you like to add?")
                        if answer == "c":
                            break
                        try:
                            answer = int(answer)
                        except ValueError:
                            input("You must write a valid input.")
                            continue
                        answer -= 1
                        team[characterID] = all[answer]
                        break
                else:
                    while True:
                        answer = input(f"Inspect or replace? [c(ancel), i(nspect), r(eplace)]")
                        if answer == "c":
                            break
                        elif answer == "i":
                            print(f"{team[characterID].name}: {team[characterID].desc}")
                            print(f"{team[characterID].name} has {team[characterID].xp}xp and is at level {team[characterID].lvl}.")
                            print(f"Their proficiencies are: {team[characterID].melee} melee, {team[characterID].range} ranged, {team[characterID].med} medicine and {team[characterID].tactic} tactical.")
                            input(f"Their health is {team[characterID].hp}hp.")
                        elif answer == "r":
                            while True:
                                availableCharacters = filterList(all,team)
                                if availableCharacters != []:
                                    q = listText(availableCharacters,"c(ancel)","")
                                    answer = input(f",Which character would you like to replace {team[characterID].name} with? {q}")
                                    if answer == "c":
                                        break
                                    try:
                                        answer = int(answer)
                                    except ValueError:
                                        input("You must write a valid input.")
                                        continue
                                    answer -= 1
                                    team[characterID] = availableCharacters[answer]
                                    q = listText(team,"","")
                                    input(f"The team now consists of {q}.")
                                    break
                                else:
                                    input(f"You don't have any characters to replace {team[characterID].name} with.")
                                    break
                            break
                        else:
                            input("You must write a valid input.")
                            continue
        else:
            input("You must write a valid answer.")
            continue

def main():
    fullTeam = [Rangewave,Firefly]
    unlockedCharacters = [Rangewave,Firefly,Caveman]
    enemies = [copy(Spider),copy(Spider),copy(Bullseye)]
    unlockedAbilities = [Punch,Swift_strike,LROne_Blaster,Flame_blast,Restoration,Energy_blade]
    while True:
        enemies = [copy(Spider),copy(Spider),copy(Bullseye)]
        answer = input("Do smthng: [c(ombat), e(dit)]")
        if answer == "c":
            fullTeam = combat(fullTeam,enemies)
            answer = ""
        elif answer == "e":
            fullTeam,unlockedCharacters = edit(fullTeam,unlockedCharacters,unlockedAbilities)
            answer = ""
        elif answer == "b":
            answer = ""
            break

main()