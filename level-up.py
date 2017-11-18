"""System to level up a character"""

#########
#IMPORTS#
#########
from char import *
from data import *
from functions import *
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
    
    header = ["NUM", "CODE", "EFFECT", "COST"]
    buffer = []
    count = 1
    for level in range(points):
      for opt in advpoints[level]:
        buffer.append([str(count), opt, advops[opt], str(level + 1)])
        count += 1

    evenspace(header, buffer)

    code = input("> ").upper()

#########
#TESTING#
#########
cwd = os.getcwd()

charpath = os.path.join(cwd, 'characters', 'storage', 'a.py')

a = pickle.load(open(charpath, 'rb'))

levelup(a)