import os
import sqlite3
import json

class DB_Creator:
    '''
    __init__() -  Class constructor.
    Parameters:
        DB (JSON object)
    Accepts a JSON object which will has the Database specs.
    Creates the connector object and the cursor object.
    Saves changes to database file.
    '''
    def __init__(self, DB):
        database = DB
        # 1) Create Database
        try:
            self.Conn = self._DB_Connector(database["database"]["db_name"]) 
            self.Doer = self.Conn.cursor()
            self.Conn.commit()
        except sqlite3.Error as er:
            print("Something Happend While Creating the Database:")
            print(er)
        
        #2 Create Database Tables
        try:
            self._Create_table(database["database"]["db_tables"])
        except sqlite3.Error as er:
            print("Something Happend while creating the Database's tables")
            print(er)

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
    It checks if the database file to be created has ".db" as its extention.
    '''
    def _File_Inspector(self, filename):
        if '.db' in filename[len(filename)-3:len(filename)]:
            return True
        return False	

#-----------------------------------------------------------------------------------------------
    ''' 
    _Get_pf_keys() -  method
    Parameters:
        typeKey (String)
        keys    (JSON object)
    Accepts a STRING which specifies the type of key to be retrive and a JSON object 
    representation of the PRIMARY and FOREIGN keys to be assigned.
    Parses each object and creates a SQL stament with its respected KEY fields.
    '''
    def _Get_pf_key(self,typeKey,keys):
        sql = list()
        sql.append(f"{typeKey} KEY")

        kys = "("
        rfs = "("

        #Check Keys exits
        if keys["exist"]:
            #Get the fields to be keys
            for fl in keys["fields"]:
                kys = kys + fl + ", "
            #Remove trailing comma
            kys = kys[:-2]
            kys = kys + ")"
            sql.append(kys)
            #Check if keys are based on a external table
            if keys["reference"]:
                rf_table = keys["reference"]
                sql.append(f"REFERENCES {rf_table}")
                #Get the fields from external table
                for rf in keys["reference_fields"]:
                    rfs = rfs + rf +", "
                #Remove trailing comma
                rfs = rfs[:-2]
                rfs = rfs + ")"
                sql.append(rfs)

        else:
            return None
        #Merge/Join SQL statement
        sql = " ".join(sql)
        print(sql)
        return sql

#-----------------------------------------------------------------------------------------------
    ''' 
    _Create_table() -  method
    Parameters:
        tables (JSON object)
    Accepts a JSON object representation of the tables to be created 
    Parses each object and creates a table with its respected field.
    '''
    def _Create_table(self, tables):

        sql = list()
        
        #Create SQL statement
        for name in tables:
            # --- Part 1 ---
            sql.append(f"CREATE TABLE IF NOT EXISTS {name} (")
            # --- Part 2 ---
            vls = " "
            for fieldName in tables[name]["fields"]:
                vls = vls + fieldName + " " + tables[name]["fields"][fieldName] + ", "
            
            # --- Part 3 ---
            #Check for PRIMARY KEYs
            if tables[name]["pk"]["exist"]:
                vls = vls +  self._Get_pf_key("PRIMARY",tables[name]["pk"]) 
                vls = vls + ", "
            
            # --- Part 4 ---
             #Check for FOREIGN KEYs
            if tables[name]["fk"]["exist"]:
                vls = vls + self._Get_pf_key("FOREIGN",tables[name]["fk"])
                vls = vls + ", "

            #Remove coma from last field
            sql.append(vls[:-2])

            # --- Part 5 ---
            sql.append(");")

            #Merged query
            sql = " ".join(sql)
            
            #Execute query
            self.Doer.execute(sql)
            
            sql = []
        
        #Save action in DB
        self.Conn.commit()