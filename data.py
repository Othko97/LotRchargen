"""Holds lists of races, orders, traits, etc"""

import collections

#CONSOLE COMMANDS
QUIT = ["QUIT", "Q", "EXIT"]
NEW = ["NEW", "NEW CHAR", "CREATE", "CREATE CHAR"]
SKILL = ["SKILL", "TRANSLATE SKILLS", "TRANSLATE SKILL", "SKILL TRANSLATE", "TRNSL SKL"]
TRAIT = ["TRAIT", "TRANSLATE TRAITS", "TRANSLATE TRAIT", "TRAIT TRANSLATE", "TRNSL TRT"]
LOAD = ["LOAD", "IMPORT", "EXISTING CHAR", "OPEN"]
PRINT = ["PRINT", "OUTPUT", "DISPLAY"]
EDIT = ["EDIT", "ALTER", "CHANGE"]

done = ["save", "done", "end", "finished"]

#ATTRIBUTES
attrtemp = collections.OrderedDict(sorted({"BRG":0, "NIM":0, "PER":0, "STR":0, "VIT":0, "WIT":0}.items()))

#REACTIONS
reactemp = collections.OrderedDict(sorted({"STA":0, "SWI":0, "WIL":0, "WIS":0}.items()))

#RACES
races = {"DWA":"Dwarf", "NOL":"Noldo", "SIN":"Sinda", "SIL":"Silva", "FAL":"Fallohide", "HAR":"Harfoot", "STO":"Stoor", "DUN":"Dunedain", "MID":"Middle men", "MOD":"Men of Darkness", "WM":"Wild men"}

dwarves = {"DWA":"Dwarf"}
elves   = {"NOL":"Noldo", "SIN":"Sinda", "SIL":"Silva"}
hobbits = {"FAL":"Fallohide", "HAR":"Harfoot", "STO":"Stoor"}
men     = {"DUN":"Dunedain", "MID":"Middle men", "MOD":"Men of Darkness", "WM":"Wild men"}

racelist = "RACELIST\n\nDWARVES:\nDWA: Dwarf\n\nELVES:\nNOL: Noldo\nSIN: Sinda\nSIL: Silva\n\nHOBBITS:\nFAL: Fallowhide\nHAR: Harfoot\nSTO: Stoor\n\nMEN:\nDUN: Dunedan\nMID: Middle man\nMOD: Man of Darkness\nWM:  Wild Man"

racattradjs = {
"DWA":{"BRG":0, "NIM":0, "PER":0, "STR":2, "VIT":2, "WIT":0},
"NOL":{"BRG":2, "NIM":2, "PER":1, "STR":0, "VIT":0, "WIT":1},
"SIN":{"BRG":1, "NIM":2, "PER":2, "STR":0, "VIT":1, "WIT":0},
"SIL":{"BRG":1, "NIM":1, "PER":2, "STR":0, "VIT":0, "WIT":0},
"FAL":{"BRG":0, "NIM":1, "PER":1, "STR":-1, "VIT":0, "WIT":0},
"HAR":{"BRG":-1, "NIM":2, "PER":1, "STR":-1, "VIT":0, "WIT":0},
"STO":{"BRG":-1, "NIM":2, "PER":1, "STR":-1, "VIT":0, "WIT":0},
"DUN":{"BRG":1, "NIM":0, "PER":0, "STR":0, "VIT":0, "WIT":1},
"MID":{"BRG":0, "NIM":0, "PER":0, "STR":1, "VIT":1, "WIT":0},
"MOD":{"BRG":0, "NIM":1, "PER":0, "STR":1, "VIT":0, "WIT":-1},
"WM":{"BRG":0, "NIM":0, "PER":1, "STR":1, "VIT":1, "WIT":0}
}

racskills = {
"DWA":["APP", "ARM", "CON", "CRA", "DEB", "GAM", "ING", "INP", "INM", "LAN", "LOR", "OBS", "PER", "PRS", "RAN", "SRC", "SIE", "SMI", "STO", "STE", "SUR", "TEA", "TRA", "WEA"],
"NOL":["ACR", "ARM", "CLI", "CRA", "DEB", "HEA", "ING", "INP", "INM", "JUM", "LAN", "LOR", "MIM", "OBS", "PER", "PRS", "RAN", "RID", "RUN", "SEA", "SRC", "SMI", "STE", "SUR", "SWI", "TRA", "WEA"],
"SIN":["ACR", "ARM", "CLI", "CRA", "DEB", "HEA", "ING", "INP", "INM", "JUM", "LAN", "LOR", "MIM", "OBS", "PER", "PRS", "RAN", "RID", "RUN", "SEA", "SRC", "SMI", "STE", "SUR", "SWI", "TRA", "WEA"],
"SIL":["ACR", "ARM", "CLI", "CRA", "DEB", "HEA", "ING", "INP", "INM", "JUM", "LAN", "LOR", "MIM", "OBS", "PER", "PRS", "RAN", "RID", "RUN", "SEA", "SRC", "SMI", "STE", "SUR", "SWI", "TRA", "WEA"],
"FAL":["ACR", "CLI", "CON", "CRA", "DEB", "GAM", "INQ", "ING", "LAN", "LEG", "LOR", "OBS", "PER", "PRS", "RAN", "SRC", "STE", "SUR", "TRA", "WEA"],
"HAR":["ACR", "CLI", "CON", "CRA", "DEB", "GAM", "INQ", "ING", "LAN", "LEG", "LOR", "OBS", "PER", "PRS", "RAN", "SRC", "STE", "SUR", "TRA", "WEA"],
"STO":["ACR", "CLI", "CON", "CRA", "DEB", "GAM", "INQ", "ING", "LAN", "LEG", "LOR", "OBS", "PER", "PRS", "RAN", "SRC", "STE", "SUR", "TRA", "WEA"],
"DUN":["ARM", "CLI", "CON", "CRA", "DEB", "GAM", "HEA", "INQ", "ING", "INP", "INM", "JUM", "LAN", "LOR", "OBS", "PER", "PRS", "RAN", "RID", "RUN", "SEA", "SRC", "SMI", "STO", "STE", "SUR", "SWI", "TEA", "TRA", "WEA"],
"MID":["ARM", "CLI", "CON", "CRA", "DEB", "GAM", "HEA", "INQ", "ING", "INP", "INM", "JUM", "LAN", "LOR", "OBS", "PER", "PRS", "RAN", "RID", "RUN", "SEA", "SRC", "SMI", "STO", "STE", "SUR", "SWI", "TEA", "TRA", "WEA"],
"MOD":["ARM", "CLI", "CON", "CRA", "DEB", "GAM", "HEA", "INQ", "ING", "INP", "INM", "JUM", "LAN", "LOR", "OBS", "PER", "PRS", "RAN", "RID", "RUN", "SEA", "SRC", "SMI", "STO", "STE", "SUR", "SWI", "TEA", "TRA", "WEA"],
"WM" :["ARM", "CLI", "CON", "CRA", "DEB", "GAM", "HEA", "INQ", "ING", "INP", "INM", "JUM", "LAN", "LOR", "OBS", "PER", "PRS", "RAN", "RID", "RUN", "SEA", "SRC", "SMI", "STO", "STE", "SUR", "SWI", "TEA", "TRA", "WEA"]
}

racskilladjs = {
"DWA":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":-2, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":2, "STE":0, "STO":2, "SUR":2, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"NOL":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":4, "RUN":4, "SEA":0, "SRC":0, "SIE":0, "SMI":2, "STE":4, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"SIN":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":2, "PRS":0, "RAN":0, "RID":4, "RUN":4, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":4, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"SIL":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":4, "RUN":4, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":4, "STO":0, "SUR":2, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"FAL":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":3, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":2, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":4, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"HAR":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":3, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":2, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":4, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"STO":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":3, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":2, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":4, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"DUN":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"MID":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"MOD":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"WM":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":2, "SWI":0, "TEA":0, "TRA":2, "UNA":0,
"WEA":2
}.items()))
}

ractraits = {
"DWA":["ALL", "CRF", "DOU", "FAI", "FEH", "FRI", "HAR", "HOA", "INC", "IND", "RES", "STE", "STW", "SWR", "TIR", "VAR", "WAK", "ARR", "COH", "DUT", "GRA", "PRO", "RIV", "STI"],
"NOL":["ACC", "ALL", "AMB", "CRF", "CUR", "DOD", "ELO", "FTH", "FRI", "GOT", "HOA", "HOT", "INC", "IND", "EAR", "NIT", "QUI", "RES", "STW", "TIR", "TRV", "VAR", "WEM", "WIS", "WOO", "ARR", "COH", "DUT", "PRO", "RIV", "STI"],
"SIN":["ACC", "ALL", "AMB", "CRF", "CUR", "DOD", "ELO", "FTH", "FRI", "GOT", "HOA", "HOT", "INC", "IND", "EAR", "NIT", "QUI", "RES", "STW", "TIR", "TRV", "VAR", "WEM", "WIS", "WOO", "ARR", "COH", "DUT", "PRO", "RIV", "STI"],
"SIL":["ACC", "ALL", "AMB", "CRF", "CUR", "DOD", "ELO", "FTH", "FRI", "GOT", "HOA", "HOT", "INC", "IND", "EAR", "NIT", "QUI", "RES", "STW", "TIR", "TRV", "VAR", "WEM", "WIS", "WOO", "ARR", "COH", "DUT", "PRO", "RIV", "STI"],
"FAL":["ACC", "AMB", "CHL", "CRF", "CUR", "DOD", "ELO", "FAI", "FTH", "FOF", "FRI", "FUR", "HOA", "HOI", "INC", "IND", "EAR", "EYE", "SWR", "VAR", "COH", "DUT", "GRA", "RIV", "STI", "WEK", "WEW"],
"HAR":["ACC", "AMB", "CHL", "CRF", "CUR", "DOD", "ELO", "FAI", "FTH", "FOF", "FRI", "FUR", "HOA", "HOI", "INC", "IND", "EAR", "EYE", "SWR", "VAR", "COH", "DUT", "GRA", "RIV", "STI", "WEK", "WEW"],
"STO":["ACC", "AMB", "CHL", "CRF", "CUR", "DOD", "ELO", "FAI", "FTH", "FOF", "FRI", "FUR", "HOA", "HOI", "INC", "IND", "EAR", "EYE", "SWR", "VAR", "COH", "DUT", "GRA", "RIV", "STI", "WEK", "WEW"],
"DUN":["ACC", "ALL", "AMB", "AOH", "BOL", "CHL", "COM", "CRF", "CUR", "DOD", "DOU", "ELF", "ELO", "FAI", "FTH", "FOF", "FEH", "FOR",  "FRI", "FUR", "GOT", "HAM", "HAR", "HEL", "HOA", "HOT", "HOI", "INC", "IND", "EAR", "EYE", "NOS", "LIO", "NIT", "QUI", "RAN",  "RES", "STE", "STW", "SWR", "TIR", "TRV", "TWO", "VAT", "VAR", "WAK", "WAH", "WAW", "WAR", "WEM", "WIS", "WOO", "ARR", "BAT", "COH", "CRV", "CRI", "DAR", "DUM", "DEA", "DEY", "DUT", "ENE", "FEA", "FEY", "GRA", "HAT", "OAT", "PRO", "REC", "RIV", "SLO", "STI", "WEK", "WEW"],
"MID":["ACC", "ALL", "AMB", "AOH", "BOL", "CHL", "COM", "CRF", "CUR", "DOD", "DOU", "ELF", "ELO", "FAI", "FTH", "FOF", "FEH", "FOR",  "FRI", "FUR", "GOT", "HAM", "HAR", "HEL", "HOA", "HOT", "HOI", "INC", "IND", "EAR", "EYE", "NOS", "LIO", "NIT", "QUI", "RAN",  "RES", "STE", "STW", "SWR", "TIR", "TRV", "TWO", "VAT", "VAR", "WAK", "WAH", "WAW", "WAR", "WEM", "WIS", "WOO", "ARR", "BAT", "COH", "CRV", "CRI", "DAR", "DUM", "DEA", "DEY", "DUT", "ENE", "FEA", "FEY", "GRA", "HAT", "OAT", "PRO", "REC", "RIV", "SLO", "STI", "WEK", "WEW"],
"MOD":["ACC", "ALL", "AMB", "AOH", "BOL", "CHL", "COM", "CRF", "CUR", "DOD", "DOU", "ELF", "ELO", "FAI", "FTH", "FOF", "FEH", "FOR",  "FRI", "FUR", "GOT", "HAM", "HAR", "HEL", "HOA", "HOT", "HOI", "INC", "IND", "EAR", "EYE", "NOS", "LIO", "NIT", "QUI", "RAN",  "RES", "STE", "STW", "SWR", "TIR", "TRV", "TWO", "VAT", "VAR", "WAK", "WAH", "WAW", "WAR", "WEM", "WIS", "WOO", "ARR", "BAT", "COH", "CRV", "CRI", "DAR", "DUM", "DEA", "DEY", "DUT", "ENE", "FEA", "FEY", "GRA", "HAT", "OAT", "PRO", "REC", "RIV", "SLO", "STI", "WEK", "WEW"],
"WM":["ACC", "ALL", "AMB", "AOH", "BOL", "CHL", "COM", "CRF", "CUR", "DOD", "DOU", "ELF", "ELO", "FAI", "FTH", "FOF", "FEH", "FOR",  "FRI", "FUR", "GOT", "HAM", "HAR", "HEL", "HOA", "HOT", "HOI", "INC", "IND", "EAR", "EYE", "NOS", "LIO", "NIT", "QUI", "RAN",  "RES", "STE", "STW", "SWR", "TIR", "TRV", "TWO", "VAT", "VAR", "WAK", "WAH", "WAW", "WAR", "WEM", "WIS", "WOO", "ARR", "BAT", "COH", "CRV", "CRI", "DAR", "DUM", "DEA", "DEY", "DUT", "ENE", "FEA", "FEY", "GRA", "HAT", "OAT", "PRO", "REC", "RIV", "SLO", "STI", "WEK", "WEW"]
}

#ORDERS
orders = {"BAR":"Barbarian", "CRA":"Craftsman", "LOR":"Loremaster", "MAG":"Magician", "MAR":"Mariner", "MIN":"Minstrel", "NOB":"Noble", "ROG":"Rogue", "WAR":"Warrior", "ARC":"Archer", "CAP":"Captain", "KNI":"Knight", "RAN":"Ranger", "SPY":"Spy", "WIZ":"Wizard"}

orderskills = {"BAR":[
"ARM", "CLI", "CRA", "JUM", "MIM", "OBS", "RAN", "RID", "RUN", "STE", "SUR", "SWI", "TRA", "WEA"
],

"CRA":[
"APP", "CON", "CRA", "DEB", "GAM", "LAN", "LOR", "OBS", "PER", "PRS", "SMI", "STO"
],

"LOR":[
"APP", "CRA", "DEB", "GAM", "HEA", "INQ", "ING", "LAN", "LOR", "OBS", "PRS", "WEA"
],

"MAG":[
"APP", "CRA", "DEB", "HEA", "INQ", "ING", "INP", "INM", "LAN", "LOR", "OBS", "PRS", "RID", "SRC", "WEA"
],

"MAR":[
"ACR", "ARM", "CLI", "JUM", "OBS", "RAN", "RUN", "SEA", "SWI", "WEA"
],

"MIN":[
"ACR", "CLI", "CRA", "DEB", "GAM", "INQ", "INP", "LAN", "LEG", "LOR", "MIM", "OBS", "PRS", "RUN", "STE"
],

"NOB":[
"ARM", "CRA", "DEB", "INQ", "LAN", "LOR", "OBS", "PRS", "RAN", "RID"
],

"ROG":[
"ACR", "APP", "ARM", "CLI", "CON", "CRA", "GAM", "GUI", "JUM", "LEG", "OBS", "PRS", "RAN", "RUN", "SRC", "STE", "SUR"
],

"WAR":[
"ARM", "CLI", "HEA", "INP", "INM", "JUM", "OBS", "RAN", "RID", "RUN", "SIE", "STE", "SUR", "TRA"
]}

#SKILLS
skilltemp = collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items()))

skillnames = collections.OrderedDict(sorted({
"ACR":"Acrobatics", "APP":"Appraise", "ARM":"Armed Combat", "CLI":"Climb", "CON":"Conceal", "CRA":"Craft", "DEB":"Debate", "GAM":"Games", "GUI":"Guise", "HEA":"Healing", "INQ":"Inquire", "ING":"Insight", "INP":"Inspire", "INM":"Intimidate", "JUM":"Jump", "LAN":"Language", "LEG":"Legerdemain", "LOR":"Lore",
"MIM":"Mimicry", "OBS":"Observe", "PER":"Perform", "PRS":"Persuade", "RAN":"Ranged Combat", "RID":"Ride", "RUN":"Run", "SEA":"Sea-craft", "SRC":"Search", "SIE":"Siege-craft", "SMI":"Smithcraft", "STE":"Stealth", "STO":"Stonecraft", "SUR":"Survival", "SWI":"Swim", "TEA":"Teamster", "TRA":"Track", "UNA":"Unarmed Combat",
"WEA":"Weather-sense"
}.items()))

skillattrs = collections.OrderedDict(sorted({
"ACR":"NIM", "APP":"WIT", "ARM":"NIM", "CLI":"STR", "CON":"WIT", "CRA":"NIM", "DEB":"WIT", "GAM":"NIM", "GUI":"WIT", "HEA":"WIT", "INQ":"BRG", "ING":"PER", "INP":"BRG", "INM":"BRG", "JUM":"STR", "LAN":"WIT", "LEG":"NIM", "LOR":"WIT",
"MIM":"BRG", "OBS":"PER", "PER":"BRG", "PRS":"WIT", "RAN":"NIM", "RID":"BRG", "RUN":"STR", "SEA":"WIT", "SRC":"PER", "SIE":"WIT", "SMI":"STR", "STE":"NIM", "STO":"STR", "SUR":"PER", "SWI":"STR", "TEA":"STR", "TRA":"WIT", "UNA":"NIM",
"WEA":"PER"
}.items()))

#TRAITS
traitstemp = collections.OrderedDict(sorted({
"ACC":0, "ALL":0, "AMB":0, "AOH":0, "BOL":0, "CHL":0, "COM":0, "CRF":0, "CUR":0, "DOD":0, "DOU":0, "ELF":0, "ELO":0, "FAI":0, "FTH":0, "FOF":0, "FEH":0, "FOR":0,
"FRI":0, "FUR":0, "GOT":0, "HAM":0, "HAR":0, "HEL":0, "HOA":0, "HOT":0, "HOI":0, "INC":0, "IND":0, "EAR":0, "EYE":0, "NOS":0, "LIO":0, "NIT":0, "QUI":0, "RAN":0,
"RES":0, "STE":0, "STW":0, "SWR":0, "TIR":0, "TRV":0, "TWO":0, "VAT":0, "VAR":0, "WAK":0, "WAH":0, "WAW":0, "WAR":0, "WEM":0, "WIS":0, "WOO":0, "ARR":0, "BAT":0,
"COH":0, "CRV":0, "CRI":0, "DAR":0, "DUM":0, "DEA":0, "DEY":0, "DUT":0, "ENE":0, "FEA":0, "FEY":0, "GRA":0, "HAT":0, "OAT":0, "PRO":0, "REC":0, "RIV":0, "SLO":0,
"STI":0, "WEK":0, "WEW":0
}.items()))

edges = [
"ACC", "ALL", "AMB", "AOH", "BOL", "CHL", "COM", "CRF", "CUR", "DOD", "DOU", "ELF", "ELO", "FAI", "FTH", "FOF", "FEH", "FOR",
"FRI", "FUR", "GOT", "HAM", "HAR", "HEL", "HOA", "HOT", "HOI", "INC", "IND", "EAR", "EYE", "NOS", "LIO", "NIT", "QUI", "RAN",
"RES", "STE", "STW", "SWR", "TIR", "TRV", "TWO", "VAT", "VAR", "WAK", "WAH", "WAW", "WAR", "WEM", "WIS", "WOO"
]

traitnames = collections.OrderedDict(sorted({
"ACC":"Accurate", "ALL":"Ally", "AMB":"Ambidextrous", "AOH":"Armour of Heroes", "BOL":"Bold", "CHL":"Charmed Life", "COM":"Command", "CRF":"Craftmaster", "CUR":"Curious", "DOD":"Dodge", "DOU":"Doughty", "ELF":"Elf-friend", "ELO":"Eloquent", "FAI":"Fair", "FTH":"Faithful", "FOF":"Favour of Fortune", "FEH":"Fell-handed", "FOR":"Foresighted",
"FRI":"Friends", "FUR":"Furtive", "GOT":"Gift of Tongues", "HAM":"Hammerhand", "HAR":"Hardy", "HEL":"Healing Hands", "HOA":"Hoard", "HOT":"Honey-Tongued", "HOI":"Honour's Insight", "INC":"Incorruptible", "IND":"Indomitable", "EAR":"Keen-eared", "EYE":"Keen-eyed", "NOS":"Keen-nosed", "LIO":"Lion-hearted", "NIT":"Night-eyed", "QUI":"Quick-draw", "RAN":"Rank",
"RES":"Resolute", "STE":"Stern", "STW":"Strong-willed", "SWR":"Swift Recovery", "TIR":"Tireless", "TRV":"Travel-sense", "TWO":"Two-handed Fighting", "VAT":"Valiant", "VAR":"Valour", "WAK":"Wakefulness", "WAH":"Warrior's Heart", "WAW":"Warwise", "WAR":"Wary", "WEM":"Weapon Mastery", "WIS":"WISE", "WOO":"Woodcrafty", "ARR":"Arrogant", "BAT":"Battle-Fury",
"COH":"Code of Honour", "CRV":"Craven", "CRI":"Crippling Wound", "DAR":"Dark Secret", "DUM":"Dullard", "DEA":"Dull-eared", "DEY":"Dull-eyed", "DUT":"Duty", "ENE":"Enemy", "FEA":"Fealty", "FEY":"Fey", "GRA":"Grasping", "HAT":"Hatred", "OAT":"Oath", "PRO":"Proud", "REC":"Reckless", "RIV":"Rival", "SLO":"Slow Recovery",
"STI":"Stiff-necked", "WEK":"Weak", "WEW":"Weak-willed"
}.items()))

traitmaxes = collections.OrderedDict(sorted({
"ACC":1, "ALL":1, "AMB":1, "AOH":1, "BOL":1, "CHL":1, "COM":4, "CRF":1, "CUR":1, "DOD":1, "DOU":1, "ELF":1, "ELO":1, "FAI":1, "FTH":10, "FOF":10, "FEH":5, "FOR":1,
"FRI":2, "FUR":1, "GOT":1, "HAM":1, "HAR":1, "HEL":1, "HOA":4, "HOT":4, "HOI":4, "INC":2, "IND":2, "EAR":1, "EYE":1, "NOS":4, "LIO":1, "NIT":2, "QUI":2, "RAN":4,
"RES":4, "STE":4, "STW":4, "SWR":1, "TIR":2, "TRV":1, "TWO":1, "VAT":1, "VAR":2, "WAK":1, "WAH":2, "WAW":3, "WAR":1, "WEM":1, "WIS":4, "WOO":4, "ARR":1, "BAT":3,
"COH":1, "CRV":1, "CRI":1, "DAR":1, "DUM":1, "DEA":1, "DEY":1, "DUT":1, "ENE":1, "FEA":1, "FEY":1, "GRA":1, "HAT":1, "OAT":1, "PRO":1, "REC":1, "RIV":1, "SLO":1,
"STI":1, "WEK":1, "WEW":1
}.items()))

traitskilladjs = collections.OrderedDict(sorted({
"ACC":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":4, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"ALL":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"AMB":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"AOH":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"BOL":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"CHL":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"COM":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"CRF":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":2, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":2, "STE":0, "STO":2, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"CUR":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"DOD":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"DOU":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"ELF":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"ELO":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":2, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":2, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"FAI":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":4, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":4, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"FTH":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"FOF":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"FEH":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"FOR":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"FRI":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"FUR":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":1, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":1, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":1, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"GOT":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":3, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"HAM":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"HAR":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"HEL":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":5, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"HOA":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"HOT":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":2, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":2, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"HOI":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":2, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"INC":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"IND":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"EAR":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":2, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"EYE":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":2, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"NOS":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":2, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":2, "UNA":0,
"WEA":0
}.items())),

"LIO":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"NIT":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"QUI":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"RAN":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"RES":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"STE":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":2, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":2, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"STW":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"SWR":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"TIR":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"TRV":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"TWO":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"VAT":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"VAR":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"WAK":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"WAH":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"WAW":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":1, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":1, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":1, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":1,
"WEA":0
}.items())),

"WAR":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"WEM":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":3, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"WIS":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":1,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"WOO":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":1, "STO":0, "SUR":1, "SWI":0, "TEA":0, "TRA":1, "UNA":0,
"WEA":1
}.items())),

"ARR":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"BAT":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"COH":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"CRV":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"CRI":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"DAR":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"DUM":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"DEA":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":-2, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"DEY":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":-2, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"DUT":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"ENE":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"FEA":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"FEY":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"GRA":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"HAT":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"OAT":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"PRO":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"REC":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"RIV":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"SLO":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"STI":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"WEK":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"WEW":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items()))
}.items()))

#READY-MADE BACKGROUNDS
dwbacks = {"N":"None", "DBC":"Dwarf of Balin's Colony", "DBM":"Dwarf of the Blue Mountains", "DIH":"Dwarf of the Iron Hills", "WD":"Wandering Dwarf"}

nobacks = {"N":"None", "ELN":"Elf of Lorien (Noldo)", "ERN":"Elf of Rivendell (Noldo)", "EWC":"Elf of the Wandering Companies (Noldo)"}
snbacks = {"N":"None", "EHS":"ELf of the Grey Havens(Sinda)", "EMS":"Elf of Mirkwood (Sinda)", "ERS":"Elf of Rivendell (Sinda)"}
slbacks = {"N":"None", "ELV":"Elf of Lorien (Silva)", "EMV":"ELf of Mirkwood (Silva)"}

habacks = {"N":"None", "COT":"Cotton (Harfoot)", "PRO":"Proudfoot (Harfoot)"}
fabacks = {"N":"None", "BAG":"Baggins (Fallohide)", "BOL":"Bolger (Fallohide)", "BRA":"Brandybuck (Fallohide)", "TOO":"Took (Fallohide)"}

mibacks = {"N":"None", "BEO":"Beorning (Middle Man)", "DUL":"Dunlending (Middle Man)", "MOB":"Man of Bree (Middle Man)", "MOE":"Man of Dale (Middle Man)", "MOG":"Man of Gondor (Middle Man)", "ROR":"Rider of Rohan (Middle Man)"}
mdbacks = {"N":"None", "EAS":"Easterling (Man of Darkness)", "SOU":"Southron Tribesman (Man of Darkness)"}
dubacks = {"N":"None", "MOM":"Man of Minas Tirith (Dunadan)"}

backs = {"DWA":dwbacks, "NOL":nobacks, "SIN":snbacks, "SIL":slbacks, "FAL":fabacks, "HAR":habacks, "STO":habacks, "DUN":dubacks, "MID":mibacks, "MOD":mdbacks, "WM":mdbacks}

bgskilladjs = {
"N":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"DBC":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":1, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":2,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":2, "SUR":1, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"DBM":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":1, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":2, "STE":0, "STO":2, "SUR":1, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"DIH":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":1, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":1, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":2, "STE":0, "STO":2, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"WD":collections.OrderedDict(sorted({
"ACR":0, "APP":1, "ARM":2, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":2, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":1, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"ELN":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":1, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":1, "LEG":0, "LOR":2,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":1, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":1, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"ERN":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":1, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":2, "LEG":0, "LOR":2,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":1, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"EWC":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":1, "LEG":0, "LOR":2,
"MIM":0, "OBS":0, "PER":1, "PRS":0, "RAN":1, "RID":0, "RUN":1, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"EHS":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":1, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":1,
"MIM":0, "OBS":0, "PER":1, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":2, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":1, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"EMS":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":1, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":1,
"MIM":0, "OBS":0, "PER":1, "PRS":0, "RAN":1, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":1, "STO":0, "SUR":1, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"ERS":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":2,
"MIM":0, "OBS":0, "PER":2, "PRS":0, "RAN":1, "RID":1, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"ELV":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":1, "CLI":1, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":1,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":2, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":1, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"EMV":collections.OrderedDict(sorted(
{"ACR":0, "APP":0, "ARM":1, "CLI":1, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":1, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":1, "STO":0, "SUR":1, "SWI":0, "TEA":0, "TRA":1, "UNA":0,
"WEA":0
}.items())),

"BAG":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":1, "DEB":0, "GAM":1, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":1, "PER":0, "PRS":1, "RAN":1, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"BOL":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":1, "DEB":1, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":1, "PER":0, "PRS":1, "RAN":1, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"BRA":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":1, "DEB":0, "GAM":1, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":1, "PER":0, "PRS":1, "RAN":1, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":1, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"TOO":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":1, "DEB":1, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":1, "PER":0, "PRS":1, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":1, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"COT":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":2, "DEB":1, "GAM":1, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":1, "PER":0, "PRS":0, "RAN":1, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"PRO":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":1, "DEB":1, "GAM":1, "GUI":0, "HEA":0, "INQ":1, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":1, "PER":0, "PRS":0, "RAN":1, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"BEO":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":2, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":1, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":1, "SWI":0, "TEA":0, "TRA":1, "UNA":0,
"WEA":0
}.items())),

"DUL":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":1, "CLI":1, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":1, "RID":1, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":2, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"MOB":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":2, "DEB":1, "GAM":1, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":1, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"MOE":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":1, "CLI":0, "CON":0, "CRA":1, "DEB":1, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":1, "RID":1, "RUN":1, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"MOG":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":1, "CLI":0, "CON":0, "CRA":1, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":1,
"MIM":0, "OBS":1, "PER":0, "PRS":0, "RAN":1, "RID":0, "RUN":1, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"ROR":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":1, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":1, "RID":2, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"EAS":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":2, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":2, "RID":1, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":1, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"SOU":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":1, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":1, "RID":1, "RUN":1, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":1, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"MOM":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":1, "CLI":1, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":1,
"MIM":0, "OBS":0, "PER":0, "PRS":1, "RAN":1, "RID":0, "RUN":1, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items()))
}

#ORDER PACKAGES
barpacks = {"N":"None", "BBAR":"Basic Barbarian", "DRU":"Druadan Tribesman", "SON":"Southron Nomad", "LOS":"Losson Tribesman", "MOU":"Mountain Folk"}
crapacks = {"N":"None", "BCRA":"Basic Craftsman", "GAR":"Gardener", "INN":"Innkeeper", "SMI":"Smith", "MAS":"Stonemason"}
lorpacks = {"N":"None", "BLOR":"Basic Loremaster", "ERI":"Eriadorian Sage", "GOS":"Gondorian Scholar", "MTH":"Minas Tirith Healer", "RIS":"Rivendell Scholar", "WIW":"Wise Woman"}
magpacks = {"N":"None", "BMAG":"Basic Magician", "WIA":"Wizards Apprentice", "SSA":"Student of the Secret Arts", "TRM":"Travelling Magician", "TIM":"Tribal Magician"}
marpacks = {"N":"None", "BMAR":"Basic Mariner", "FIS":"Fisherman", "NAV":"Navy", "RIV":"Riverman", "SHI":"Shipwright"}
minpacks = {"N":"None", "BMIN":"Basic Minstrel", "GOM":"Gondorian Minstrel", "PER":"Performer", "ROB":"Rohirric Bard", "TRC":"Tribal Chanter"}
nobpacks = {"N":"None", "BNOB":"Basic Noble", "GOL":"Gondorian Lord", "ERG":"Eriadorian Gentry", "LOF":"Leader of Folk", "CHF":"Tribal Chieftain"}
rogpacks = {"N":"None", "BROG":"Basic Rogue", "BUR":"Burglar", "OUT":"Outlaw", "LUR":"Lurker", "PIC":"Pickpocket"}
warpacks = {"N":"None", "BWAR":"Basic Warrior", "BOW":"Bowman", "HOR":"Horseman", "SCO":"Scout", "SEN":"Sentinel", "SHR":"Shirriff"}

packs = {"BAR":barpacks, "CRA":crapacks, "LOR":lorpacks, "MAG":magpacks, "MAR":marpacks, "MIN":minpacks, "NOB":nobpacks, "ROG":rogpacks, "WAR":warpacks}

packskilladjs = {
"N":skilltemp,

"BBAR":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":2, "CLI":1, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":2, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":1, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":3, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":3, "UNA":0,
"WEA":0
}.items())),

"DRU":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":1, "CLI":1, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":1, "PER":0, "PRS":0, "RAN":2, "RID":0, "RUN":1, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":3, "STO":0, "SUR":3, "SWI":0, "TEA":0, "TRA":3, "UNA":0,
"WEA":0
}.items())),

"SON":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":2, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":2, "PER":0, "PRS":0, "RAN":2, "RID":0, "RUN":2, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":2, "STO":0, "SUR":3, "SWI":0, "TEA":0, "TRA":2, "UNA":0,
"WEA":0
}.items())),

"LOS":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":2, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":2, "PER":0, "PRS":0, "RAN":2, "RID":0, "RUN":2, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":2, "STO":0, "SUR":3, "SWI":0, "TEA":0, "TRA":2, "UNA":0,
"WEA":0
}.items())),

"MOU":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":2, "CLI":3, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":2, "PER":0, "PRS":0, "RAN":1, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":2, "STO":0, "SUR":3, "SWI":0, "TEA":0, "TRA":2, "UNA":0,
"WEA":0
}.items())),

"BCRA":collections.OrderedDict(sorted({
"ACR":0, "APP":3, "ARM":0, "CLI":0, "CON":0, "CRA":4, "DEB":2, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":2, "PER":0, "PRS":2, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":1, "STE":0, "STO":1, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"GAR":collections.OrderedDict(sorted({
"ACR":0, "APP":1, "ARM":0, "CLI":0, "CON":0, "CRA":5, "DEB":0, "GAM":2, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":3,
"MIM":0, "OBS":2, "PER":0, "PRS":2, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"INN":collections.OrderedDict(sorted({
"ACR":0, "APP":2, "ARM":0, "CLI":0, "CON":0, "CRA":6, "DEB":2, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":2,
"MIM":0, "OBS":1, "PER":0, "PRS":2, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"SMI":collections.OrderedDict(sorted({
"ACR":0, "APP":3, "ARM":0, "CLI":0, "CON":0, "CRA":2, "DEB":2, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":2, "PER":0, "PRS":2, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":3, "STE":0, "STO":1, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"MAS":collections.OrderedDict(sorted({
"ACR":0, "APP":3, "ARM":0, "CLI":0, "CON":0, "CRA":2, "DEB":2, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":2, "PER":2, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":1, "STE":0, "STO":3, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"BLOR":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":3, "GAM":0, "GUI":0, "HEA":1, "INQ":0, "ING":1, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":6,
"MIM":0, "OBS":2, "PER":1, "PRS":1, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"ERI":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":2, "DEB":2, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":2, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":3,
"MIM":0, "OBS":2, "PER":1, "PRS":1, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"GOS":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":2, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":3, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":6,
"MIM":0, "OBS":1, "PER":1, "PRS":2, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"MTH":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":3, "INQ":0, "ING":1, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":8,
"MIM":0, "OBS":2, "PER":0, "PRS":1, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"RIS":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":1, "GAM":0, "GUI":0, "HEA":1, "INQ":0, "ING":1, "INP":0, "INM":0, "JUM":0, "LAN":2, "LEG":0, "LOR":6,
"MIM":0, "OBS":2, "PER":1, "PRS":1, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"WIW":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":2, "GAM":0, "GUI":0, "HEA":1, "INQ":0, "ING":1, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":6,
"MIM":0, "OBS":2, "PER":0, "PRS":1, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":2
}.items())),

"BMAG":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":1, "INQ":0, "ING":1, "INP":0, "INM":2, "JUM":0, "LAN":3, "LEG":0, "LOR":5,
"MIM":0, "OBS":2, "PER":1, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"WIA":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":1, "GAM":0, "GUI":0, "HEA":0, "INQ":1, "ING":1, "INP":1, "INM":2, "JUM":0, "LAN":2, "LEG":0, "LOR":4,
"MIM":0, "OBS":1, "PER":0, "PRS":1, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"SSA":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":2, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":2, "JUM":0, "LAN":3, "LEG":0, "LOR":5,
"MIM":0, "OBS":1, "PER":0, "PRS":2, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"TRM":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":1, "INQ":0, "ING":1, "INP":0, "INM":1, "JUM":0, "LAN":3, "LEG":0, "LOR":5,
"MIM":0, "OBS":2, "PER":0, "PRS":2, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"TIM":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":1, "INQ":0, "ING":1, "INP":0, "INM":2, "JUM":0, "LAN":1, "LEG":0, "LOR":5,
"MIM":0, "OBS":2, "PER":0, "PRS":2, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":1
}.items())),

"BMAR":collections.OrderedDict(sorted({
"ACR":1, "APP":0, "ARM":2, "CLI":2, "CON":0, "CRA":1, "DEB":0, "GAM":1, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":1, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":3, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":3, "TEA":0, "TRA":0, "UNA":0,
"WEA":1
}.items())),

"FIS":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":1, "CLI":1, "CON":0, "CRA":3, "DEB":0, "GAM":1, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":1, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":1, "SEA":3, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":3, "TEA":0, "TRA":0, "UNA":0,
"WEA":1
}.items())),

"NAV":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":2, "CLI":2, "CON":0, "CRA":1, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":1, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":2, "RID":0, "RUN":1, "SEA":3, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":2, "TEA":0, "TRA":0, "UNA":0,
"WEA":1
}.items())),

"RIV":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":2, "CLI":1, "CON":0, "CRA":2, "DEB":0, "GAM":1, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":1, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":2, "RID":0, "RUN":0, "SEA":3, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":3, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"SHI":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":1, "CLI":2, "CON":0, "CRA":2, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":1, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":0, "PER":0, "PRS":0, "RAN":1, "RID":0, "RUN":1, "SEA":3, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":3, "TEA":0, "TRA":0, "UNA":0,
"WEA":1
}.items())),

"BMIN":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":1, "DEB":1, "GAM":1, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":1, "INM":0, "JUM":0, "LAN":3, "LEG":0, "LOR":1,
"MIM":1, "OBS":0, "PER":3, "PRS":2, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":1, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"GOM":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":1, "GAM":1, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":2, "INM":0, "JUM":0, "LAN":0, "LEG":1, "LOR":2,
"MIM":2, "OBS":0, "PER":3, "PRS":2, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":1, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"PER":collections.OrderedDict(sorted({
"ACR":2, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":2, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":3, "LOR":0,
"MIM":1, "OBS":0, "PER":3, "PRS":2, "RAN":1, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":1, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"ROB":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":1, "GAM":1, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":3, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":3,
"MIM":1, "OBS":0, "PER":3, "PRS":2, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":1, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"TRC":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":1, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":2, "INM":0, "JUM":0, "LAN":0, "LEG":1, "LOR":3,
"MIM":1, "OBS":0, "PER":3, "PRS":2, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":2, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"BNOB":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":2, "CLI":0, "CON":0, "CRA":0, "DEB":2, "GAM":0, "GUI":0, "HEA":0, "INQ":1, "ING":0, "INP":2, "INM":2, "JUM":0, "LAN":0, "LEG":0, "LOR":1,
"MIM":0, "OBS":2, "PER":0, "PRS":1, "RAN":0, "RID":2, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"GOL":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":3, "CLI":0, "CON":0, "CRA":0, "DEB":2, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":2, "INM":2, "JUM":0, "LAN":1, "LEG":0, "LOR":1,
"MIM":0, "OBS":1, "PER":0, "PRS":1, "RAN":0, "RID":2, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"ERG":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":0, "CLI":0, "CON":0, "CRA":0, "DEB":2, "GAM":0, "GUI":0, "HEA":0, "INQ":1, "ING":0, "INP":2, "INM":1, "JUM":0, "LAN":2, "LEG":0, "LOR":2,
"MIM":0, "OBS":2, "PER":0, "PRS":3, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"LOF":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":3, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":2, "INM":2, "JUM":0, "LAN":0, "LEG":0, "LOR":1,
"MIM":0, "OBS":2, "PER":0, "PRS":1, "RAN":2, "RID":2, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"CHF":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":2, "CLI":0, "CON":0, "CRA":0, "DEB":2, "GAM":0, "GUI":0, "HEA":0, "INQ":1, "ING":0, "INP":2, "INM":2, "JUM":0, "LAN":0, "LEG":0, "LOR":1,
"MIM":0, "OBS":2, "PER":1, "PRS":0, "RAN":0, "RID":2, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"BROG":collections.OrderedDict(sorted({
"ACR":0, "APP":1, "ARM":2, "CLI":2, "CON":2, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":1, "ING":0, "INP":0, "INM":0, "JUM":2, "LAN":0, "LEG":1, "LOR":0,
"MIM":0, "OBS":1, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":3, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"BUR":collections.OrderedDict(sorted({
"ACR":1, "APP":3, "ARM":1, "CLI":3, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":1, "LAN":0, "LEG":1, "LOR":0,
"MIM":0, "OBS":1, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":1, "SIE":0, "SMI":0, "STE":3, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"OUT":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":3, "CLI":2, "CON":2, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":2, "PER":0, "PRS":0, "RAN":2, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":3, "STO":0, "SUR":1, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"LUR":collections.OrderedDict(sorted({
"ACR":0, "APP":1, "ARM":0, "CLI":0, "CON":2, "CRA":0, "DEB":0, "GAM":0, "GUI":2, "HEA":0, "INQ":2, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":1, "LOR":0,
"MIM":0, "OBS":3, "PER":1, "PRS":0, "RAN":0, "RID":0, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":3, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"PIC":collections.OrderedDict(sorted({
"ACR":0, "APP":2, "ARM":1, "CLI":0, "CON":2, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":1, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":3, "LOR":0,
"MIM":0, "OBS":2, "PER":0, "PRS":0, "RAN":0, "RID":0, "RUN":1, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":3, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"BWAR":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":3, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":1, "INQ":0, "ING":0, "INP":1, "INM":1, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":2, "PER":0, "PRS":0, "RAN":3, "RID":2, "RUN":0, "SEA":0, "SRC":0, "SIE":2, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"BOW":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":1, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":1, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":1, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":3, "PER":0, "PRS":0, "RAN":3, "RID":2, "RUN":1, "SEA":0, "SRC":0, "SIE":1, "SMI":0, "STE":0, "STO":0, "SUR":1, "SWI":0, "TEA":0, "TRA":1, "UNA":0,
"WEA":0
}.items())),

"HOR":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":3, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":1, "INQ":0, "ING":0, "INP":2, "INM":2, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":2, "PER":0, "PRS":0, "RAN":1, "RID":3, "RUN":0, "SEA":0, "SRC":0, "SIE":1, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"SCO":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":2, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":1, "INQ":0, "ING":0, "INP":0, "INM":0, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":3, "PER":0, "PRS":0, "RAN":2, "RID":2, "RUN":0, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":3, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":2, "UNA":0,
"WEA":0
}.items())),

"SEN":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":3, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":2, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":3, "PER":0, "PRS":0, "RAN":2, "RID":1, "RUN":1, "SEA":0, "SRC":0, "SIE":3, "SMI":0, "STE":0, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items())),

"SHR":collections.OrderedDict(sorted({
"ACR":0, "APP":0, "ARM":2, "CLI":0, "CON":0, "CRA":0, "DEB":0, "GAM":0, "GUI":0, "HEA":0, "INQ":0, "ING":0, "INP":0, "INM":1, "JUM":0, "LAN":0, "LEG":0, "LOR":0,
"MIM":0, "OBS":3, "PER":0, "PRS":0, "RAN":3, "RID":0, "RUN":3, "SEA":0, "SRC":0, "SIE":0, "SMI":0, "STE":3, "STO":0, "SUR":0, "SWI":0, "TEA":0, "TRA":0, "UNA":0,
"WEA":0
}.items()))
}


#Package Traits

bartraits = {"BBAR":["DOU", "HAR", "TIR", "WAR", "WOO"], "DRU":["ACC", "DOD", "NIT", "WAR", "WOO"], "SON":["HAR", "EYE", "TRV", "TIR", "WOO"], "LOS":["ACC", "HAR", "TRV", "WAK", "WOO"], "MOU":["DOU", "FEH", "SWR", "WOO"]}
cratraits = {"BCRA":["AMB", "CRF", "FOF", "FRI", "HOA"], "GAR":["CHL", "CRF", "FOF", "FRI", "WIS"], "INN":["CRF", "FRI", "HOA", "HOT", "WAK"], "SMI":["CRF", "DOU", "HAR", "FRI", "HOA"], "MAS":["CRF", "DOU", "HAR", "FRI", "HOA"]}
lortraits = {"BLOR":["CUR", "GOT", "HEL", "HOI", "WIS"], "ERI":["CUR", "ELF", "FRI", "HEL", "WIS"], "GOS":["HOA", "HOT", "RAN", "STE", "WIS"], "MTH":["FRI", "GOT", "HEL", "RES", "WIS"], "RIS":["CUR", "ELF", "GOT", "HEL", "WIS"], "WIW":["ALL", "ELO", "HAR", "HOT", "WIS"]}
magtraits = {"BMAG":["AOH", "CHL", "CUR", "STW", "WIS"], "WIA":["CUR", "STW", "VAT", "VAR", "WIS"], "SSA":["ALL", "CUR", "HOT", "RAN", "STW"], "TRM":["AOH", "CHL", "CUR", "FRI", "WIS"], "TIM":["CUR", "FRI", "HAR", "WIS", "WOO"]}
martraits = {"BMAR":["AMB", "DOU", "HAR", "EYE", "TRV"], "FIS":["CRF", "DOU", "HAR", "EYE", "TRV"], "NAV":["ALL", "COM", "RAN", "STE", "WAW"], "RIV":["DOU", "HAR", "EYE", "TIR", "WOO"], "SHI":["CRF", "DOD", "ELF", "FRI", "EYE"]}
mintraits = {"BMIN":["FOF", "FRI", "GOT", "HOT", "EYE"], "GOM":["CUR", "DOD", "FRI", "HOT", "EYE"], "PER":["CHL", "FOF", "FRI", "HOT", "EYE"], "ROB":["ALL", "FRI", "HAR", "HOT", "EYE"], "TRC":["ALL", "FRI", "HAR", "HOT", "EYE"]}
nobtraits = {"BNOB":["COM", "HEL", "HOA", "RAN", "STE"], "GOL":["COM", "HEL", "HOA", "RAN", "STE"], "ERG":["CHL", "FRI", "HOA", "HOT", "RAN"], "LOF":["AOH", "COM", "RAN", "HOA", "STE"], "CHF":["ALL", "COM", "HOA", "RAN", "WOO"]}
rogtraits = {"BROG":["DOD", "FRI", "FUR", "NIT", "WAR"], "BUR":["AMB", "DOD", "FUR", "EYE", "WAR"], "OUT":["DOD", "FRI", "HAR", "STW", "TIR"], "LUR":["DOD", "FRI", "FUR", "HOT", "WAR"], "PIC":["AMB", "DOD", "FRI", "FUR", "WAR"]}
wartraits = {"BWAR":["BOL", "COM", "VAT", "WAH", "WAW"], "BOW":["ACC", "AOH", "QUI", "VAT", "WAW"], "HOR":["BOL", "FEH", "HOI", "WAH", "WAW"], "SCO":["COM", "RES", "WAH", "WAW", "WOO"], "SEN":["EAR", "EYE", "NIT", "WAK", "WAR"], "SHR":["ACC", "DOD", "FRI", "EAR", "EYE"]}

ordertraits = {"BAR":bartraits, "CRA":cratraits, "LOR":lortraits, "MAG":magtraits, "MAR":martraits, "MIN":mintraits, "NOB":nobtraits, "ROG":rogtraits, "WAR":wartraits}

#Order Abilities

barabils = ["Brew Poison", "Champion", "Hard March", "Marking-Signs", "Preferred Weapon", "Walk Without Trace"]
craabils = ["Enchantment", "Masterwork", "Place Of Trade", "Preservation", "Refuge", "Speedy Work"]
lorabils = ["Ancient Scripts", "Expertise", "Scroll Hoard", "Secretive", "Spellcasting", "Vala Virtue"]
magabils = ["Spellcasting", "Dwimmer-Crafty", "Sanctum", "Sanctum Power", "Spellcasting Method", "Spell Specialty", "Wizard's Heart"]
marabils = ["Diver", "Rope-craft", "Sailor's Eye", "Sea Legs", "Ship", "Wind-mastery"]
minabils = ["Gladden", "Inspiring Performance", "Jugglery", "Natural Talent", "Voice of Power", "Woven Words"]
nobabils = ["Courtier", "Cross-Order Skill", "Deference", "Domain", "Noble Mien"]
rogabils = ["Fleet-Footed", "Lockpicking", "Lurking in Shadows", "Sanctuary"]
warabils = ["Battle-Hardened", "Evasion", "Favoured Weapon", "Swift Strike", "Warrior-born"]

orderabils = {"BAR":barabils, "CRA":craabils, "LOR":lorabils, "MAG":magabils, "MAR":marabils, "MIN":minabils, "NOB":nobabils, "ROG":rogabils, "WAR":warabils}