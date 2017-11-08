"""Main program to be run for Character Generator"""

#########
#IMPORTS#
#########

import os
import pickle
from char import *
from chargen import *
from data import *
from traittranslator import *
from skilltranslator import *

###############
#MAIN FUNCTION#
###############

def app():
    run = True
    curchar = None

    while run == True:
        command = input("> ").upper()

        if command == "QUIT":
            run = False

        elif command == "NEW":
            curchar = createchar()

        elif command == "SKILL":
            skilltrans()

        elif command == "TRAIT":
            traittrans()

        elif command == "LOAD":
            cwd = os.getcwd()
            dirname = os.path.join(cwd, 'characters', 'storage')
            chars = os.listdir(dirname)
            print("\nAvailable Characters:")
            for i in range(len(chars)):
                chars[i] = chars[i].split('.')[0]
                print(chars[i])
            print()
            name = input("Name: ")
            if name in chars:
                curchar = pickle.load(open(os.path.join(dirname, name + '.py'), 'rb'))
            else:
                print('No such Character\n')
        
        elif command == "PRINT":
            if curchar != None:
                curchar.output()
        


app()
            

            
