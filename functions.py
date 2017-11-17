"""Miscellaneous functions used frequently"""

#########
#IMPORTS#
#########
import random as R


###########
#FUNCTIONS#
###########

#ROLL 2 D6
	#Simulates rolling of 2d6
  #Returns integer

def twoDsix():
	x = R.randint(1,6)
	y = R.randint(1,6)
	return(x+y)


#MATRIX ADDITION FOR LISTS
	#Adds two lists together elementwise
  #Returns list

def add(list1, list2):
	list = []
	for i in range(len(list1)):
		list.append(list1[i]+list2[i])
	return(list)


#ATTRIBUTE MODIFIERS
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

#EQUAL SPACED PRINTING
  #Spaces lists of data into columns
  #Prints a list of strings ready to be printed line by line

def evenspace(header, buffer):
  buffer.insert(0, header)
  numcols = len(header)
  print(numcols)
  col_widths = [(max(len(row[i]) for row in buffer) + 2) for i in range(numcols)]
  for row in buffer:
    printline = ""
    for i in range(numcols):
      printline += row[i].ljust(col_widths[i])
    print(printline)