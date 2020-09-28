import os
import sqlite3
import json

class DB_Creator:
    '''
    __init__() -  Class constructor.
    Parameters:
        database (string)
        db_specs
    Accepts a string which will become the Database file.
    Creates the connector object and the cursor object.
    Saves changes to database file.
    '''
    def __init__(self, database, db_specs):
        #Create Database
        self.Conn = self._DB_Connector(database) 
        self.Doer = self.Conn.cursor()
        self.Conn.commit()
        
        #DB_Config Data
        self.db_config_data = db_specs

        #Create table(s) 
        self._Create_table()

        #Exit DB
        self.Conn.close()

#-----------------------------------------------------------------------------------------------
    '''
    DB_Connector() - method.
    Parameters:
        filename (string)
    Accespts a string which will become the database file.
    It returns the sqlite3 object.
    '''
    def _DB_Connector(self, filename):
        if(self._File_Inspector(filename)):
            return sqlite3.connect(filename)
        else:
            print("not such file")
#-----------------------------------------------------------------------------------------------
    '''
    File_Inspector() -  method
    Parameters:
        filename (string)
    Accepts a string and parses it for proper file extention.
    '''
    def _File_Inspector(self, filename):
        if '.db' in filename[len(filename)-3:len(filename)]:
            return True
        return False	
#-----------------------------------------------------------------------------------------------

    def _Create_table(self):

        #Table Vars
        db_instruction = "CREATE TABLE "
        table_name = self.db_config_data["db_tables"]["table_1"]["tabel_name"]
        table_fields = self.db_config_data["db_tables"]["table_1"]["fields_name"]
        table_fields_type = self.db_config_data["db_tables"]["table_1"]["fields_type"]

        #Create SQL statement
        db_instruction =  db_instruction+table_name+" ( "

        for x in range(len(table_fields)):
            db_instruction = db_instruction +table_fields[x]+" "+table_fields_type[x]
            if(x != len(table_fields)-1 ):
                db_instruction += ", "

        db_instruction += ");"

        print(db_instruction)

        #Execute query
        self.Doer.execute(db_instruction)

        #Save action in DB
        self.Conn.commit()

        
        
    
                        
        
