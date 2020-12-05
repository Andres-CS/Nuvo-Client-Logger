import sqlite3
from .database_connect import DB_Connector


class DB_Mutator(DB_Connector):
    '''
    '''
    def __init__(self, DB_file):
        DB_Connector.__init__(self,DB_file)
#-----------------------------------------------------------------------------------------------
    '''
    Add_New_Entry() - method
    '''
    def Add_New_Entry(self, Data):
        
        self.Doer.execute(query)
        self.Conn.commit()
#-----------------------------------------------------------------------------------------------
    '''
    Update_Row() - method.
    '''
    def Update_Row(self, TableName, ColumnN, ColumnD, JobID,PkVal):
        print("INSIDE UPDATE ROW")
