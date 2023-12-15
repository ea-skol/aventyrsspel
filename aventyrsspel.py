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

class AdvancedEnemyAbility:
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
        self.defaultValues = [melee,ranged,medicine,tactic,health,armour,shield]
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
Punch = StandardAbility("Power Punch","A fairly weak but universal form of hating someone. \nKinetic attack which deals 50 melee damage.","melee",50,0,"kinetic","enemy")
Swift_strike = AdvancedAbility("Swift strike","A swift double strike which deals damage twice. \nKinetic attack which deals 30x2 melee damage.",30,"melee",0,"kinetic","enemy")
Energy_blade = AdvancedAbility("Energy blade","A blade of energy which slices through every enemy. \nEnergy attack which deals 20 melee damage to all enemies.",20,"melee",0,"energy","")
Combat_knife = StandardAbility("Combat knife","A simple combat knife. \nKinetic attack which deals 30 melee damage.","melee",30,0,"kinetic","enemy")

#ranged
LROne_Blaster = StandardAbility("LR-1 Blaster","A standard issue energy blaster. \nEnergy attack which deals 60 ranged damage.","ranged",60,2,"energy","enemy")
Flame_blast = StandardAbility("Flame blast","A lunge of fire. \nKinetic attack which deals 40 ranged damage.","ranged",40,0,"kinetic","enemy")
Dual_blasters = AdvancedAbility("Dual blasters","Two medium-range blasters which deliver double the trouble. \nEnergy attack which deals 25x2 ranged damage.",25,"ranged",1,"energy","enemy")
XXI_Sniper = StandardAbility("XXI Sniper","A standard issue sniper rifle used by the VanGard. \nKinetic attack which deals 40 ranged damage.","ranged",40,0,"kinetic","enemy")
LRX_Blaster = StandardAbility("LR-X Blaster","Standard issue blaster for officers within the VanGard. \nEnergy attack which deals 30 ranged damage.","ranged",30,1,"energy","enemy")
FIIC_TCrossbow = AdvancedAbility("FIIC Tactical Crossbow","A modern and powerful crossbow which pierces through armour. \nKinetic attack which deals 45 ranged damage.",45,"ranged",1,"kinetic","enemy")

#ability
Restoration = AdvancedAbility("Restoration","Restore the health of allies to help them fight for another day. \nRestores 80 medical health.",80,"medicine",2,"","team")
Energy_shield = AdvancedAbility("ESG","Energy Shield Generator which grants extra shield for 2 rounds. \nGrants 10 tactical shield.",10,"tactic",2,"","team")

#tactical
Railgun = StandardAbility("Railgun","A powerful railgun which accelerates a bullet to immense speeds.\nKinetic attack which deals 100 ranged damage.","ranged",100,0,"kinetic","enemy")
Powerblade = StandardAbility("Powerblade","A blade of pure power. \nEnergy attack which deals 120 melee damage.","melee",120,0,"energy","enemy")
Stand_off = AdvancedAbility("Stand off","Aim in on your target with high precision and deal extra damage. \nIncrease ranged level by 2.",1,"tactic",0,"","enemy")
Earthquake = AdvancedAbility("Earthquake","Shatter the ground damaging enemies. \nKinetic attack which deals 50 melee damage to all enemies.",50,"melee",0,"kinetic","enemy")
Command = AdvancedAbility("Command","An encouraging command to fight better. \nDoubles all melee damage for 1 round.",1,"tactic",0,"","team")

#characters
Rangewave = Character("Rangewave","Proficient fighter of the VanGard.",1,2,1,1,880,0,10,Railgun)
Rangewave.ability = [Combat_knife,XXI_Sniper,LROne_Blaster,Railgun]

General_Borg = Character("General Borg","General Attus Borg is a general within the VanGard.",1,2,1,2,900,0,0,Command)
General_Borg.ability = [Combat_knife,Restoration,LRX_Blaster,Command]

Firefly = Character("Firefly","Fiery warrior and mechanical officer of the VanGard. From the planet Laito.",1,2,1,2,900,10,0,Powerblade)
Firefly.ability = [Flame_blast,Restoration,Energy_blade,Powerblade]

Target_practice = Character("Target Practice","Marksman of the VanGard.",1,2,1,1,970,0,20,Stand_off)
Target_practice.ability = [Dual_blasters,Energy_blade,LROne_Blaster,Stand_off]
Target_practice.lvl = 2
Target_practice.melee = Target_practice.defaultValues[0] * Target_practice.lvl
Target_practice.range = Target_practice.defaultValues[1] * Target_practice.lvl
Target_practice.med = Target_practice.defaultValues[2] * Target_practice.lvl
Target_practice.tactic = Target_practice.defaultValues[3] * Target_practice.lvl
Target_practice.hp = Target_practice.defaultValues[4] + 200 * (Target_practice.lvl - 1)
Target_practice.maxhp = Target_practice.defaultValues[4] + 200 * (Target_practice.lvl - 1)
Target_practice.armour = Target_practice.defaultValues[5]
Target_practice.shield = Target_practice.defaultValues[6]


Caveman = Character("Caveman","Strengthy brute who can take a hit.",2,1,1,1,1020,0,20,Earthquake)
Caveman.ability = [Punch,Swift_strike,LRX_Blaster,Earthquake]
Caveman.lvl = 2
Caveman.melee = Caveman.defaultValues[0] * Caveman.lvl
Caveman.range = Caveman.defaultValues[1] * Caveman.lvl
Caveman.med = Caveman.defaultValues[2] * Caveman.lvl
Caveman.tactic = Caveman.defaultValues[3] * Caveman.lvl
Caveman.hp = Caveman.defaultValues[4] + 200 * (Caveman.lvl - 1)
Caveman.maxhp = Caveman.defaultValues[4] + 200 * (Caveman.lvl - 1)
Caveman.armour = Caveman.defaultValues[5]
Caveman.shield = Caveman.defaultValues[6]

#enemy abilities
Pounce = StandardEnemyAbility("Pounce","A quick and easy pounce","kinetic",20,"team")
Claw = StandardEnemyAbility("Claw","A quick attack made by claws","kinetic",30,"team")
FC_DBlasters = StandardEnemyAbility("FC Dual blasters","Two blasters used by famed bounty hunter Bullseye.","energy",40,"team")
Charge = StandardEnemyAbility("Charge","Rush towards the enemy.","kinetic",70,"team")
C58_Grenade = AdvancedEnemyAbility("C58 Grenade","A grenade.","energy",30,"team")
TTI_Blaster = StandardEnemyAbility("TTI Blaster","Standard issue Exi blaster.","energy",50,"team")
TTX_Blaster = StandardEnemyAbility("TTX Blaster","Standard issue Exi officer blaster.","energy",60,"team")
ShieldEn = AdvancedEnemyAbility("Shield generator","Apply a temporary shield.","",10,"enemy")
Sovereign_Spear = StandardEnemyAbility("Sovereign Spear","A spear used by the Exi Sovereign Guards.","kinetic",80,"team")

#enemies
Critter = Enemy("Critter","Small but oversized desert dwelling insect.",180,0,0)
Critter.ability = [copy(Pounce),copy(Claw)]
Critter.ability[0].weight = 3
Critter.ability[1].weight = 1

Spider = Enemy("Spider","A spider",150,0,0)
Spider.ability = [copy(Pounce)]
Spider.ability[0].weight = 1

Bullseye = Enemy("Bullseye","Famed bounty hunter",740,15,10)
Bullseye.ability = [copy(FC_DBlasters),copy(Charge)]
Bullseye.ability[0].weight = 3
Bullseye.ability[1].weight = 1

Exi_trooper = Enemy("Exi Trooper","Standard trooper of Exi.",280,5,0)
Exi_trooper.ability = [copy(TTI_Blaster)]
Exi_trooper.ability[0].weight = 1

Exi_Canoneer = Enemy("Exi Canoneer","Explosive expert within Exi.",250,5,0)
Exi_Canoneer.ability = [copy(TTI_Blaster),copy(C58_Grenade)]
Exi_Canoneer.ability[0].weight = 4
Exi_Canoneer.ability[1].weight = 1

Exi_pilot = Enemy("Exi Pilot","Pilot of Exi.",230,5,5)
Exi_pilot.ability = [copy(TTI_Blaster),copy(ShieldEn)]
Exi_pilot.ability[0].weight = 5
Exi_pilot.ability[1].weight = 1

Exi_officer = Enemy("Exi Officer","Officer of Exi.",250,10,5)
Exi_officer.ability = [copy(TTX_Blaster),copy(ShieldEn)]
Exi_officer.ability[0].weight = 3
Exi_officer.ability[1].weight = 1

Exi_guard = Enemy("Exi Sovereign Guard","",1000,20,20)
Exi_guard.ability = [copy(Sovereign_Spear)]
Exi_guard.ability[0].weight = 1

Exi_SuperiorGaurd = Enemy("Exi Superior Guard","Coming soon",0,0,0)

Scope = Enemy("Scope","Coming soon",0,0,0)
Scope.ability = [copy(Pounce)]

#levels
levels = [[Exi_trooper,Exi_trooper],[Critter,Critter,Critter],[Exi_trooper,Exi_Canoneer,Exi_trooper],[Exi_trooper,Bullseye,Exi_trooper],[Exi_trooper,Exi_pilot],[Exi_trooper,Exi_pilot,Exi_pilot],[Exi_Canoneer,Exi_officer],[Exi_officer,Exi_trooper,Exi_trooper],[Exi_trooper,Exi_trooper],[Exi_officer,Exi_Canoneer,Exi_officer],[Exi_guard,Exi_guard]]
difficulty = [1,1,1,1,2,2,2,2,3,3,3]

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
        damage = caster.ability[abilityID].value * proficiency - targetList[targetID].armour * targetList[targetID].lvl
    elif caster.ability[abilityID].type == "energy":
        damage = caster.ability[abilityID].value * proficiency - targetList[targetID].shield * targetList[targetID].lvl
    if damage < 0:
        damage = 0
    print(f"\nThe enemy's health was {targetList[targetID].hp}")
    targetList[targetID].hp -= damage
    if targetList[targetID].hp < 1:
        targetList[targetID].hp = 0
    print(f"The enemy's health is now {targetList[targetID].hp}")
    return targetList,damage

def tacticalCalc(inputDamage,charge):
    if charge + int(inputDamage/8) > 100:
        return 100-charge
    else:
        return int(inputDamage/8)

def combat(team,enemies):
    q = []
    for i in range(len(enemies)):
        q.append(enemies[i].name)
    input(f"You encountered: {q}")
    exitType = "x"
    xp = 0
    energy = 0
    tactical = 0
    cancel = False
    activeTeam = copy(team)
    livingTeam = copy(team)
    turnCounter = 0
    counter = ["x","x","x","x"]
    # for i in range(len(team)):
    #     team[i].hp = team[i].hp * team[i].lvl
    for i in range(len(enemies)):
        enemies[i].hp = enemies[i].maxhp
    character = ""
    while len(livingTeam) > 0 and len(enemies) > 0:
        turnCounter += 1
        for i in range(len(counter)):
            if counter[i] != "x":
                counter[i][0] -= 1
                if counter[i][0] == 0:
                    if i == 0:
                        counter[0][1].range -= 1
                        counter[0] = "x"
                    elif i == 1:
                        for x in range(len(livingTeam)):
                            livingTeam[x].melee -= 1
                        counter[1] = "x"
                    elif i == 2:
                        counter[2][1].shield -= Energy_shield.value
                        counter[2] = "x"
                    elif i == 3:
                        counter[3][1].shield -= ShieldEn.value * counter[3][1].lvl
                        counter[3] = "x"
        energy += 1
        activeTeam = copy(livingTeam)
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
                    tactical += tacticalCalc(damage/character.lvl,tactical)
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
                        tactical += tacticalCalc(damage/character.lvl,tactical)
                        print(f"Tactical: {tactical}%\n")
                        enemies,damage = dealDamage(character,ability,enemies,targetID)
                        tactical += tacticalCalc(damage/character.lvl,tactical)
                        print(f"Tactical: {tactical}%\n")
                    if abilityValue == Restoration:
                        targetID = findTarget(livingTeam)
                        if targetID == "c":
                            cancel = True
                            break
                        livingTeam[targetID].hp += abilityValue.value * character.med
                        if livingTeam[targetID].hp > livingTeam[targetID].maxhp:
                            livingTeam[targetID].hp = livingTeam[targetID].maxhp
                        input(f"{livingTeam[targetID].name} was healed to {livingTeam[targetID].hp} health.")
                    if abilityValue == Energy_blade:
                        for i in range(len(enemies)):
                            proficiency = character.melee
                            damage = character.ability[ability].value * proficiency - enemies[i].armour
                            if damage < 0:
                                damage = 0
                            print(f"\nThe enemy's health was {enemies[i].hp}")
                            enemies[i].hp -= damage
                            if enemies[i].hp < 1:
                                enemies[i].hp = 0
                            print(f"The enemy's health is now {enemies[i].hp}")
                            tactical += tacticalCalc(damage/character.lvl,tactical)
                            print(f"Tactical: {tactical}%\n")
                    if abilityValue == Stand_off:
                        character.range += 2
                        counter[0] = [3,character]
                        tactical = 0
                    if abilityValue == Dual_blasters:
                        targetID = findTarget(enemies)
                        if targetID == "c":
                            cancel = True
                            break
                        enemies,damage = dealDamage(character,ability,enemies,targetID)
                        tactical += tacticalCalc(damage/character.lvl,tactical)
                        print(f"Tactical: {tactical}%\n")
                        enemies,damage = dealDamage(character,ability,enemies,targetID)
                        tactical += tacticalCalc(damage/character.lvl,tactical)
                        print(f"Tactical: {tactical}%\n")
                    if abilityValue == Earthquake:
                        for i in range(len(enemies)):
                            tactical = 0
                            proficiency = character.melee
                            damage = character.ability[ability].value * proficiency - enemies[i].armour
                            if damage < 0:
                                damage = 0
                            print(f"\nThe enemy's health was {enemies[i].hp}")
                            enemies[i].hp -= damage
                            if enemies[i].hp < 1:
                                enemies[i].hp = 0
                            print(f"The enemy's health is now {enemies[i].hp}")
                            print(f"Tactical: {tactical}%\n")
                    if abilityValue == Command:
                        for i in range(len(livingTeam)):
                            livingTeam[i].melee += 1
                        counter[1] = [2,"all"]
                        tactical = 0
                    if abilityValue == Energy_shield:
                        targetID = findTarget(livingTeam)
                        if targetID == "c":
                            cancel = True
                            break
                        livingTeam[targetID].shield += abilityValue.value * character.lvl
                        counter[2] = [2,livingTeam[targetID]]
                    if abilityValue == FIIC_TCrossbow:
                        targetID = findTarget(enemies)
                        if targetID == "c":
                            cancel = True
                            break
                        proficiency = character.range
                        damage = character.ability[ability].value * proficiency
                        if damage < 0:
                            damage = 0
                        print(f"\nThe enemy's health was {enemies[targetID].hp}")
                        enemies[targetID].hp -= damage
                        if enemies[targetID].hp < 1:
                            enemies[targetID].hp = 0
                        print(f"The enemy's health is now {enemies[targetID].hp}")
                        tactical += tacticalCalc(damage/character.lvl,tactical)
                        print(f"Tactical: {tactical}%\n")
                    energy -= activeTeam[characterID].ability[ability].cost
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
                    print(f"\n{enemies[i].name} uses {enemies[i].ability[ability].name} against {livingTeam[targetID].name}.")
                    print(f"{livingTeam[targetID].name}'s health was {livingTeam[targetID].hp}")
                    livingTeam[targetID].hp -= damage
                    if livingTeam[targetID].hp < 1:
                        livingTeam[targetID].hp = 0
                    print(f"{livingTeam[targetID].name}'s health is now {livingTeam[targetID].hp}")
                    tactical += tacticalCalc(damage/enemies[i].lvl,tactical)
                    input(f"Tactical: {tactical}%")
                if type(enemies[i].ability[ability]) == AdvancedEnemyAbility:
                    abilityValue = enemies[i].ability[ability]
                    if abilityValue.name == "C58 Grenade":
                        print(f"\n{enemies[i].name} uses {enemies[i].ability[ability].name}.")
                        for x in range(len(livingTeam)):
                            damage = enemies[i].ability[ability].value * enemies[i].lvl - livingTeam[x].armour
                            if damage < 0:
                                damage = 0
                            print(f"\n{livingTeam[x].name}'s health was {livingTeam[x].hp}")
                            livingTeam[x].hp -= damage
                            if livingTeam[x].hp < 1:
                                livingTeam[x].hp = 0
                            print(f"{livingTeam[x].name}'s health is now {livingTeam[x].hp}")
                            tactical += tacticalCalc(damage/enemies[i].lvl,tactical)
                            input(f"Tactical: {tactical}%")
                    if abilityValue.name == "Shield generator":
                        print(f"\n{enemies[i].name} uses {enemies[i].ability[ability].name} and increases their shield by {abilityValue.value * enemies[i].lvl}.")
                        counter[3] = [2,enemies[i]]
                        enemies[i].shield += abilityValue.value * enemies[i].lvl
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
        input("All characters died and you lost!")
        exitType = "defeat"
    elif enemies == []:
        input(f"Your characters gained {xp}xp!")
        exitType = "victory"
    if exitType == "victory":
        for i in range(len(team)):
            team[i].xp += xp
            if team[i].xp > team[i].lvl*250:
                while team[i].xp > team[i].lvl*250:
                    team[i].xp -= team[i].lvl*250
                    team[i].lvl += 1
                team[i].melee = team[i].defaultValues[0] * team[i].lvl
                team[i].range = team[i].defaultValues[1] * team[i].lvl
                team[i].med = team[i].defaultValues[2] * team[i].lvl
                team[i].tactic = team[i].defaultValues[3] * team[i].lvl
                team[i].hp = team[i].defaultValues[4] + 200 * (team[i].lvl - 1)
                team[i].maxhp = team[i].defaultValues[4] + 200 * (team[i].lvl - 1)
                team[i].armour = team[i].defaultValues[5]
                team[i].shield = team[i].defaultValues[6]
    return team,exitType

def edit(team,all,abilities):
    while True:
        answer = input("\nWould you like to edit your characters or change your team? [exit, e(dit), c(hange)]")
        if answer == "exit":
            return team,all
        elif answer == "e": 
            while True:
                q = listText(all,"c(ancel)","")
                answer = (input(f"\nChoose a character: {q}"))
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
                    answer = input(f"\nChoose an ability to edit or inspect: {q}")
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
                            answer = input(f"\nInspect or replace {all[characterID].ability[abilityID].name}? [c(ancel), i(nspect), r(eplace)]")
                            if answer == "c":
                                break
                            elif answer == "i":
                                input(f"\n{all[characterID].ability[abilityID].name}: {all[characterID].ability[abilityID].desc} \nThis ability costs {all[characterID].ability[abilityID].cost} energy to use.")
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
            add_character = Character("Add character","There is currently no character in this slot.",0,0,0,0,0,0,0,"n/a")
            while True:
                while True:
                    if len(team) != 3:
                        for i in range(3-len(team)):
                            team.append(add_character)
                    else:
                        break
                q = listText(team,"c(ancel)","")
                answer = input(f"\nChoose a team member to replace: {q}")
                if answer == "c":
                    for i in range(len(team)):
                        if team[i] == add_character:
                            team.remove(add_character)
                            i -= 1
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
                        answer = input(f"\nInspect or replace? [c(ancel), i(nspect), r(eplace)]")
                        if answer == "c":
                            break
                        elif answer == "i":
                            print(f"\n{team[characterID].name}: {team[characterID].desc}")
                            print(f"{team[characterID].name} has {team[characterID].xp}xp and is at level {team[characterID].lvl}.")
                            print(f"Their proficiencies are: {team[characterID].melee} melee, {team[characterID].range} ranged, {team[characterID].med} medicine and {team[characterID].tactic} tactical.")
                            print(f"Their health is {team[characterID].hp}hp.")
                            input(f"They have {team[characterID].armour} armour and {team[characterID].shield} shield.")
                        elif answer == "r":
                            while True:
                                availableCharacters = filterList(all,team)
                                if availableCharacters != []:
                                    q = listText(availableCharacters,"c(ancel)","")
                                    answer = input(f"Which character would you like to replace {team[characterID].name} with? {q}")
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

def playDialogue(level,dialogue):
    if dialogue == 1:
        return
    else:
        if level == 0:
            input("On the planet Toros, in the southern parts of the Norak desert, the VanGard has set up camp.")
            input("The planet has been outside of the war for its entire duration.")
            input("The VanGard has, however, reason to believe that the Exi, their enemy, has a military base in the north of the desert.")
            input("They prepare to attack....")
            input('General Borg: "Listen up! We have it confirmed! One of our scouts spotted a facility and upon investigation could confirm it belonged to the Exi."')
            input('General Borg: "The only problem is, they captured the scout."')
            input('General Borg: "They know we are coming, and so we must act quickly!"')
            input('General Borg: "Rangewave! The camp lies around 3km from a cliff. I need you as a sniper atop that cliff."')
            input('Rangewave: "Yes, general!"')
            input('General Borg: "We will need a team to enter and extract the scout and a..."')
            input('General Borg: "Wait..."')
            input('General Borg: "Does anyone else hear that?"')
            input('"INCOMING!!!"')
            input("A ship approaches and fires a bolt, hitting parts of the camp which go up in flames.")
            input("Another ship approaches and drops of Exi-troopers.")
            input("The troops rush towards Borg and Rangewave who are caught alone amidst the now ensuing chaos.")
            input('''General Borg: "Rangewave! I'll cover you!"''')
        if level == 1:
            input('General Borg: "That was a close one. But now we are in trouble."')
            input('General Borg: "We must launch a counterattack immediately!"')
            input('General Borg: "Rangewave! Grab a hoverbike and approach the Exi base. A team will assist you with aircract shortly."')
            input("Rangewave jumps on the hoverbike and goes towards the Exi base.")
            input("Suddenly, the bike stops.")
            input('Rangewave: "Dammit! This is Rangewave, the bike broke down, over."')
            input('Comms: "We hear you. Give us your location, over."')
            input('''Rangewave: "34'56a."''')
            input('Comms: "Aircraft will be inbound shortly, over."')
            input('Rangewave: "Copy."')
            input("A whisp of wind blows past in the empt desert.")
            input("Rangewave looks around and notices a small group of oversized insects approaching.")
            input('Rangewave: "This is Rangewave, I have a pack of critters approaching, over"')
            input('Comms: "The aircraft is soon there, over."')
            input('Rangewave: "Copy."')
            input("Rangewave shoots at the critters which only seems to anger them, and they approach and jump towards Rangewave in an attack.")
        if level == 2:
            input("A ship approaches over Rangewave who jumps aboard it as a new hoard of critters approach.")
            input('Firefly: "My name is Firefly. We are approaching the Exi base and when we arrive you and I will be on the ground."')
            input('Rangewave: "Copy!"')
            input("The ship approaches the Exi base and as it does oncoming fire forces them to fly low.")
            input('''Firefly: "We're going to have to settle down here! Get ready to jump!"''')
            input("Firefly and Rangewave jump out of the ship and approach the base.")
            input("A group of Exi soldiers approaches them from the gates of the base.")
        if level == 3:
            input('Comms: "This is General Borg! We have located where in the base the scout is held."')
            input('''Firefly: "Send us the position and we'll get on it!"''')
            input("After a few seconds a beep is heard.")
            input('''Firefly: "Position recieved! Let's go!"''')
            input("The team goes into the base and approaches the location of the scout.")
            input("Suddenly, a blast flies past them.")
            input('Bullseye: "Well then, look what we got here!"')
            input('''Bullseye: "Name's Bullseye, famed bounty hunter, and wherever you're going you're not going any further."''')
        if level == 4:
            input('Rangewave: "Surrender!"')
            input('Bullseye: "..."')
            input('Bullseye: "No!"')
            input("Bullseye leaps and runs away. Rangewave decides to follow but is stopped by Firefly.")
            input('''Firefly: "He's not important. Let's rescue the scout."''')
            input("They enter the chamber where the scout is being held and release them.")
            input('Scout: "Thank you!"')
            input('General Borg: "Good job! We have secured the base."')
            input("Firefly and Rangewave leave the base and jump aboard a ship.")
            input('General Borg: "Well done, you two!"')
            input('General Borg: "However, we have news of the Exi terrorizing the Itmar system."')
            input('General Borg: "We will need you both there as soon as possible."')
            input('General Borg: "Before you go we do however have some upgrades."')
            input('General Borg: "Here!"')
            input('Your characters have gained access to the ability: "FIIC Tactical Crossbow"')
            input("To equip it on a character enter the edit menu.")
        if level == 6:
            input('As the team goes through the ship they meet one of the members, Target Practice, of Team Charge.')
            input('Rangewave: "What are you doing here?"')
            input('Target Practice: "Caveman and I were going through the reactor shaft when he fell."')
            input('''Target Practice: "He is alright, he's just alone."''')
            input('''Firefly: "Then we need to find him!"''')
            input("Target Practice has been added to the available characters. Enter the customazation menu to put them on the team.")
        if level == 7:
            input('Comms: "This is captain Phfion, I have good news!"')
            input('Comms: "We are recieving support from the Caion Federation."')
            input('Into the hangar of the Exi cruiser ships fly in which start shooting at the Exi soldiers.')
            input("Troops exit the ships and approach the team.")
            input('''Captain Hyjio: "Your job here is done, we're taking over."''')
            input('Firefly: "We have a trooper within this ship that we have to recieve."')
            input('''Captain Hyjio: "If they're alone, then they're dead."''')
            input('Target Practice: "Caveman is strong. I doubt he will go down easily!"')
            input('''Captain Hyjio: "Caveman! What a stupid name. Either way you're out."''')
            input('Firefly: "What jurisdiction do you have to tell us that?"')
            input('Captain Hyjio: "This system is part of the Caion Federation, get out!"')
            input('Firefly: "The VanGard is part of the Caion Federation."')
            input('Captain Hyjio: "I can demote you."')
            input('Rangewave: "Contact Phfion."')
            input('Captain Hyjio: "No need."')
            input("Firefly stares at Hyjio and turns on the comms.")
            input('Comms: "Captain Phfion here, over."')
            input('Firefly: "Permission to ignore Caion commands and go save Caveman?"')
            input('Comms: "What?"')
            input('Firefly: "We have been ordered to leave but Caveman is in trouble."')
            input('''Comms: "Why wouldn't you be able to rescue him?"''')
            input('''Firefly: "Because we've been ordered to leave by some Hyjio."''')
            input('Comms: "Permission to rescue Caveman granted."')
            input('Firefly: "Thank you, captain."')
            input("Firefly glares at Hyjio before they leave to go after Caveman.")
        if level == 10:
            input("As the team runs through the ship they manage to walk into a familiar face.")
            input('Target Practice: "Caveman!"')
            input('Caveman: "Target Practice! We have to hurry!"')
            input("Caveman starts running and the others follow.")
            input('Caveman: "I managed to run into some important Exi figures."')
            input('Caveman: "First off: Grand General Kaiylof of the Exi."')
            input('Firefly: "And what happened?"')
            input('Caveman: "Took them by surprise; The Grand General is dead."')
            input('Caveman: "With the Grand General was also Exi Governer Ridley. They managed to flee."')
            input('Firefly: "Dammit!"')
            input('Caveman: "Lastly: High Chancellor Sailos, the leader of the Exi."')
            input('Firefly: "Did they flee too?"')
            input('Caveman: "Not yet, and that is why we hurry!"')
            input("Firefly actives the comms.")
            input('Firefly: "Everyone! The High Chancellor is on this cruiser. I repeat: High Chancellor Sailos is on this cruiser."')
            input('Comms: "Captain Phfion here, are you sure?"')
            input('Caveman: "Yes!"')
            input('Comms: "We will have the cruiser surrounded then!"')
            input("Caveman has been added to the available characters.")

def playPreDialogue(level,play):
    if not play:
        return
    else:
        if level == 4:
            input('The team approaches the Itmar system in a battle cruiser.')
            input('Captain Phfion: "When we enter the system we will immidietly be under fire from this Exi cruiser."')
            input("A map is shown with an image of an Exi cruiser.")
            input('Captain Phfion: "Two teams will board the cruiser: Team Ion and Team Charge."')
            input('Captain Phfion: "Team Ion will consist of Officer Firefly and Rangewave."')
            input('Captain Phfion: "Team Charge will consist of Target Practice and Caveman."')
            input("Two people standing beside Firefly and Rangewave nod.")
            input("After some more briefing of the plan the two teams are loaded aboard separate ships.")
            input("As the cruiser approaches the system the ships leave it and approach the Exi cruiser under heavy fire.")
            input("Luckily, both make it aboard.")
            input("Team Ion lands in a hangar and are immidietly approached by Exi troopers.")
            input('Firefly: "Incoming!"')
        if level == 10:
            input('Caveman: "There!"')
            input("Caveman's outburst alerts what he was referencing: The High Chancellor as well as four guards.")
            input('High Chancellor Sailos: "Two of you, take care of them. The other two escort me."')

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
    for i in range(len(returnCharacters)):
        returnCharacters[i].melee = returnCharacters[i].defaultValues[0] * returnCharacters[i].lvl
        returnCharacters[i].range = returnCharacters[i].defaultValues[1] * returnCharacters[i].lvl
        returnCharacters[i].med = returnCharacters[i].defaultValues[2] * returnCharacters[i].lvl
        returnCharacters[i].tactic = returnCharacters[i].defaultValues[3] * returnCharacters[i].lvl
        returnCharacters[i].hp = returnCharacters[i].defaultValues[4] + 200 * (returnCharacters[i].lvl - 1)
        returnCharacters[i].maxhp = returnCharacters[i].defaultValues[4] + 200 * (returnCharacters[i].lvl - 1)
    return returnTeam,returnCharacters,returnAbilities,level

def main():
    f = open("Prr/aventyrsspel/save.txt", "a")
    f.close()
    dialogue = 0
    while True:
        answer = input("Load save? y/n:")
        if answer == "y":
            f = open("Prr/aventyrsspel/save.txt")
            if f.readline() != "Characters:\n":
                print("There seems to be a problem with the file.\nFix it and try to load it again.")
                quit()
            allCharacters = [Rangewave,General_Borg,Firefly,Caveman,Target_practice]
            allAbilities = [Punch,Swift_strike,LROne_Blaster,Flame_blast,Restoration,Energy_blade,Railgun,Powerblade,Energy_shield,FIIC_TCrossbow]
            fullTeam,unlockedCharacters,unlockedAbilities,level = loadGame(allCharacters,allAbilities)
            input("Loaded save [Enter]")
            skipCutscene = False
            break
        elif answer == "n":
            answer = input("This will overwrite any existing saves. Are you sure? [y(es)/anything else]")
            if answer == "y":
                input("Creating new game [Enter]")
                fullTeam = [Rangewave,General_Borg]
                unlockedCharacters = [Rangewave]
                unlockedAbilities = [Combat_knife,XXI_Sniper,LROne_Blaster]
                level = 0
                while True:
                    answer = input("Yould you like to SKIP all cutscenes? y/n")
                    if answer == "y":
                        skipCutscene = True
                        break
                    elif answer == "n":
                        skipCutscene = False
                        break
                    else:
                        input("Invalid input")
                        continue
                break
        else:
            input("Invalid input")
    while True:
        if skipCutscene:
            dialogue = 1
        playDialogue(level,dialogue)
        dialogue = 1
        if level < 4:
            enemies = []
            for i in range(len(levels[level])):
                enemies.append(copy(levels[level][i]))
                enemies[i].lvl = difficulty[level]
                enemies[i].maxhp *= enemies[i].lvl
            fullTeam,exitType = combat(fullTeam,enemies)
            if exitType == "victory":
                if level == 0:
                    fullTeam.remove(General_Borg)
                if level == 1:
                    fullTeam.append(Firefly)
                    unlockedCharacters.append(Firefly)
                    unlockedAbilities.append(Flame_blast)
                    unlockedAbilities.append(Restoration)
                    unlockedAbilities.append(Energy_blade)
                if level == 3:
                    unlockedAbilities.append(FIIC_TCrossbow)
                level += 1
                if skipCutscene:
                    dialogue = 1
                else:
                    dialogue = 0
            for i in range(len(fullTeam)):
                fullTeam[i].hp = fullTeam[i].maxhp
        else:
            answer = input("\nWhat would you like to do? [c(ombat), e(dit team), [s(ave game])]")
            if answer == "c":
                while True:
                    levelsNum = []
                    levelsNum.append("c(ancel)")
                    if level >= len(levels):
                        for i in range(len(levels)):
                            levelsNum.append(i+1)
                    else:
                        for i in range(level+1):
                            levelsNum.append(i+1)
                    answer = input(f"Select level: {levelsNum}")
                    if answer == "c":
                        break
                    try:
                        answer = int(answer)
                    except ValueError:
                        input("Write a valid input")
                        continue
                    answer -= 1
                    break
                if answer == "c":
                    continue
                enemies = []
                for i in range(len(levels[answer])):
                    enemies.append(copy(levels[answer][i]))
                    enemies[i].lvl = difficulty[answer]
                    enemies[i].maxhp = enemies[i].hp + 200 * (enemies[i].lvl - 1)
                playPreDialogue(level,answer==level)
                fullTeam,exitType = combat(fullTeam,enemies)
                if exitType == "victory" and answer == level:
                    if level == 5:
                        unlockedCharacters.append(Target_practice)
                        unlockedAbilities.append(Dual_blasters)
                    if level == 9:
                        unlockedCharacters.append(Caveman)
                        unlockedAbilities.append(Punch)
                        unlockedAbilities.append(Swift_strike)
                        unlockedAbilities.append(LRX_Blaster)
                    level += 1
                    if skipCutscene:
                        dialogue = 1
                    else:
                        dialogue = 0
                for i in range(len(fullTeam)):
                    fullTeam[i].hp = fullTeam[i].maxhp
                answer = ""
            elif answer == "e":
                fullTeam,unlockedCharacters = edit(fullTeam,unlockedCharacters,unlockedAbilities)
                answer = ""
            elif answer == "b":
                answer = ""
                break
            elif answer == "s":
                q = saveGame(fullTeam,unlockedCharacters,unlockedAbilities,level)
                f = open("Prr/aventyrsspel/save.txt", "w")
                f.write(q)
                f.close()
                input("Saved game")
        q = saveGame(fullTeam,unlockedCharacters,unlockedAbilities,level)
        f = open("Prr/aventyrsspel/save.txt", "w")
        f.write(q)
        f.close()

main()