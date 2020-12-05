from database_creator import DB_Creator
import json

with open("DB_specs.json", 'r') as db:
    spcs = json.load(db)
db.close()

#db = DB_Creator(spcs)

def t(lst,data):
    
    if(len(lst) == 0 ):
        return "Tabale: "
    else:
        print("Ok")

        return t(lst[1:],data) + ", " + str(lst[0])

STATUS = t(list(spcs["database"]["db_tables"].keys()), spcs["database"]["db_tables"])
print(STATUS)