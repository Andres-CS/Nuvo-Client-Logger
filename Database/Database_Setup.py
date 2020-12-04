#
#   LEGACY
#

'''     Database Set Up.       '''
import json
import os
from .database_creator import DB_Creator


def _get_db_specs(db,filename):
    specs = dict()
    with open(filename,"r") as db_data:
        #Get config data
        specs = json.load(db_data)
    
    specs = specs[db]
    return specs

'''Determins if a DB existis in the File systems'''
def database_exits(filename):
    fn = filename
    if '.db' not in fn[len(fn)-3:len(fn)]:
        fn=fn+".db"
    fn = os.path.join(os.path.dirname(__file__),fn)
    print("**************************************")
    print("Database_Setup.py -> Database_Exists()")
    stm = "Is database in path: " + fn + " ----> " + str(os.path.isfile(fn))
    print(stm)
    print("**************************************")
    
    return os.path.isfile(fn)


'''
Set the DB to be used based on the configuration file.
'''
def DB_Setup():
    #Get file DBs_App.json.
    config_file = os.path.join(os.path.dirname(__file__),"DBs_App.json")
    #Stores Config Data 
    specs = dict()        
    #TMP FILE, WHILE APP IN USE.
    tmp_f = "DB_TMP.json"

    #DATA FOR TMP FILE.
    tmp_data = {
        "specs_file":"",
        "warning_level":0,
        "db_name": "",
    }

    #Open DBs_App.json file.
    try:
        with open(config_file,"r") as cfg_file:
            #Get config data
            specs = json.load(cfg_file)
        #Close DBs_App file.
        cfg_file.close()
    except:
        ''' TO BE DONE'''
    
    '''CHECK IF CURRENT DB EXISTS, IF NOT CREATE...'''
    if ( database_exits(specs["current_db"])):
        dbspecs = _get_db_specs( specs["current_db"], os.path.join(os.path.dirname(__file__),specs["specs_file"]))
        DB_Creator(specs["current_db"]+".db",dbspecs)
    
    #Check DB warning level
    if(specs["warning"]["level"] < 4):
        print("**************************************")
        print("Database_Setup.py -> DB_Setup()")
        stm = "Database warning level: " + str(specs["warning"]["level"]) + "\n" + str(specs["warning"][str(specs["warning"]["level"])])
        print(stm)
        print("**************************************")
        tmp_data["warning_level"] = specs["warning"]["level"]
    else:
        '''
        IF THE WARNING LEVEL IS >4 THEN A NEW DB FILE HAS TO BE CREATED.
        THE DB TO BE CREATED IS THE ONE WITH THE NEXT CONSECITVY POST-FIX.

        THIS NEEDS TO BE ADJUSTED!.
        '''
        print(specs["warning"]["level"])
    
    
    #Get DB Spec path file.
    tmp_data["specs_file"] = specs["specs_file"]
    
    #Get Current DB
    tmp_data["db_name"]=specs["current_db"]


    #Write TMP DATA to TMP FILE.    
    with open(os.path.join(os.path.dirname(__file__),"DB_TMP.json"),"w") as tmpf:
        json.dump(tmp_data, tmpf)
    #Close Tmp File.
    tmpf.close()


    


    
    







