import sqlite3
from .database_connect import DB_Connector


class DB_Mutator(DB_Connector):
    '''
    '''
    def __init__(self, DB_file):
        DB_Connector.__init__(self,DB_file)
#-----------------------------------------------------------------------------------------------
    '''
    Add_New_Row() - method
    Paramters:
        TableName (String)
        Fields (List)
        Data (List)
    Inserts a new row in the the specified table (TableName).
    Inserts values in corresponding fields.
    Save changes to table.
    '''
    def Add_New_Row(self, Data):
        table_name = self.database_specs["db_tables"]["table_1"]["tabel_name"]
        Fields = self.database_specs["db_tables"]["table_1"]["fields_name"]
        datatype =self.database_specs["db_tables"]["table_1"]["fields_type"]

        query = "INSERT or IGNORE INTO "+ table_name
        into = "  ("
        values = " VALUES ("
        
        
        for f in range(len(Fields)):
            into += Fields[f]
            if(f != len(Fields)-1):
                into+=", "
        into += ")"


        for d in range(len(Fields)):
            if(datatype[d] == "TEXT"):
                values += '"'+Data[Fields[d]]+'"'
            else:
                values += str(Data[Fields[d]])
            if(d != len(Data)-1):
                values+=", "
        values += ")"

        query += into + values+";"

        #FOR APP LOGS PURPOSE
        print("**************************************")
        print("Database_Mutator.py -> Add_New_Row()")
        stm = "SQL Query: " + query
        print(stm)
        print("**************************************")

        self.Doer.execute(query)
        self.Conn.commit()
#-----------------------------------------------------------------------------------------------
    '''
    Update_Row() - method.
    Parameters:
        TableName (String)
        Fields (Dictionary)
        JobID (unknown) - Depends on the input of the user.
    Updates a single or various rows in the table provided (TableName).
    Inserts data in specified row given the Primary Key(JobID)
    Data to be updated is located in a dictionary (Fields).
    Saves changes to table.
    '''
    def Update_Row(self, TableName, ColumnN, ColumnD, JobID,PkVal):
        self.Doer.execute("update '{0}' set '{1}'='{2}' where '{3}'=='{4}'".format(TableName, ColumnN, ColumnD, PkVal, JobID ))
        self.Conn.commit()
        print("INSIDE UPDATE ROW")
