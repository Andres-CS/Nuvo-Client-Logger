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
            
            #Map USERDATA
            for key1 in externalData["userData"]:
                # --- THIS NEEDS FIXING ON THE GUI SIDE ---
                if key1 == "TextInput":
                    print("TextInput Read")
                # --- THIS NEEDS FIXING ON THE GUI SIDE ---
                else:
                    data[MapSchema[key1]] = externalData["userData"][key1]
            #MAP RESULTDATA
            for key2 in externalData["resultData"]:
                data[MapSchema[key2]] = externalData["resultData"][key2]
        except:
            print("SOMETHING HAPPENED WITH THE MAP FILE.\DATA COULD NOT BE MAPPED")
        

        #LASTLY, MAP DATA ACCORDING TO TABLE
        try:
            new_data = dict()
            table_file = os.path.join(os.path.dirname(__file__),"Database\_CONFIG\DB_specs.json")
            with open(table_file,'r') as TableSchema:
                Tables = json.load(TableSchema)
            print("\n\n")
            #MAP DATA TO ALL TABLES
            for F in data:
                for T in Tables["database"]["db_tables"]:
                    if F in Tables["database"]["db_tables"][T]["fields"]:
                        if T in new_data:
                            new_data[T].update({F:data[F]})
                        else:
                            new_data[T] = {F:data[F]}
        except:
            print("SOMETHING HAPPENED WITH THE DATABASE TABLE FILE.\nDATA COULD NOT BE MAPPED")

        return new_data
    

    def send2DB(self, PAYLOAD):
        _STATUS = None
        _RECORD = self._Map(PAYLOAD["PAYLOAD"])
        print(_RECORD)
        #ID CURD'S VALUE
        if(PAYLOAD["CRUD"] == "CREATE"):
            print(PAYLOAD["CRUD"])
            DBobj = DB_Mutator(self.database)
            #_STATUS = DBobj.some_method()
            #return _STATUS
        elif(PAYLOAD["CRUD"] == "READ"):
            print(PAYLOAD["CRUD"])
            #DBobj = DB_Accessor(self.database)
            #_STATUS = DBobj.some_method()
            #return _STATUS
        elif(PAYLOAD["CRUD"] == "UPDATE"):
            print(PAYLOAD["CRUD"])
            #DBobj = DB_Mutator(self.database)
            #_STATUS = DBobj.some_method()
            #return _STATUS
        elif(PAYLOAD["CRUD"] == "DELETE"):
            print(PAYLOAD["CRUD"])
            #DBobj = DB_Mutator(self.database)
            #_STATUS = DBobj.some_method()
            #return _STATUS

# -----------------------------------------------------------------------------------




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

        




        
                







   

