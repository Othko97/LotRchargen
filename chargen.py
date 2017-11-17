"""creates characters in LotR system"""

#########
#IMPORTS#
#########

import random as R
import os
import collections
from data import *
from char import *
from functions import *




##################################
#MAIN CHARACTER CREATION FUNCTION#
##################################

def createchar():
	#Takes PC specific data
	if input("Player Character? (y/N): ").upper() == "Y":
		pc = True
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
		pc = False
		name = input("Character Name: ")

	#Loops until valid race given
	race = 'START'	#placeholder
	while race not in races.keys():
		race = input('Race: ').upper()
		if race == "LIST":
			print(racelist)

	#Loops until valid order given
	order = 'START'
	while order not in orders.keys():
		order = input('Order: ').upper()
		if order == "LIST":
			print("ORDER LIST:\n")
			for i in orders:
				print(i + ": " + orders[i])
			print()

	#Roll/Choose attributes
	if input("Roll random attributes? (Y/n): ").upper() == "N":	#user input of attributes
		attrs = collections.OrderedDict(sorted({"BRG":input("BRG: "), "NIM":input("NIM: "), "PER":input("PER: "), "STR":input("STR: "), "VIT":input("VIT: "), "WIT":input("WIT: ")}.items()))
	#Random Roll of attributes
	else:
		rolls = []
		for i in range(9):
			rolls.append(twoDsix())		#rolls 9, takes highest 6
		rolls.sort(reverse=True)
		rolls = rolls[:6]
		R.shuffle(rolls)				#randomises order
		attrs = collections.OrderedDict(sorted(dict(zip(["BRG", "NIM", "PER", "STR", "VIT", "WIT"],rolls)).items()))
	
	#Find attribute modifiers
	attrmods = collections.OrderedDict(sorted(dict(zip(["BRG", "NIM", "PER", "STR", "VIT", "WIT"], attrmod(list(attrs.values())))).items()))

	#Find reactions
	reas = collections.OrderedDict(sorted({"STA":0, "SWI":0, "WIL":0, "WIS":0}.items()))
	reas["STA"] = max([attrmods["STR"], attrmods["VIT"]])
	reas["SWI"] = max([attrmods["NIM"], attrmods["PER"]])
	reas["WIL"] = max([attrmods["BRG"], attrmods["WIT"]])
	reas["WIS"] = max([attrmods["BRG"], attrmods["PER"]])

	#Find HP
	hp = attrs["VIT"] + attrmods["STR"]

	#Set wound levels
	if race in hobbits:
		wls = 5
	else:
		wls = 6

	#Set defence, courage, corruption, renown and level (to 1)
	dfce = 10 + attrs["NIM"]
	cou = 3
	corr = 0
	ren = 0
	level = 1

	#Create empty lists of skills, traits
	skills = skilltemp
	traits = traitstemp


	#RACIAL BACKGROUND
	print("Choose a background from the list below:\nBACKGROUNDS: \n")
	#Display options
	for i in backs[race]:
		print(i + ": " + backs[race][i])
	print()
	#Handle User Input
	bg = input("Enter background (default N): ").upper()
	
	#Adds background modifiers, or runs no background
	if bg not in backs[race]:
		bg = "N"
	
	skills = collections.OrderedDict(sorted(dict(zip(list(skills.keys()), add(list(skills.values()),list(bgskilladjs[bg].values())))).items()))
	
	if bg == "N":
		i = 0
		while i < 6: 
			templist = racincskill(race, skills, traits)
			skills = templist[0]
			traits = templist[1]
			i += templist[2]

	#adds racial mods for character's race
	attrs = collections.OrderedDict(sorted(dict(zip(list(attrs.keys()), add(list(attrs.values()),list(racattradjs[race].values())))).items()))

	#adds 3*WIT to language and lore
	print("Add 3x WIT to language and lore skills.\n")
	langs = []
	lore = []
	i = 0
	while i < 3*attrs["WIT"]:
		print("\n" + str(3*attrs["WIT"]-i) + " to choose.")
		choice = input("LAN/LOR: ").upper()

		if choice == "LAN":
			language = input("Enter language: ")
			check = 0
			for x in langs:
				if language == x[0]:
					x[1] += 1
					check = 1
			if check == 0:
				langs.append([language, 1])
			i += 1
		
		elif choice == "LOR":
			loreskill = input("Enter lore skill: ")
			check = 0
			for x in lore:
				if loreskill == x[0]:
					x[1] += 1
					check = 1
			if check == 0:
				lore.append([loreskill, 1])
			i += 1
		
		else:
			print("Must be either 'LAN' or 'LOR'\n")



	#ORDER PACKAGES
	print("Choose a package from the list below:\nPACKAGES: \n")
	availablepacks = []
	#Gather & display available packages
	for j in packs[order]:
		print(j + ": " + packs[order][j])
		availablepacks.append(j)
	print()

	#Handle User Input
	pack = input("Enter package (default basic [order]): ").upper()
	#Adds package skills, defaults to no basic [order]
	if pack not in availablepacks:
		pack = "B" + order
	else:
		skills = collections.OrderedDict(sorted(dict(zip(list(skills.keys()), add(list(skills.values()),list(packskilladjs[pack].values())))).items()))
	#Handle case of no package
	if pack == "N":
		i=0
		while i < 15:
			templist = ordincskill([order], skills)
			skills = templist[0]
			i +=  templist[1]

	#Add 5 free picks of order skills
	i=0
	while i < 5:
		templist = ordincskill([order], skills)
		skills = templist[0]
		i +=  templist[1]
	
	#For no package, choose any edge
	if pack == "N":
		i = 0
		while i < 1:
			templist = choosetrait(traits)
			traits = templist[0]
			i += templist[1]
	#For packages, choose from edges listed
	else:
		i = 0
		while i < 1:
			templist = packagechoosetrait(order, pack, traits)
			traits = templist[0]
			i += templist[1]
	
	#ORDER ABILITIES
	abilities = []
	print("Choose an order ability from the list below:\nABILITIES: \n")
	#Display available abilities
	for i in range(len(orderabils[order])):
		print(str(i) + ": " + orderabils[order][i])
	
	#Handle user input
	ability = -1
	while ability not in list(range(len(orderabils[order]))):
		ability = int(input("Enter Number: "))
	
	abilities.append(orderabils[order][ability])


	#Create character object
	if pc:
		char = Player(name, race, [order], attrs, attrmods, reas, hp, wls, dfce, cou, corr, skills, traits, abilities, level, ren, langs, lore, gender, age, birthday, height, weight, hair, eyes, skin, handedness, homeland)
	else:
		char = Char(name, race, [order], attrs, attrmods, reas, hp, wls, dfce, cou, corr, skills, traits, abilities, level, ren, langs, lore)
	 
	char.output()
	char.save()
	return(char)


#TESTING
#createchar()