import os
import json



_DATABASE = "Database"
_CONFGFILE = "DBs_App.json"
_STORAGE = "Storage"


# -------- LOW LEVEL METHODS -------- 

# 1. Check DB to be used.
'''
    In the APP'S ROOT FOLDER look for the Database FOLDER
    In Database FOLDER look for DBs_App.json FILE
    Load DBs_App.json FILE
'''
def _get_DB_Config():
    if os.path.exists(_DATABASE):
        #Change dirs
        os.chdir( os.path.join( os.path.dirname(__file__), _DATABASE) )
        if os.path.exists(_CONFGFILE):
            #Load File data
            with open(_CONFGFILE, 'r') as config:
                dbconfig = json.load(config)
                #print(db)
            config.close()
    return dbconfig

# 2. Check DB exists in _STORAGE Folder 
def _get_DB_exists():
    flag = False
    if _STORAGE in os.listdir():
        #Change Dirs
        os.chdir(os.path.join(os.path.dirname(__file__), _STORAGE))
        file = _DBCONFIG[_DBCONFIG["current_db"]]
        #Check if file exists
        if os.path.exists(file):
            flag = True
            print("DB Exisits")
    return flag

# 3. Update DB Info with SIZE & WARNING 
def _set_DB_size_warning():
    #Go to STORAGE folder
    if os.path.exists(_STORAGE):
        os.chdir(os.path.join(os.path.dirname(__file__),_STORAGE))
        #Current Size of DB
        _DBCONFIG["currentsize"] = os.path.getsize(_DBCONFIG[_DBCONFIG["current_db"]])
        print("DB size: ",end=' ')
        print(_DBCONFIG["currentsize"])
        #Clac warning Level
        percFull = _DBCONFIG["currentsize"] / _DBCONFIG["maxsize"]
        print("DB percentage: ",end=" ")
        print(percFull)
        if percFull < _DBCONFIG["warning"]["1"]:
            _DBCONFIG["warning"]["level"] = 1
        elif percFull <= _DBCONFIG["warning"]["2"]:
            _DBCONFIG["warning"]["level"] = 2
        elif percFull <= _DBCONFIG["warning"]["3"]:
            _DBCONFIG["warning"]["level"] = 3
        elif percFull <= _DBCONFIG["warning"]["4"]: 
            _DBCONFIG["warning"]["level"] = 4
        else:
            print("NEED TO CHANGE/CREATE A NEW DB - EXCEDED LIMITS")
        print("DB Level: ", end=" ")
        print(_DBCONFIG["warning"]["level"])

# 4. Update DBs_App.json file
def _update_DB_Config_File():
    os.chdir( os.path.join( os.path.dirname(__file__), _DATABASE) )
    #Check we are in DATABASE folder
    if _DATABASE == os.getcwd()[-len(_DATABASE):]:
        with open(_CONFGFILE, 'w') as config:
            json.dump(_DBCONFIG,config)
        config.close()


# -------- MID LEVEL METHODS -------- 


def _DB_Setup():
    global _DBCONFIG 
    _DBCONFIG = _get_DB_Config()
    #Go to App's ROOT folder
    os.chdir("..")
    if(_get_DB_exists()):
        #Go to App's ROOT folder
        os.chdir("..")
        _set_DB_size_warning()
    #Go to App's ROOT folder
    os.chdir("..")
    _update_DB_Config_File()
    #Go to App's ROOT folder
    os.chdir("..")


# -------- TOP LEVEL METHODS -------- 


def setUp():
    _DB_Setup()
    print(os.getcwd())



# --- RUN SETUP SCRIPT --- 