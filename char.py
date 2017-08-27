"""Character Class for LotR DnD"""

#IMPORTS
from data import *
import random as r
import collections
import os

#DEFINING CLASSES AND FUNCTIONS

#Roll 2d6
def twoDsix():
	x = R.randint(1,6)
	y = R.randint(1,6)
	return(x+y)

#Matrix Addition for lists
def add(list1, list2):
	list = []
	for i in range(len(list1)):
		list.append(list1[i]+list2[i])
	return(list)

#Returns modifiers for attribute level
def attrmod(list):
	out = []
	for i in list:
		if i in [0,1]:
			out.append(-3)
		elif i == 2:
			out.append(-2)
		elif i == 3:
			out.append(-1)
		elif i in [4,5,6,7]:
			out.append(0)
		else:
			out.append((i // 2)-3)
	return(out)

#Character object
class Char():

    def __init__(self, name, race, order, attrs, attrmods, reas, hp, wls, dfce, cou, corr, skills, traits, abilities, level):
		self.name = name
		self.race = race
		self.order = order
		self.attrs = attrs
		self.attrmods = attrmods
		self.reas = reas
		self.hp = hp
		self.wls = wls
		self.dfce = dfce
		self.cou = cou
		self.corr = corr
		self.skills = skills
		self.traits = traits
		self.abilities = abilities
		self.level = level
		print("\nCharacter Created!\n")

	def update(self, name, race, order, attrs, attrmods, reas, hp, wls, dfce, cou, corr, skills, traits, abilities, level):
		self.name = name
		self.race = race
		self.order = order
		self.attrs = attrs
		self.attrmods = attrmods
		self.reas = reas
		self.hp = hp
		self.wls = wls
		self.dfce = dfce
		self.cou = cou
		self.corr = corr
		self.skills = skills
		self.traits = traits
		self.abilities = abilities
		self.level = level
		self.save()
		print("\nCharacter Updated!\n")

    def save(self):
        cwd = os.getcwd()
        dirname = cwd + '\\characters\\'
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        os.chdir(dirname)
        char = open(self.name + '.txt', 'w+')

        char.write('Name: ' + self.name)
        char.write('\nRace: ' + races[self.race])
        char.write('\nOrders:\n')
        for i in self.order:
            char.write(i + '\n')
        char.write('\n\nAttributes:')
        for i in self.attrs:
            char.write('\n' + str(i) + '\t' + str(self.attrs[i]) + '\t' + str(self.attrmods[i]))
        char.write('\n\nReactions:')
        for i in self.reas:
            char.write('\n' + str(i) + '\t' +  str(self.reas[i]))
        char.write('\n\nHP: ' + str(self.hp))
        char.write('\nWound Levels: ' + str(self.wls))
        char.write('\nDefence: ' + str(self.dfce))
        char.write('\nCourage: ' + str(self.cou))
        char.write('\nCorruption: ' + str(self.corr))
        char.write('\n\nSkills:')
        for i in self.skills:
            char.write('\n' + str(i) + '\t' + str(skillnames[i]) + '\t' +  str(self.skills[i]))
        char.write('\n\nTraits:')
        for i in self.traits:
            if self.traits[i] > 0:
                char.write('\n' + str(i) + '\t' + str(traitnames[i]) + '\t' + str(self.traits[i]))
        char.write('\n\nAbilities: ')
        for i in self.abilities:
            char.write('\n' + str(self.abilities[i]))

        char.close()

        dirname = cwd + '\\characters\\storage\\'
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        os.chdir(dirname)
        char = open(self.name + '.txt', 'w+')

        char.write(self.name)
        char.write('\n' + self.race)
        char.write('\n')
        for i in self.order:
            char.write(i + ',')
        char.write('\n')
        for i in self.attrs:
            char.write(str(self.attrs[i]) + ',')
        char.write('\n')
        for i in self.attrmods:
            char.write(str(self.attrmods[i]) + ',')
        char.write('\n')
        for i in self.reas:
            char.write(str(self.reas[i]) + ',')
        char.write('\n' + str(self.hp))
        char.write('\n' + str(self.wls))
        char.write('\n' + str(self.dfce))
        char.write('\n' + str(self.cou))
        char.write('\n' + str(self.corr))
        char.write('\n')
        for i in self.skills:
            char.write(str(self.skills[i]) + ',')
        char.write('\n')
        for i in self.traits:
            char.write(str(self.traits[i]) + ',')
        char.write('\n')
        for i in self.abilities:
            char.write(str(self.abilities[i]) + ',')

        char.close()

	def output(self):
		print('Name: ' + self.name)
        print('\nRace: ' + races[self.race])
        print('\nOrders:\n')
        for i in self.order:
            print(i + '\n')
        print('\n\nAttributes:')
        for i in self.attrs:
            print('\n' + str(i) + '\t' + str(self.attrs[i]) + '\t' + str(self.attrmods[i]))
        print('\n\nReactions:')
        for i in self.reas:
            print('\n' + str(i) + '\t' +  str(self.reas[i]))
        print('\n\nHP: ' + str(self.hp))
        print('\nWound Levels: ' + str(self.wls))
        print('\nDefence: ' + str(self.dfce))
        print('\nCourage: ' + str(self.cou))
        print('\nCorruption: ' + str(self.corr))
        print('\n\nSkills:')
        for i in self.skills:
            print('\n' + str(i) + '\t' + str(skillnames[i]) + '\t' +  str(self.skills[i]))
        print('\n\nTraits:')
        for i in self.traits:
            if self.traits[i] > 0:
                print('\n' + str(i) + '\t' + str(traitnames[i]) + '\t' + str(self.traits[i]))
        print('\n\nAbilities: ')
        for i in self.abilities:
            print('\n' + str(self.abilities[i]))

#Player Character object
class Player(Char):
	def __init__(self, name, race, order, attrs, attrmods, reas, hp, wls, dfce, cou, corr, skills, traits, abilities, level, gender, age, birthday, height, weight, hair, eyes, skin, handedness, homeland):
		Char.__init__(self, name, race, order, attrs, attrmods, reas, hp, wls, dfce, cou, corr, skills, traits, abilities, level)
		self.gender = gender
		self.age = age
		self.birthday = birthday
		self.height = height
		self.weight = weight
		self.hair = hair
		self.eyes = eyes
		self.skin = skin
		self.handedness = handedness
		self.homeland = homeland

#TESTING

Earendil = Char("Earendil",
"NOL",
["MAR"],
collections.OrderedDict(sorted({"BRG":0, "NIM":0, "PER":0, "STR":0, "VIT":0, "WIT":0}.items())),
collections.OrderedDict(sorted({"BRG":0, "NIM":0, "PER":0, "STR":0, "VIT":0, "WIT":0}.items())),
collections.OrderedDict(sorted({"STA":0, "SWI":0, "WIL":0, "WIS":0}.items())),
10,
5,
10,
3,
0,
collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":4, "RUN":4, "SEA":0, "SRC":0, "SIE":0, "SMI":2, "STE":4, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),
collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),
[]
)

Earendil.save()
