import os
import json

# 1. Check DB to be used.
'''
    In the APP'S ROOT FOLDER look for the Database FOLDER
    In Database FOLDER look for DBs_App.json FILE
    Load DBs.App.json FILE
'''
_FOLDER = "Database"
_FILE = "DBs_App.json"

if os.path.exists(_FOLDER):
    #Change dirs
    os.chdir( os.path.join( os.path.dirname(__file__), _FOLDER) )
    if os.path.exists(_FILE):
        #Load File data
        with open(_FILE, 'r') as config:
            db = json.load(config)
            #print(db)
        config.close()
    #Go back to root folder
    os.chdir("..")


# 2. Check DB exists
'''
''' 
_FOLDER = "Storage"

if _FOLDER in os.listdir():
    #Change Dirs
    os.chdir(os.path.join(os.path.dirname(__file__), _FOLDER))
    file = db["current_db"]
    file = db[file]
    #Check if file exists
    if os.path.exists(file):
        print("GOOD")
        print(os.listdir())
    #Go back to root folder
    os.chdir("..")


# 3. Update DB Info