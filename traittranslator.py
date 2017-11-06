from data import *

invtraitnames = {y.upper():x for x,y in traitnames.items()}

run = True
while run:
    query = input(">> ")
    if query.lower() == "quit":
        run = False
    elif query.upper() in traitnames:
        print(traitnames[query.upper()])
    elif query.upper() in  invtraitnames:
        print(invtraitnames[query.upper()])
