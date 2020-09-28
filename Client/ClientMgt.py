import os
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
