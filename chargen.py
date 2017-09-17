"""creates characters in LotR system"""

#IMPORTS

import random as R
import os
import collections
from data import *
from char import *


#DEFINING CLASSES AND FUNCTIONS

def racincskill(race, skills, traits):
	racstufflist = []
	print("\nEnter 3 letter skill/trait code to increase \n")
	print("SKILLS: ")
	for x in racskills[race]:
		print(x, skillnames[x], skills[x])
		racstufflist.append(x)
	print("\nTRAITS: ")
	for x in ractraits[race]:
		print(x, traitnames[x], traits[x])
		racstufflist.append(x)
	inc = input("Enter code: ")
	if inc == "RND":
		i = R.randint(1,len(racstufflist))-1
		if i < len(racskills[race]):
			skills[racstufflist[i]] += 1
			return(1)
		else:
			traits[racstufflist[i]] += 1
			return(1)
	if inc in skills:
		skills[inc] += 1
		return(1)
	elif inc in traits:
		if traits[inc] < traitmaxes[inc]:
			traits[inc] += 1
			return(1)
		else:
			print("Already taken to maximum level")
			return(0)

def ordincskill(self):
	print("\nEnter 3 letter skill code to increase \n")
	orskillist = []
	for x in orderskills[order]:
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

def createchar():
	#Takes PC specific data
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
	else:	#Takes NPC data only
		name = input("Character Name: ")

	#loops until valid race given
	race = 'START'	#placeholder
	while race not in races.keys():
		race = input('Race: ').upper()
		if race == "LIST":
			print(racelist)

	#loops until valid order given
	order = 'START'
	while order not in orders.keys():
		order = input('Order: ').upper()
		if order == "LIST":
			print("ORDER LIST:\n")
			for i in orders:
				print(i + ": " + orders[i])
			print()

	if input("Roll random attributes? (Y/n): ").upper() == "N":
		attrs = collections.OrderedDict(sorted({"BRG":input("BRG: "), "NIM":input("NIM: "), "PER":input("PER: "), "STR":input("STR: "), "VIT":input("VIT: "), "WIT":input("WIT: ")}.items()))
	else:
		rolls = []
		for i in range(9):
			rolls.append(twoDsix())		#rolls 9, takes highest 6
		rolls.sort(reverse=True)
		rolls = rolls[:6]
		R.shuffle(rolls)				#randomises order
		attrs = collections.OrderedDict(sorted(dict(zip(["BRG", "NIM", "PER", "STR", "VIT", "WIT"],rolls)).items()))
	attrs = collections.OrderedDict(sorted(dict(zip(list(attrs.keys()), add(list(attrs.values()),list(racattradjs[race].values())))).items()))

	attrmods = collections.OrderedDict(sorted(dict(zip(["BRG", "NIM", "PER", "STR", "VIT", "WIT"], attrmod(list(self.attrs.values())))).items()))

	reas = collections.OrderedDict(sorted({"STA":0, "SWI":0, "WIL":0, "WIS":0}.items()))
	reas["STA"] = max([attrmods["STR"], attrmods["VIT"]])
	reas["SWI"] = max([attrmods["NIM"], attrmods["PER"]])
	reas["WIL"] = max([attrmods["BRG"], attrmods["WIT"]])
	reas["WIS"] = max([attrmods["BRG"], attrmods["PER"]])

	hp = attrs["VIT"] + attrmods["STR"]

	if race in hobbits:
		wls = 5
	else:
		wls = 6

	dfce = 10 + attrs["NIM"]
	cou = 3
	corr = 0
	ren = 0
	level = 1

	skills = skilltemp
	traits = traitstemp

	print("Choose a background from the list below:\nBACKGROUNDS: \n")
	for i in backs[race]:
		print(i)
	print()
	bg = input("Enter background (default N): ").upper()
	if bg in backs[race]:
		skills = collections.OrderedDict(sorted(dict(zip(list(skills.keys()), add(list(skills.values()),list(bgskilladjs[bg].values())))).items()))
	else:
		i = 0
		while i < 6:
			i += racincskill(race, skills, traits)

	#adds racial mods for character's race
	attrs = collections.OrderedDict(sorted(dict(zip(list(attrs.keys()), add(list(attrs.values()),list(racattradjs[race].values())))).items()))

	#adds 3*WIT to language and lore
	for i in range(attrs["WIT"]*3):	#make
		if R.randint(1,2) == 1:		#this
			skills["LAN"] += 1		#better
		else:						#pls
			skills["LOR"] += 1		#tom

	print("Choose a package from the list below:\nPACKAGES: \n")
	availablepacks = []
	for j in packs[order]:
		print(j)
		availablepacks.append(j)
	print()
	pack = input("Enter package (default basic [first order]): ").upper()
	if pack not in availablepacks:
		pack = "B" + orders
	else:
		skills = collections.OrderedDict(sorted(dict(zip(list(skills.keys()), add(list(skills.values()),list(packskilladjs[pack].values())))).items()))

	for i in range(5):
		ordincskill()
