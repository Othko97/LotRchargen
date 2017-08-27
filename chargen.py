"""creates characters in LotR system"""

#IMPORTS

import random as R
import os
import collections
from data import *
from char import *


#DEFINING CLASSES AND FUNCTIONS

def createchar():
	if input("Player Character? (y/N): ").upper() == "Y":
		name = input("Character Name: ")
		gender = input("Gender: ")
		age = input("Age: ")
		birthday = input("Birthday: ")
		height = input("Height: ")
		weight = input("Weight: ")
		hair = input("Hair Colour: ")
		eyes = input("Eye Colour: ")
		skin = input("Skin Colour: ")
		handedness = input("Handedness: ")
		homeland = input("Homeland: ")
	else:
		name = input("Character Name: ")
	race = 'START'
	while race not in races.keys():
		race = input('Race: ').upper()
		if race == "LIST":
			print(racelist)

	


#########################################################
#ANYTHING BELOW THIS POINT IS OLD CODE BEING MOVED ABOVE#
#########################################################

class Char():

	#Roll random Attributes
	def rollrandattrs(self):
		rolls = []
		for i in range(9):
			rolls.append(twoDsix())		#rolls 9, takes highest 6
		rolls.sort(reverse=True)
		rolls = rolls[:6]
		R.shuffle(rolls)				#randomises order
		self.attrs = collections.OrderedDict(sorted(dict(zip(["BRG", "NIM", "PER", "STR", "VIT", "WIT"],rolls)).items()))

	#Adds racial modifiers to attributes
	def racialmod(self):
		#adds racial mods for character's race
		self.attrs = collections.OrderedDict(sorted(dict(zip(list(self.attrs.keys()), add(list(self.attrs.values()),list(racattradjs[self.race].values())))).items()))

		#adds 3*WIT to language and lore
		for i in range(self.attrs["WIT"]*3):
			if R.randint(1,2) == 1:
				self.skills["LAN"] += 1
			else:
				self.skills["LOR"] += 1

	#Adds background modifiers
	def bgmod(self):
		#adds mods for pre made background
		self.skills = collections.OrderedDict(sorted(dict(zip(list(self.skills.keys()), add(list(self.skills.values()),list(bgskilladjs[self.background].values())))).items()))

		#if no premade background adds 6 picks
		if self.background == "N":
			i = 0
			while i < 6:
				i += self.racincskill()

	#Adds order package modifiers
	def packmod(self):
		#adds mods for pre made package
		self.skills = collections.OrderedDict(sorted(dict(zip(list(self.skills.keys()), add(list(self.skills.values()),list(packskilladjs[self.pack].values())))).items()))

	#System to increment skills for race
	def racincskill(self):
		racstufflist = []
		print("\nEnter 3 letter skill/trait code to increase \n")
		print("SKILLS: ")
		for x in racskills[self.race]:
			print(x, skillnames[x], self.skills[x])
			racstufflist.append(x)
		print("\nTRAITS: ")
		for x in ractraits[self.race]:
			print(x, traitnames[x], self.traits[x])
			racstufflist.append(x)
		inc = input("Enter code: ")
		if inc == "RND":
			i = R.randint(1,len(racstufflist))-1
			if i < len(racskills[self.race]):
				self.skills[racstufflist[i]] += 1
				return(1)
			else:
				self.traits[racstufflist[i]] += 1
				return(1)
		if inc in self.skills:
			self.skills[inc] += 1
			return(1)
		elif inc in self.traits:
			if self.traits[inc] < traitmaxes[inc]:
				self.traits[inc] += 1
				return(1)
			else:
				print("Already taken to maximum level")
				return(0)

	#System to increment skills for order
	def ordincskill(self):
		print("\nEnter 3 letter skill code to increase \n")
		orskillist = []
		for i in self.orders:
			for x in orderskills[i]:
				if x in orskillist:
					pass
				else:
					orskillist.append(x)
		for x in orskillist:
			print(x, skillnames[x], self.skills[x])
		inc = input("Enter code: ")
		if inc == "RND":
			self.skills[orskillist[R.randint(1,len(orskillist))-1]]
		if inc in self.skills:
			self.skills[inc] += 1
		elif inc in self.traits:
			self.traits[inc] += 1

	#Calculates reactions from attributes
	def setreas(self):
		self.reas["STA"] = max([self.attrmods["STR"], self.attrmods["VIT"]])
		self.reas["SWI"] = max([self.attrmods["NIM"], self.attrmods["PER"]])
		self.reas["WIL"] = max([self.attrmods["BRG"], self.attrmods["WIT"]])
		self.reas["WIS"] = max([self.attrmods["BRG"], self.attrmods["PER"]])

	#Initialisation of instance
	def __init__(self, name, race, order, background, pack, gender):
		self.name = name
		self.race = race
		self.orders = []
		if order != "N":
			self.orders.append(order)
		self.background = background
		self.gender = gender
		self.reas = reactemp
		self.rollrandattrs()
		self.skills = skilltemp
		self.traits = traitstemp
		self.racialmod()
		self.attrmods = collections.OrderedDict(sorted(dict(zip(["BRG", "NIM", "PER", "STR", "VIT", "WIT"], attrmod(list(self.attrs.values())))).items()))
		self.bgmod()
		self.pack = pack
		self.packmod()
		for i in range(5):
			self.ordincskill()
		#self.setreas()
		self.defence = 10 + self.attrs["NIM"]
		self.hp = self.attrs["VIT"] + self.attrmods["STR"]
		if self.race in hobbits:
			self.wounds = 5
		else:
			self.wounds = 6
		self.courage = 3
		self.renown = 0

#Main program
def createchar():
	name = input("Enter name: ")
	race = input("Enter race: ")
	order = input("Enter order: ")
	background = input("Enter background: ")
	gender = input("Enter Gender: ")

	char = Char(name, race, order, background, pack, gender)
	print('Saving to file')
	char.save()
