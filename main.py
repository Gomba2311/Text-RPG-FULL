import random
import os
import sys

class PlayerProperty:
    def __init__(self, value):
        self.value = value
    def get_value(self):
        return self.value  

class Player:
    def __init__(self, name, cast, class_p):
        self.name = name
        self.cast = cast
        self.p_class = class_p
        self.Properties = {'Power': PlayerProperty(13).get_value(), 'Defend': PlayerProperty(12).get_value()}

            

            
    def classProperties(self):
        # Paladin
        if int(self.p_class) == 1:
            for p in self.Properties:
                self.Properties[p] += 1
        # Rouge
        elif int(self.p_class) == 2:
            self.Properties["Power"] -= 1
            self.Properties["Defend"] += 1
            self.Properties["Speed"] += 3
            self.Properties["Lucky"] += 2
            self.Properties["Charisma"] -= 1
        # Ranger
        elif int(self.p_class) == 3:
            self.Properties["Power"] += 2
            self.Properties["Defend"] += 3
            self.Properties["Speed"] -= 1

            self.Properties["Lucky"] += 2
            self.Properties["Charisma"] += 1
        # Knight
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

    def player_setup(self):
        self.classProperties()
        

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
    os.system('cls')
    print('add meg az osztályodat')
    classes = ["Paladin", "Rogue", "Ranger", "Knight", "Warrior", "Bard", "Barbarian", "Druid", "Mage"]
    for i, c in enumerate(classes):
        print(i + 1, '.', c)
    uclass = input("> ")
    os.system('cls')
    player = Player(uname, ucast, uclass)
    player.update()
    print(player.Properties)


setup()