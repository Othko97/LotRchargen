"""Miscellaneous functions used frequently"""

#########
#IMPORTS#
#########
import random as R


###########
#FUNCTIONS#
###########

#ROLL 2 D6
def twoDsix():
	"""Simulates the rolling of 2d6
		 Returns an int in the range (1, 12)"""
	x = R.randint(1,6)
	y = R.randint(1,6)
	return x+y


#MATRIX ADDITION FOR LISTS
def add(list1, list2):
	"""Element-wise addition on lists
		 Returns a list"""
	return [i1 + i2 for i1,i2 in zip(list1, list2)]


#ATTRIBUTE MODIFIERS
def attrmod(list):
	"""Calculates modifiers for a list of attributes
		 Returns a list of modifiers"""
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
def evenspace(header, buffer, file=None):
	"""Spaces data evenly into columns for pretty printing
		 Prints a table, returns nothing"""
  buffer.insert(0, header)
  numcols = len(header)
  col_widths = [(max(len(str(row[i])) for row in buffer) + 2) for i in range(numcols)]
  for row in buffer:
    printline = ""
    for i in range(numcols):
      printline += str(row[i]).ljust(col_widths[i])
    if file is None:
			print(printline)
		else:
			file.write(printline)