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
                        curchar.save()
                    

                    elif field in pcparameters:
                        if isinstance(curchar, Player):
                            setattr(curchar, field, input(">> "))
                        else:
                            print("Not a player character\n")
                    

                    elif field == name:
                        curchar.name = input(">> ")
                    

                    elif field == "race":
                        race = 'START'	#placeholder
                        while race not in races.keys():
                            race = input('>> ').upper()
                            if race == "LIST":
                                print(racelist)
                        curchar.race = race
                    

                    elif field == "order":
                        choice = input("ADD or EDIT: ").upper()
                    
                        if choice == "ADD":
                            ord = 'START'
                            while ord not in orders.keys():
                                ord = input('>> ').upper()
                                if ord == "LIST":
                                    print("ORDER LIST:\n")
                                    for i in orders:
                                        print(i + ": " + orders[i])
                                    print()
                            curchar.order.append(ord)
                    
                        elif choice == "EDIT":
                            for i in curchar.order:
                                print(i + ':' + orders[i])
                            choice = input("Order: ").upper()
                            if choice in curchar.order:
                                curchar.order.remove(choice)
                                ord = 'START'
                                while ord not in list(orders.keys()) + [""]:
                                    ord = input('>> ').upper()
                                    if ord == "LIST":
                                        print("ORDER LIST:\n")
                                        for i in orders:
                                            print(i + ": " + orders[i])
                                        print()
                                if ord != "":
                                    curchar.order.append(ord)
                    
                            else:
                                print("Order not current\n")
                        else:
                            print("Must be 'ADD' or 'EDIT'\n")
                    
                    
                    elif field in list(curchar.attrs.keys()) + [s + 'mod' for s in list(curchar.attrs.keys())] + list(curchar.reas.keys()) + npcparameters[5:11] + ["level", "ren"]:
                        val = None
                        while not isinstance(val, int):
                            try:
                                val = int(input(">> "))
                            except ValueError:
                                pass

                        if field in list(curchar.attrs.keys()):
                            curchar.attrs[field] = val
                        elif field in [s + 'mod' for s in list(curchar.attrs.keys())]:
                            curchar.attrmods[field[:-3]] = val
                        elif field in list(curchar.reas.keys()):
                            curchar.reas[field] = val
                        else:
                            setattr(curchar, field, val)


                    elif field == "skills":
                        ski = None
                        while ski not in QUIT:
                            ski = input("Enter Skill: ").upper()
                            if ski in curchar.skills.keys():
                                val = None
                                while not isinstance(val, int):
                                    try:
                                        val = int(input(">> "))
                                    except ValueError:
                                        pass
                                curchar.skills[ski] = val
                            else:
                                print("Not a skill.\n")
                    

                    elif field == "traits":
                        trt = None
                        while trt not in QUIT:
                            trt = input("Enter Trait: ").upper()
                            if trt in curchar.traits.keys():
                                val = None
                                while val not in list(range(traitmaxes[trt])):
                                    try:
                                        val = int(input(">> "))
                                    except ValueError:
                                        pass
                                curchar.traits[trt] = val
                            else:
                                print("Not a trait.\n")


                    elif field == "abilities":
                        #Display available abilities
                        abilities = [i for order in curchar.order for i in orderabils[order]]
                        for i in range(len(abilities)):
                            print(str(i) + ": " + abilities[i])
                        
                        #Handle user input
                        ability = -1
                        while ability not in list(range(len(abilities))):
                            ability = int(input(">> "))
                        
                        curchar.abilities.append(abilities[ability])

                    
                    elif field in ["langs", "lore"]:
                        check = 0
                        lanlor = input(">> ")
                        llist = getattr(curchar, field)
                        for x in llist:
                            if lanlor == x[0]:
                                x[1] += 1
                                check = 1
                            if check ==  0:
                                llist.append([lanlor, 1])
                        setattr(curchar, field, llist)


                    else:
                        pass
                    
                        
            else:
                print("No character loaded!\n")
        


        else:
            pass

app()
            

            
