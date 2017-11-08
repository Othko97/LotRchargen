"""Main program to be run for Character Generator"""

#########
#IMPORTS#
#########

import os
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
        command = input(">>> ").upper()
        if command == "QUIT":
            run = False
        elif command == "NEW":
            curchar = createchar()
        elif command == "SKILL":
            skilltrans()
        elif command == "TRAIT":
            traittrans()
        elif command == "LOAD":