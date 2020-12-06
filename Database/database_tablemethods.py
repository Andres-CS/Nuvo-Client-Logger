# Client
def _insert(table, data, **addData):
    #Start SQL statement
    sql = "INSERT INTO "+ table + " ("
    #Make list of fields and values
    fld=""
    vls=""
    for f in data[table]:
        fld += f + ", "
        vls += '"' + str(data[table][f]) + '"' + ", "
    #Check if addData has data and add it
    if bool(addData):
        for f_ in addData:
            fld += f_ + ", "
            vls += '"' + str(addData[f_]) + '"' + ", " 
    #remove last comma
    fld = fld[:-2]
    vls = vls[:-2]
    #Complete SQL statement
    sql += fld + ") VALUES (" + vls +");"
    #Return SQL
    return sql

def _select(table, data, **addData):
    #Start SQL statement
    sql = "SELECT "
    # Select Fields
    fls=""
    for f in data[table]:
        fls += f + ", "
    #Remove last Comma
    fls=fls[:-2]
    #Continue SQL 
    sql += fls + " FROM " + table + ";"  
    return sql

def sql_query(crud, table, data, **addData):
    if crud == "CREATE":
        return _insert(table,data,**addData)
    if crud == "READ":
        return _select(table,data,**addData)

data ={ 'client_table': {'client': 'Individual_1'}, 
        'job_table': {'job_id': 2359, 'job_name': 'BNK30'}, 
        'FinalPrint_table': {'job_id': 2359, 'type_of_book': 'Term Sheet', 'number_of_copies': 24, 'number_of_pages': 79, 'number_of_printers': 2, 'siding': 2, 'paper': 'Hammermill - Letter', 'printer': 'CANON', 'coil': 'None', 'inserts': 0.0, 'number_sheets': 948.0, 'number_sheet_per_book': 39.5, 'number_rims': 4.74, 'number_cartons': 0.47400000000000003, 'coil_size': 'None', 'time_printing': 'Sat Dec 5 01:01:59 2020'}
      }

print()
print(sql_query("CREATE", "client_table", data))
print()
print(sql_query("CREATE", "job_table", data, **{ "client_di":"1" }))
print()
print(sql_query("CREATE", "FinalPrint_table", data))

print()
#print(sql_query("READ","job_table",data))
print()
#print(sql_query("READ","job_table",data))
print()
#print(sql_query("READ","FinalPrint_table",data))