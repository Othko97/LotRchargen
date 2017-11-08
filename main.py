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

        if command in QUIT:
            run = False

        elif command in NEW:
            curchar = createchar()

        elif command in SKILL:
            skilltrans()

        elif command in TRAIT:
            traittrans()

        elif command in LOAD:
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
        
        elif command in PRINT:
            if curchar != None:
                curchar.output()
            else:
                print("No character loaded!\n")

        elif command in EDIT:
            if curchar != None:
                editing = True
                while editing == True:
                    field = input("Enter Field: ").lower()
                    if field in done:
                        editing = False
                    
                        
            else:
                print("No character loaded!\n")
        


app()
            

            
