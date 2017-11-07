from data import *

invskillnames = {y.upper():x for x,y in skillnames.items()}

run = True
while run:
    query = input(">> ")
    if query.lower() == "quit":
        run = False
    elif query.upper() in skillnames:
        print(skillnames[query.upper()])
    elif query.upper() in  invskillnames:
        print(invskillnames[query.upper()])