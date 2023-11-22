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
    def __init__(self,name,desc,value,proficiency,cost,type,target):
        self.name = name
        self.desc = desc
        self.value = value
        self.expType = proficiency
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
Punch = StandardAbility("Punch","A fairly weak but universal form of hating someone.","melee",20,0,"kinetic","enemy")
Swift_strike = AdvancedAbility("Swift strike","A swift double strike",20,"melee",0,"kinetic","enemy")
Energy_blade = AdvancedAbility("Energy blade","A blade of energy which slices through every enemy.",10,"melee",0,"energy","")

#ranged
LROne_Blaster = StandardAbility("LR-1 Blaster","A standard issue energy blaster.","ranged",30,2,"energy","enemy")
Flame_blast = StandardAbility("Flame blast","A lunge of fire.","ranged",20,0,"kinetic","enemy")
Dual_blasters = AdvancedAbility("Dual blasters","Two medium-range blasters which deliver double the trouble.",15,"ranged",1,"energy","enemy")
XXI_Sniper = StandardAbility("XXI Sniper","A standard issue sniper rifle used by the VanGard.","ranged",30,0,"kinetic","enemy")

#ability
Restoration = AdvancedAbility("Restoration","Restore some health.",40,"medicine",1,"","team")

#tactical
Railgun = StandardAbility("Railgun","A powerful railgun which accelerates a bullet to immense speeds.","ranged",150,0,"kinetic","enemy")
Powerblade = StandardAbility("Powerblade","A blade of pure power.","melee",130,0,"energy","enemy")
Stand_off = AdvancedAbility("Stand off","Aim in on your target with high precision and deal extra damage.",1,"tactic",0,"","enemy")

#characters
Rangewave = Character("Rangewave","Proficient fighter of the VanGard.",2,1,1,1,950,0,20,Railgun)
Rangewave.ability = [Punch,XXI_Sniper,LROne_Blaster,Railgun]

Firefly = Character("Firefly","Fiery warrior and mechanic.",1,2,1,2,800,10,0,Powerblade)
Firefly.ability = [Flame_blast,Restoration,Energy_blade,Powerblade]

Caveman = Character("Caveman","Strengthy brute who can take a hit.",1,1,1,1,1020,0,20,Railgun)
Caveman.ability = [Punch,Swift_strike,LROne_Blaster,Railgun]

Target_practice = Character("Target Practice","Never misses. Does not wear a blindfold.",1,1,1,1,900,0,20,Restoration)
Target_practice.ability = [Dual_blasters,Energy_blade,LROne_Blaster,Stand_off]

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

#levels
levels = [[copy(Spider),copy(Spider)],[copy(Spider),copy(Bullseye),copy(Spider)]]

#functions
def listText(list,prepend,append):
    if prepend != "":
        q = f"[{prepend}, 1. {list[0].name}"
    else:
        q = f"[1. {list[0].name}"
    for x in range (1,len(list)):
        q = (f"{q}, {x+1}. {list[x].name}")
    if append != "": 
        # x += 1
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
        
def filterList(list,antiFilter):
    returnValue = []
    for i in range(len(list)):
        if list[i] not in antiFilter:
            returnValue.append(list[i])
    return returnValue

def dealDamage(caster,abilityID,targetList,targetID):
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
    elif caster.ability[abilityID].type == "energy":
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
    tactical = 100
    cancel = False
    activeTeam = copy(team)
    livingTeam = team
    turnCounter = 0
    counter = ["x"]
    for i in range(len(team)):
        team[i].hp = team[i].hp * team[i].lvl
    for i in range(len(enemies)):
        enemies[i].hp = enemies[i].hp * enemies[i].lvl
    character = ""
    while len(livingTeam) > 0 and len(enemies) > 0:
        turnCounter += 1
        for i in range(len(counter)):
            if counter[i] != "x":
                counter[i][0] -= 1
                if counter[i][0] == 0:
                    if i == 0:
                        counter[0][1].range -= 1
                    elif i == 1:
                        pass
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
                    enemies,damage = dealDamage(character,ability,enemies,targetID)
                    tactical += tacticalCalc(damage,tactical)
                    if ability == 3:
                        tactical = 0
                    print(f"Tactical: {tactical}%\n")
                    energy -= activeTeam[characterID].ability[ability].cost
                    break
                if type(character.ability[ability]) == AdvancedAbility:
                    abilityValue = character.ability[ability]
                    if abilityValue == Swift_strike:
                        if character.ability[ability].target == "enemy":
                            targetID = findTarget(enemies)
                        elif character.ability[ability].target == "team":
                            targetID = findTarget(enemies)
                        if targetID == "c":
                            cancel = True
                            break
                        enemies,damage = dealDamage(character,ability,enemies,targetID)
                        tactical += tacticalCalc(damage,tactical)
                        print(f"Tactical: {tactical}%\n")
                        enemies,damage = dealDamage(character,ability,enemies,targetID)
                        tactical += tacticalCalc(damage,tactical)
                        print(f"Tactical: {tactical}%\n")
                    if abilityValue == Restoration:
                        targetID = findTarget(livingTeam)
                        if targetID == "c":
                            cancel = True
                            break
                        livingTeam[targetID].hp += abilityValue.value
                        if livingTeam[targetID].hp > livingTeam[targetID].maxhp:
                            livingTeam[targetID].hp = livingTeam[targetID].maxhp
                        input(f"{livingTeam[targetID].name} was healed to {livingTeam[targetID].hp} health.")
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
                    if abilityValue == Stand_off:
                        character.range += 1
                        counter[0] = [3,character]
                    if abilityValue == Dual_blasters:
                        targetID = findTarget(enemies)
                        if targetID == "c":
                            cancel = True
                            break
                        enemies,damage = dealDamage(character,ability,enemies,targetID)
                        tactical += tacticalCalc(damage,tactical)
                        print(f"Tactical: {tactical}%\n")
                        enemies,damage = dealDamage(character,ability,enemies,targetID)
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
                targetID = rand.randint(1,len(livingTeam))
                targetID -= 1
                if type(enemies[i].ability[ability]) == StandardEnemyAbility:
                    if enemies[i].ability[ability].type == "kinetic":
                        damage = enemies[i].ability[ability].value * enemies[i].lvl - livingTeam[targetID].armour
                    if enemies[i].ability[ability].type == "energy":
                        damage = enemies[i].ability[ability].value * enemies[i].lvl - livingTeam[targetID].shield
                    if damage < 0:
                        damage = 0
                    print()
                    print(f"{enemies[i].name} uses {enemies[i].ability[ability].name} against {livingTeam[targetID].name}.")
                    print(f"{livingTeam[targetID].name}'s health was {livingTeam[targetID].hp}")
                    livingTeam[targetID].hp -= damage
                    if livingTeam[targetID].hp < 1:
                        livingTeam[targetID].hp = 0
                    print(f"{livingTeam[targetID].name}'s health is now {livingTeam[targetID].hp}")
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

def saveGame(team,characters,abilities,level):
    q = "Characters:\n"
    for i in range(len(characters)):
        q = f"{q}{characters[i].name}\n"
        q = f"{q}{characters[i].xp}\n"
        q = f"{q}{characters[i].lvl}\n"
        for x in range(4):
            q = f"{q}{characters[i].ability[x].name}\n"
    q = f"{q}end\n"
    q = f"{q}Team:\n"
    for i in range(len(team)):
        q = f"{q}{team[i].name}\n"
    q = f"{q}end\n"
    q = f"{q}Abilities:\n"
    for i in range(len(abilities)):
        q = f"{q}{abilities[i].name}\n"
    q = f"{q}end\n"
    q = f"{q}{level}\n"
    return q

def loadGame(allCharacters,allAbilities):
    f = open("Prr/aventyrsspel/save.txt")
    q = ""
    returnTeam = []
    returnCharacters = []
    returnAbilities = []
    line = f.readline()
    line = f.readline()
    while line != "end\n":
        for i in range(len(allCharacters)):
            if (allCharacters[i].name + "\n") == line:
                returnCharacters.append(allCharacters[i])
                line = f.readline()
                returnCharacters[len(returnCharacters)-1].xp = int(line)
                line = f.readline()
                returnCharacters[len(returnCharacters)-1].lvl = int(line)
                line = f.readline()
                for x in range(len(allAbilities)):
                    if (allAbilities[x].name + "\n") == line:
                        returnCharacters[len(returnCharacters)-1].ability[0] = allAbilities[x]
                        break
                line = f.readline()
                for x in range(len(allAbilities)):
                    if (allAbilities[x].name + "\n") == line:
                        returnCharacters[len(returnCharacters)-1].ability[1] = allAbilities[x]
                        break
                line = f.readline()
                for x in range(len(allAbilities)):
                    if (allAbilities[x].name + "\n") == line:
                        returnCharacters[len(returnCharacters)-1].ability[2] = allAbilities[x]
                        break
                break
        line = f.readline()
    line = f.readline()
    while line != "end\n":
        for i in range(len(allCharacters)):
            if (allCharacters[i].name + "\n") == line:
                returnTeam.append(allCharacters[i])
                break
        line = f.readline()
    line = f.readline()
    while line != "end\n":
        for i in range(len(allAbilities)):
            if (allAbilities[i].name + "\n") == line:
                returnAbilities.append(allAbilities[i])
                break
        line = f.readline()
    level = int(f.readline())
    return returnTeam,returnCharacters,returnAbilities,level

def main():
    f = open("Prr/aventyrsspel/save.txt", "a")
    f.close()
    while True:
        answer = input("Load save? y/n")
        if answer == "y":
            f = open("Prr/aventyrsspel/save.txt")
            if f.readline() != "Characters:\n":
                print("There seems to be a problem with the file.\nFix it and try to load it again.")
                quit()
            allCharacters = [Rangewave,Firefly,Caveman,Target_practice]
            allAbilities = [Punch,Swift_strike,LROne_Blaster,Flame_blast,Restoration,Energy_blade,Railgun,Powerblade]
            fullTeam,unlockedCharacters,unlockedAbilities,level = loadGame(allCharacters,allAbilities)
            input("Loaded save")
            break
        else:
            input("Creating new game")
            fullTeam = [Rangewave,Firefly,Target_practice]
            unlockedCharacters = [Rangewave,Firefly,Caveman,Target_practice]
            unlockedAbilities = [Punch,Swift_strike,LROne_Blaster,Flame_blast,Restoration,Energy_blade]
            level = 0
            break
    enemies = copy(levels[level])
    while True:
        answer = input("Do smthng: [c(ombat), e(dit)]")
        if answer == "c":
            fullTeam = combat(fullTeam,enemies)
            answer = ""
            level += 1
        elif answer == "e":
            fullTeam,unlockedCharacters = edit(fullTeam,unlockedCharacters,unlockedAbilities)
            answer = ""
        elif answer == "b":
            answer = ""
            break
        q = saveGame(fullTeam,unlockedCharacters,unlockedAbilities,level)
        f = open("Prr/aventyrsspel/save.txt", "w")
        f.write(q)
        f.close()

main()