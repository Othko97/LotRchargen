"""Character Class for LotR DnD"""

#########
#IMPORTS#
#########

from data import *
import random as R
import collections
import os
import pickle

###########
#CONSTANTS#
###########

npcparameters = ['name', 'race', 'order', 'attrs', 'attrmods', 'reas', 'hp', 'wls', 'dfce', 'cou', 'corr', 'skills', 'traits', 'abilities', 'level', 'ren', 'langs', 'lore']
pcparameters  = ['gender', 'age', 'birthday', 'height', 'weight', 'hair', 'eyes', 'skin', 'handedness', 'homeland']


################################
#DEFINING CLASSES AND FUNCTIONS#
################################

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


#ROLL 2 D6
#
#Simulates rolling of 2d6
    #Returns integer

def twoDsix():
	x = R.randint(1,6)
	y = R.randint(1,6)
	return(x+y)


#MATRIX ADDITION FOR LISTS
#
#Adds two lists together elementwise
    #Returns list

def add(list1, list2):
	list = []
	for i in range(len(list1)):
		list.append(list1[i]+list2[i])
	return(list)


#ATTRIBUTE MODIFIERS
#
#Calculates attribute modifiers for a given set of attributes
    #Returns list of modifiers

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



##################
#CHARACTER OBJECT#
##################

class Char():

	def __init__(self, name, race, order, attrs, attrmods, reas, hp, wls, dfce, cou, corr, skills, traits, abilities, level, ren, langs, lore):
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
		self.ren = ren
		self.langs = langs
		self.lore = lore
		print("\nCharacter Created!\n")

	def update(self, name, race, order, attrs, attrmods, reas, hp, wls, dfce, cou, corr, skills, traits, abilities, level, ren, langs, lore):
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
		self.ren = ren
		self.langs = langs
		self.lore = lore
		self.save()
		print("\nCharacter Updated!\n")

	def save(self):
		cwd = os.getcwd()
		dirname = os.path.join(cwd, 'characters')
		if not os.path.exists(dirname):
			os.makedirs(dirname)
		os.chdir(dirname)
		with open(self.name + '.txt', 'w+') as char:

			char.write('Name: ' + self.name)
			char.write('\nLevel: ' +str(self.level))
			char.write('\nRace: ' + races[self.race])
			char.write('\nOrders:\n')
			for i in self.order:
				char.write(i + '\n')
			char.write('\n\nAttributes:\n')
			buffer = []
			for i in self.attrs:
				buffer.append([str(i), str(self.attrs[i]), str(self.attrmods[i])])
			col_width = max(len(word) for row in buffer for word in row) + 2  # padding
			for row in buffer:
				char.write(row[0].ljust(4) + row[1].ljust(col_width) + row[2].ljust(3)+"\n")
			char.write('\n\nReactions: \n')
			for i in self.reas:
				char.write('\n' + str(i) + '\t' +  str(self.reas[i]))
			char.write('\n\nHP: ' + str(self.hp))
			char.write('\nWound Levels: ' + str(self.wls))
			char.write('\nDefence: ' + str(self.dfce))
			char.write('\nCourage: ' + str(self.cou))
			char.write('\nCorruption: ' + str(self.corr))
			char.write('\nRenown: ' + str(self.ren))
			char.write('\n\nSkills:\n')
			buffer = []
			for i in self.skills:
				buffer.append([str(i), str(skillnames[i]), str(self.skills[i])])
			col_width = max(len(word) for row in buffer for word in row) + 2  # padding
			for row in buffer:
				char.write(row[0].ljust(4) + row[1].ljust(col_width) + row[2].ljust(3)+"\n")
			char.write('\n\nTraits:\n')
			buffer = []
			for i in self.traits:
				if self.traits[i] > 0:
					buffer.append([str(i), str(traitnames[i]), str(self.traits[i])])
			col_width = max(len(word) for row in buffer for word in row) + 2  # padding
			for row in buffer:
				char.write(row[0].ljust(4) + row[1].ljust(col_width) + row[2].ljust(3)+"\n")
			char.write('\n\nAbilities: ')
			for i in self.abilities:
				char.write('\n' + i)
			char.write('\n\nLanguages: ')
			for i in self.langs:
				char.write('\n' + i[0])
			char.write('\n\nLore Skills: ')
			for i in self.lore:
				char.write('\n' + i[0])

		dirname = os.path.join(cwd, 'characters','storage')
		if not os.path.exists(dirname):
			os.makedirs(dirname)
		os.chdir(dirname)
		with open(self.name + '.py', 'wb') as char:
			pickle.dump(self, char)

		os.chdir(cwd)

	def output(self):
		print('Name: ' + self.name)
		print('\nRace: ' + races[self.race])
		print('\nOrders:\n')
		for i in self.order:
			print(i + '\n')
		print('\n\nAttributes:')
		buffer = []
		for i in self.attrs:
			buffer.append([str(i), str(self.attrs[i]), str(self.attrmods[i])])
		col_width = max(len(word) for row in buffer for word in row) + 2  # padding
		for row in buffer:
			print(row[0].ljust(4) + row[1].ljust(col_width) + row[2].ljust(3)+"\n")
		print('\n\nReactions:')
		for i in self.reas:
			print('\n' + str(i) + '\t' +  str(self.reas[i]))
		print('\n\nHP: ' + str(self.hp))
		print('\nWound Levels: ' + str(self.wls))
		print('\nDefence: ' + str(self.dfce))
		print('\nCourage: ' + str(self.cou))
		print('\nCorruption: ' + str(self.corr))
		print('\n\nSkills:')
		buffer = []
		for i in self.skills:
			buffer.append([str(i), str(skillnames[i]), str(self.skills[i])])
		col_width = max(len(word) for row in buffer for word in row) + 2  # padding
		for row in buffer:
			print(row[0].ljust(4) + row[1].ljust(col_width) + row[2].ljust(3)+"\n")
		print('\n\nTraits:')
		buffer = []
		for i in self.traits:
			if self.traits[i] > 0:
				buffer.append([str(i), str(traitnames[i]), str(self.traits[i])])
		col_width = max(len(word) for row in buffer for word in row) + 2  # padding
		for row in buffer:
			print(row[0].ljust(4) + row[1].ljust(col_width) + row[2].ljust(3)+"\n")
		print('\n\nAbilities: ')
		for i in self.abilities:
			print(i + "\n")




###################
#PLAYER CHARACTERS#
###################
class Player(Char):
	def __init__(self, name, race, order, attrs, attrmods, reas, hp, wls, dfce, cou, corr, skills, traits, abilities, level, ren, langs, lore, gender, age, birthday, height, weight, hair, eyes, skin, handedness, homeland):
		Char.__init__(self, name, race, order, attrs, attrmods, reas, hp, wls, dfce, cou, corr, skills, traits, abilities, level, ren, langs, lore)
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

	def update(self, name, race, order, attrs, attrmods, reas, hp, wls, dfce, cou, corr, skills, traits, abilities, level, gender, age, birthday, height, weight, hair, eyes, skin, handedness, homeland):
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
		super(Player, self).update(name, race, order, attrs, attrmods, reas, hp, wls, dfce, cou, corr, skills, traits, abilities, level, ren, langs, lore)

	def save(self):
		super(Player, self).save()
		cwd = os.getcwd()
		os.chdir(os.path.join(cwd, 'characters'))
		with open(self.name + ".txt", "a") as char:
			char.write("\n\nPersonal Details:")
			char.write("\nGender: "  + self.gender)
			char.write("\nAge: " + self.age)
			char.write("\nBirthday: " + self.birthday)
			char.write("\nHeight: " + self.height)
			char.write("\nWeight: " + self.weight)
			char.write("\nHair Colour: " + self.hair)
			char.write("\nEye Colour: " + self.eyes)
			char.write("\nSkin Colour: " + self.skin)
			char.write("\nHandedness: " + self.handedness)
			char.write("\nHomeland: " + self.homeland)
		os.chdir(cwd)

	def output(self):
		super(Player, self).output()
		print("\n\nPersonal Details:")
		print("\nGender: "  + self.gender)
		print("\nAge: " + self.age)
		print("\nBirthday: " + self.birthday)
		print("\nHeight: " + self.height)
		print("\nWeight: " + self.weight)
		print("\nHair Colour: " + self.hair)
		print("\nEye Colour: " + self.eyes)
		print("\nSkin Colour: " + self.skin)
		print("\nHandedness: " + self.handedness)
		print("\nHomeland: " + self.homeland)




#TESTING
#
#Earendil = Char(name="Earendil",
#race="NOL",
#order=["MAR"],
#attrs=collections.OrderedDict(sorted({"BRG":0, "NIM":0, "PER":0, "STR":0, "VIT":0, "WIT":0}.items())),
#attrmods=collections.OrderedDict(sorted({"BRG":0, "NIM":0, "PER":0, "STR":0, "VIT":0, "WIT":0}.items())),
#reas=collections.OrderedDict(sorted({"STA":0, "SWI":0, "WIL":0, "WIS":0}.items())),
#hp=10,
#wls=5,
#dfce=10,
#cou=3,
#corr=0,
#skills=collections.OrderedDict(sorted({
#"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
#"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":4, "RUN":4, "SEA":0, "SRC":0, "SIE":0, "SMI":2, "STE":4, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
#"WEA":0
#}.items())),
#traits=collections.OrderedDict(sorted({
#"ACC":0, "ALL":0, "AMB":0, "AOH":0, "BOL":0, "CHL":0, "COM":0, "CRF":0, "CUR":0, "DOD":0, "DOU":0, "ELF":0, "ELO":0, "FAI":0, "FTH":0, "FOF":0, "FEH":0, "FOR":0,
#"FRI":0, "FUR":0, "GOT":0, "HAM":0, "HAR":0, "HEL":0, "HOA":0, "HOT":0, "HOI":0, "INC":0, "IND":0, "EAR":0, "EYE":0, "NOS":0, "LIO":0, "NIT":0, "QUI":0, "RAN":0,
#"RES":0, "STE":0, "STW":0, "SWR":0, "TIR":0, "TRV":0, "TWO":0, "VAT":0, "VAR":0, "WAK":0, "WAH":0, "WAW":0, "WAR":0, "WEM":0, "WIS":0, "WOO":0, "ARR":0, "BAT":0,
#"COH":0, "CRV":0, "CRI":0, "DAR":0, "DUM":0, "DEA":0, "DEY":0, "DUT":0, "ENE":0, "FEA":0, "FEY":0, "GRA":0, "HAT":0, "OAT":0, "PRO":0, "REC":0, "RIV":0, "SLO":0,
#"STI":0, "WEK":0, "WEW":0
#}.items())),
#abilities=[],
#level=1,
#ren=0,
#langs=["Sindarin"],
#lore=["Gondolin", "Sea"]
#)
#
#Earendil.save()
