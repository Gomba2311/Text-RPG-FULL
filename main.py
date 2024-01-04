import random
import os
import sys


class Player:
    def __init__(self, name, cast, class_p):
        self.name = name
        self.cast = cast
        self.p_class = class_p
        self.Properties = {
            'Power': random.randint(8, 18),
            'Defend': random.randint(8, 18),
            'Speed': random.randint(8, 18),
            'Lucky': random.randint(7, 12),
            'Magic Power': random.randint(10, 30),
            'Charisma': random.randint(7, 20),
        }
    def classProperties(self):
        # Paladin
        if int(self.p_class) == 1:
            self.Properties["Power"] += 1
            self.Properties["Defend"] += 1
            self.Properties["Speed"] -= 2
            self.Properties["Lucky"] += 1
            self.Properties["Charisma"] += 3
        # Rouge
        elif int(self.p_class) == 2:
            self.Properties["Power"] -= 1
            self.Properties["Defend"] += 1
            self.Properties["Speed"] += 3
            self.Properties["Lucky"] += 2
            self.Properties["Charisma"] -= 2
        # Knight
        elif int(self.p_class) == 3:
            self.Properties["Power"] += 2
            self.Properties["Defend"] += 3
            self.Properties["Speed"] -= 1

            self.Properties["Lucky"] += 2
            self.Properties["Charisma"] += 1
        # Paladin
        elif int(self.p_class) == 4:
            self.Properties["Power"] += 1
            self.Properties["Defend"] -= 2
            self.Properties["Speed"] -= 1
            self.Properties["Lucky"] += 2
            self.Properties["Charisma"] += 1
        # Paladin
        elif int(self.p_class) == 5:
            self.Properties["Power"] += 1
            self.Properties["Defend"] -= 2
            self.Properties["Speed"] -= 1
            self.Properties["Lucky"] += 2
            self.Properties["Charisma"] += 1
        # Paladin
        elif int(self.p_class) == 6:
            self.Properties["Power"] += 1
            self.Properties["Defend"] -= 2
            self.Properties["Speed"] -= 1
            self.Properties["Lucky"] += 2
            self.Properties["Charisma"] += 1
        # Paladin
        elif int(self.p_class) == 7:
            self.Properties["Power"] += 1
            self.Properties["Defend"] -= 2
            self.Properties["Speed"] -= 1
            self.Properties["Lucky"] += 2
            self.Properties["Charisma"] += 1
        # Paladin
        elif int(self.p_class) == 8:
            self.Properties["Power"] += 1
            self.Properties["Defend"] -= 2
            self.Properties["Speed"] -= 1
            self.Properties["Lucky"] += 2
            self.Properties["Charisma"] += 1
        # Paladin
        elif int(self.p_class) == 9:
            self.Properties["Power"] += 1
            self.Properties["Defend"] -= 2
            self.Properties["Speed"] -= 1
            self.Properties["Lucky"] += 2
            self.Properties["Charisma"] += 1
        # Paladin
        elif int(self.p_class) == 10:
            self.Properties["Power"] += 1
            self.Properties["Defend"] -= 2
            self.Properties["Speed"] -= 1
            self.Properties["Lucky"] += 2
            self.Properties["Charisma"] += 1
        # Paladin
        elif int(self.p_class) == 11:
            self.Properties["Power"] += 1
            self.Properties["Defend"] -= 2
            self.Properties["Speed"] -= 1
            self.Properties["Lucky"] += 2
            self.Properties["Charisma"] += 1

    def update(self):
        self.classProperties()

class ClassesPropertiesPrinter:
    def __init__(self):
        global uclassB
        self.cl = classer()
        if int(self.cl) == 1:
            print('###Paladin###')
            print('Power: +1')
            print('Defend: -2')
            print('Speed: -1')
            print('Lucky: +2')
            print('Magic Power: Nothing')
            print('Charisma: +1')
            print('#############')
            yorn = input('> ')
            if yorn == 'yes':
                uclassB = '1'
                print(uclassB)
            elif yorn == 'no':
                ClassesPropertiesPrinter()
            else:
                print('Invalid! Please answer with yes or no!')
                while yorn != 'yes' or 'no':
                    yorn = input('> ')
                    if yorn == 'yes':
                        uclassB = '1'
                    elif yorn == 'no':
                        ClassesPropertiesPrinter()
    def returning(self):
        return uclassB



def classer():
    os.system('cls')
    print('add meg az osztályodat')
    classes = ["Paladin", "Rogue", "Ranger", "Knight", "Warrior", "Bard", "Barbarian", "Druid", "Mage"]
    for i, c in enumerate(classes):
        print(i + 1, '.', c)
    uclassA = input("> ")
    os.system('cls')
    return uclassA
        

def setup():
    global player, uclassB
    os.system('cls')
    # - USERNAME ----------------------------------------------------------------*
    uname = input("Add meg a neved! ")
    os.system('cls')
    # - CAST --------------------------------------------------------------------*
    print("Add meg a kasztodat!")
    casts = ["Ember", "Elf", "Ork", "Goblin", "Dwarf", "Dragonborn"]
    for c in range(len(casts)):
        print(c+1, ". ", casts[c])
    ucast = input("> ")
    os.system('cls')    
    # - CLASS -------------------------------------------------------------------*
    player = Player(uname, ucast, ClassesPropertiesPrinter().returning())
    print(player.Properties)

setup()