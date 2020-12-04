'''
In this file will be contained the blase that connects to a SQLite Database; and offsprings...
    * database_Accessor:  class will be used only for quering the database the base class connected to.
    * database_Mutator:   class will be to update the database the base class connected to.
'''

import sqlite3
import json
import os

class DB_Connector:
    '''
    __init__() -  Class constructor.
    Parameters:
        DBName (string)
    Accepts a string which will become the Database file.
    Creates the connector object and the cursor object.
    Saves changes to database file.
    '''
    def __init__(self, DBName):
       #GO TO STORAGE FOLDER
        self.Location_Database = os.path.join( os.path.abspath(os.path.join( os.path.dirname(__file__), os.pardir )), "Storage\\"+DBName )
        self.Conn = self.DB_Connect(self.Location_Database)
        self.Doer = self.Conn.cursor()
        self.Conn.commit()

#-----------------------------------------------------------------------------------------------
    '''
    DB_Connector() - method.
    Parameters:
        db_filename (string)
    Accespts a string which will become the database file.
    It returns the sqlite3 object.
    '''
    def DB_Connect(self, db_filename):
        if(self.File_Inspector(db_filename)):
            return sqlite3.connect(db_filename)
        else:
            print("Not such file")
#-----------------------------------------------------------------------------------------------
    '''
    File_Inspector() -  method
    Parameters:
        filename (string)
    Accepts a string and parses it for proper file extention.
    '''
    def File_Inspector(self, filename):
        if '.db' in filename[len(filename)-3:len(filename)]:
            return True
        return False
#-----------------------------------------------------------------------------------------------
    '''
    Exit_DB() - Method
    Parameters:
        None
    Closes connection witht the Databas.
    '''
    def Exit_DB(self):
        self.Conn.close()
#-----------------------------------------------------------------------------------------------