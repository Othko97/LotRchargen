"""creates characters in LotR system"""

#########
#IMPORTS#
#########

import random as R
import os
import collections
from data import *
from char import *




################################
#DEFINING CLASSES AND FUNCTIONS#
################################

#MAY MOVE THIS SECTION TO CHAR.PY

#RACIAL SKILL INCREASE
#
#Increase a racial skill or trait
	#Returns 3-tuple of skills, traits and a check that a skill was actually increased

def racincskill(race, skills, traits):
	racstufflist = []
	print("\nEnter 3 letter skill/trait code to increase \n")

	#Gather & display relevant skills
	print("SKILLS: ")
	for x in racskills[race]:
		print(x, skillnames[x], skills[x])
		racstufflist.append(x)
	
	#Gather & display relevant traits
	print("\nTRAITS: ")
	for x in ractraits[race]:
		print(x, traitnames[x], traits[x])
		racstufflist.append(x)
	
	#Handle User Input
	inc = input("Enter code: ").upper()
	
	#Increment random value from list
	if inc == "RND":
		check = 0
		while check == 0:
			i = R.randint(1,len(racstufflist))-1
			if i < len(racskills[race]):
				skills[racstufflist[i]] += 1
				check = 1
				return([skills, traits, 1])
			else:
				if traits[racstufflist[i]] < traitmaxes[racstufflist[i]]:
					traits[racstufflist[i]] += 1
					check = 1
					return([race, skills, traits, 1])
	
	#Increment skill from list
	elif inc in skills:
		skills[inc] += 1
		return([skills, traits, 1])

	#Increment trait from list
	elif inc in traits:
		if traits[inc] < traitmaxes[inc]:
			traits[inc] += 1
			return([skills, traits, 1])
		else:
			print("Already taken to maximum level")
			return([skills, traits, 0])
	
	#Handle case where code not valid
	else:
		print("Not a valid code")
		return([race, skills, traits, 0])


#INCREASE ORDER SKILL
#
#Increase an order skill
	#Returns a 2-tuple of skills and a check that a skill was increased

def ordincskill(order, skills):
	print("\nEnter 3 letter skill code to increase \n")
	orskillist = []

	#Gather & display relevant skills
	for o in order:
		for x in orderskills[o]:
			if x in orskillist:
				pass
			else:
				orskillist.append(x)
				print(x, skillnames[x], skills[x])
	
	#Handle User Input
	inc = input("Enter code: ").upper()
	#Increment random skill in list
	if inc == "RND":
		skills[orskillist[R.randint(1,len(orskillist))-1]] += 1
		return([skills, 1])

	#Increment user-chosen skill
	if inc in skills:
		skills[inc] += 1
		return([skills, 1])

	#Handle case where code not valid
	else:
		print("Not a valid code")
		return([skills, 0])


#CHOOSE PACKAGE TRAIT
#
#Choose an edge for a background package
	#Returns a 2-tuple of traits and a check that a trait was actually taken

def packagechoosetrait(order, pack, traits):
	print("\nEnter 3 letter trait code to choose \n")

	#Display available traits
	for trait in ordertraits[order][pack]:
		print(trait, traitnames[trait], traits[trait])
	
	#Handle User Input
	inc = input("Enter code: ").upper()

	#Take random trait from list
	if inc == "RND":
		traits[ordertraits[order][pack][R.randint(1,5)]] += 1
	
	#Increment User-chosen trait
	if inc in traits:
		if traits[inc] < traitmaxes[inc]:
			traits[inc] += 1
			return([traits, 1])
		else:
			print("Already taken to maximum level")
			return([traits, 0])
	
	#Handle case where code not valid
	else:
		print("Not a valid code")
		return([traits, 0])

#CHOOSE AN EDGE
#
#Takes an edge
	#Returns a 2-tuple of traits and a check

def choosetrait(traits):
	print("\nEnter 3 letter trait code to choose \n")

	#Display edges
	for trait in edges:
		print(trait, traitnames[trait], traits[trait])

	#Handle User Input
	inc = input("Enter code: ").upper()

	#Increment random edge
	if inc == "RND":
		check = 0
		while check == 0:
			x = R.randint(0, len(edges)-1)
			if traits[edges[x]] < traitmaxes[edges[x]]:
				traits[edges[x]] += 1
				check = 1

	#Increment User-chosen trait
	elif inc in traits:																
		if traits[inc] < traitmaxes[inc]:
			traits[inc] += 1
			return([traits, 1])
		else:
			print("Already taken to maximum level")
			return([traits, 0])
	
	#Handle case where code not valid
	else:
		print("Not a valid code")
		return([traits, 0])





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
				langs.append([loreskill, 1])
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
		char = Player(name, race, order, attrs, attrmods, reas, hp, wls, dfce, cou, corr, skills, traits, abilities, level, gender, age, birthday, height, weight, hair, eyes, skin, handedness, homeland)
	else:
		char = Char(name, race, order, attrs, attrmods, reas, hp, wls, dfce, cou, corr, skills, traits, abilities, level, ren, langs, lore)
	 
	char.output()
	char.save()


#TESTING
createchar()