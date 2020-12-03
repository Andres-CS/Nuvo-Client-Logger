import os
import json
from App_DB_Bridge import databaseBridge

class clients():
    def __init__(self):
        self.obj = databaseBridge()
        
        #Payload Template
        self.PAYLOAD = {
            "CRUD" : "",
            "PAYLOAD": {
                "userData" : dict(),
                "resultData" : dict()
            }
        }
        
    def get_clients(self):
        #Define CRUD
        self.PAYLOAD["CRUD"] = "READ"
        self.obj.send2DB()

    def add_clients(self):
        #Define CRUD
        self.PAYLOAD["CRUD"] = "CREATE"

        #TMP
        clt=list()
        with open(os.path.join(os.path.dirname(__file__),"client.txt")) as lst:
            for l in lst.readlines():
                clt.append(l.split("\n")[0])
        lst.close()

        for c in clt:
            self.PAYLOAD["PAYLOAD"]["userData"]["Client"]=c
            self.obj.send2DB(self.PAYLOAD)
       
        

        

        

client_file = os.path.join(os.path.dirname(__file__),"client.txt")

def get_clients():
    clients=list()
    with open(client_file) as clis:
        for i in clis.readlines():
            clients.append(i.split("\n")[0])
    clis.close()
    return clients



def set_client(new_client):
    clis = open(client_file,"a+")
    clis.write(new_client+"\n")
    clis.close()
