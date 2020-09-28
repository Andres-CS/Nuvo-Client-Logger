import sqlite3
from .database_connect import DB_Connector


class DB_Accessor(DB_Connector):
    '''
    __init__() - Constructor
    Parameters:
        None
    It runs it parent's constructor.
    '''
    def __init__(self,DB_file):
        DB_Connector.__init__(self,DB_file)
        pass
#-----------------------------------------------------------------------------------------------
    '''
    All_Logs() - method
    Parameters:
        TableName (string)
    Accepts a table name and queries for all the data in such table.
    Returns in list format all the rows in the table name provided.
    '''
    def All_Logs(self):
        self.Doer.execute("select * from '{}'".format(self.database_specs["db_tables"]["table_1"]["tabel_name"]))
        query=self.Doer.fetchall()
        return query

#-----------------------------------------------------------------------------------------------

    def Search_logs(self,fields,values):
        query=""
        select = "SELECT * FROM "+self.database_specs["db_tables"]["table_1"]["tabel_name"]
        where = " WHERE "
        And = " AND "
        equal = list()

        #Get Fields and Values
        for v in range(len(values)):
            if values[v] == "":
                continue
            tmp = fields[v]+" = '"+values[v]+"'"
            equal.append(tmp)

        #Build condition
        condition =""
        for i in range(len(equal)):
            if i>0 and i < len(equal):
                condition += And
            condition += equal[i]
        condition += ";"

        #Complete Query
        query = select + where + condition
        #Execute Query
        self.Doer.execute(query)
        
        return self.Doer.fetchall()
    
    def get_ColNames(self):
        return self.database_specs["db_tables"]["table_1"]["fields_name"]
