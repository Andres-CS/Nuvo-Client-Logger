#Form-> Transaction -> Database

import os
import json

from Database.database_accessor import DB_Accessor
from Database.database_mutator import DB_Mutator

# -------------------------------- BRIDGE TOOLS -------------------------------------

class databaseBridge():

    def __init__(self):
        print("Bridge Initialized")
        self.database = self._DatabaseToUse()
    
    def _DatabaseToUse(self):
        #GET DATABASE TO BE USED
        try:
            db_file = os.path.join(os.path.dirname(__file__),"Database\_CONFIG\DBs_App.json")
            with open(db_file, 'r') as dbinfo:
                info = json.load(dbinfo)
        except:
            print("SOMETING HAPPENED WITH EITHER THE DATABASE OR THE CONFIG FILE")
        
        return info[info["current_db"]]

    
    def _Map(self, externalData):
        data = dict()
        #GET MAP SCHEMA FILE 
        try:
            map_file = os.path.join(os.path.dirname(__file__),"Database\_CONFIG\MapSchema.json")
            with open(map_file,'r') as map:
                MapSchema = json.load(map)
        except:
            print("SOMETHING HAPPENED WITH THE MAP FILE.")
        #Map USERDATA
        for key1 in externalData["userData"]:
            # --- THIS NEEDS FIXING ON THE GUI SIDE
            if key1 == "TextInput":
                print("TextInput Read")
            else:
                data[MapSchema[key1]] = externalData["userData"][key1]
        #MAP RESULTDATA
        for key2 in externalData["resultData"]:
            data[MapSchema[key2]] = externalData["resultData"][key2]
                
        return data
    

    def send2DB(self, PAYLOAD):
        _STATUS = None
        _RECORD = self._Map(PAYLOAD["PAYLOAD"])
        #ID CURD'S VALUE
        if(PAYLOAD["CRUD"] == "CREATE"):
            print(PAYLOAD["CRUD"])
        elif(PAYLOAD["CRUD"] == "READ"):
            print(PAYLOAD["CRUD"])
        elif(PAYLOAD["CRUD"] == "UPDATE"):
            print(PAYLOAD["CRUD"])
        elif(PAYLOAD["CRUD"] == "DELETE"):
            print(PAYLOAD["CRUD"])





# -----------------------------------------------------------------------------------


def process_db_header(headers):
    tmp = list()
    for h in headers:
        tmp.append(h.replace("_"," ").title())
    return tmp

'''
Get_database_name()
'''
def Get_database_name():
    db_file =""
    if(os.name == "posix"):
        db_file = os.path.join(os.path.dirname(__file__),"./Database/DB_TMP.json") #UNIX / LINUX
    elif(os.name == "nt"):
        db_file = os.path.join(os.path.dirname(__file__),".\\Database\\DB_TMP.json") #WINDOS SYS

    tmp = dict()
    with open(db_file) as dbf:
        tmp = json.load(dbf)
    dbf.close()

    return tmp["db_name"]




'''
--------------------------- FOR DB MUTATION -------------------------------------------
'''
from Database.database_mutator import DB_Mutator

'''
process_data_for_db()
    *This function makes sure that the Fields in the App are compatible with the ones in the DB.
    *For purpose of scalability we are assuming that there will be multiple DB files as application is used with time.
     For such reason the fileds in the DB files will always match the appropiate labels in the result dialogs, this mathcing
     will be taken care in a "setup/config" confile when app starts.
    *For such prupose this fucntion will always make the labels to lower case and strip out the whitespaces.
'''
def process_data_for_db(user_input, calc_resuts):
    
    #Pass data to lower case
    ui = dict()
    cr = dict()
    final = dict()

    #To Lower and replace whitespaces
    for ui_k in list(user_input.keys()):
        k_lower = ui_k.lower().replace(" ","_")
        ui[k_lower] = user_input[ui_k]
    
    for cr_k in list(calc_resuts.keys()):
        k_lower = cr_k.lower().replace(" ","_")
        cr[k_lower] =calc_resuts[cr_k]


    final = ui
    final.update(cr)
    return final

'''
fields_and_data()  --- OBSOLET
'''
def get_fields_and_data(data):
    fields = list()
    values = list()

    for k in list(data.keys()):
        fields.append(k)
        values.append(data[k])
    
    return fields, values


'''
send2DB()    
    *Accepts the dicts with data provided by the user and results calculated.
    *This function is the bridge between the Application and the DB storing all the data provided. 
    *This functions calls all the other necesary functions that analyze the data provided by the forms to make them DB compatible.
    *As a last step it opens the DB connection and add the data to the DB.
'''
def send2DB(PAYLOAD):
    _Status = None

    #ID CURD'S VALUE
    if(PAYLOAD["CRUD"] == "CREATE"):
        print(PAYLOAD["CRUD"])
        _Record = M
    elif(PAYLOAD["CRUD"] == "READ"):
        print(PAYLOAD["CRUD"])
    elif(PAYLOAD["CRUD"] == "UPDATE"):
        print(PAYLOAD["CRUD"])
    elif(PAYLOAD["CRUD"] == "DELETE"):
        print(PAYLOAD["CRUD"])

    '''data = process_data_for_db(user_input,calc_resuts)

    #ui_filds, ui_values = get_fields_and_data(ui)
    #cr_filds, cr_values = get_fields_and_data(cr)
    
    #Get Database Name based on how the Database_Setup.py file seted up.
    db_2_use = Get_database_name()

    #Pass Data to DB
    db_mut = DB_Mutator(db_2_use)

    db_mut.Add_New_Row(data)
    
    db_mut.Exit_DB()
    '''



'''
--------------------------- FOR DB ACCESS -------------------------------------------
'''
from Database.database_accessor import DB_Accessor

class database():
    def __init__(self):
        self.db_conn =  DB_Accessor(Get_database_name())

        #TMP data holder
        self.tmp=list()
    
    def get_data(self,prmts):
        #Determine if all records
        if(self._all_recods(prmts)):
            return self.db_conn.All_Logs()
        else:
            return self._get_records(prmts)
    
    def get_ColHeading(self):
        return process_db_header(self.db_conn.get_ColNames())
    
    def _all_recods(self,prmts):
        prmt_counter = 0
        for prmt in prmts.keys():
            if not prmts[prmt]=="":
                prmt_counter+=1
        if prmt_counter > 0:
            return False
        return True

    def _get_records(self,prmts):
        fields = list(prmts.keys())
        values = list()
        for v in fields:
            values.append(prmts[v])
        return self.db_conn.Search_logs(fields,values)

        




        
                







   

