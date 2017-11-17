"""System to level up a character"""

#########
#IMPORTS#
#########
from char import *
from data import *
#imports for testing only, remove later
import os 
import pickle 

###################
#LEVEL UP FUNCTION#
###################

def levelup(char):
  points = 5
  while points > 0:
    print ("\nChoose an advancement from the list below: \n")
    
    buffer = [["NUM", "CODE", "EFFECT", "COST"]]
    for level in range(points):
      for opt in advpoints[level]:
        buffer.append([opt, advops[opt], str(level + 1)])
    col_widths = [(max(len(row[i]) for row in buffer) + 2) for i in range(3)]  # padding
    print(col_widths)
    for row in buffer:
      print(row[0].ljust(col_widths[0]) + row[1].ljust(col_widths[1]) + row[2].ljust(col_widths[2])+"\n")
    
    code = input("> ").upper()

#########
#TESTING#
#########
cwd = os.getcwd()

charpath = os.path.join(cwd, 'characters', 'storage', 'a.py')

a = pickle.load(open(charpath, 'rb'))

levelup(a)