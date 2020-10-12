from database_creator import DB_Creator
import json

with open("DB_specs.json", 'r') as db:
    spcs = json.load(db)
db.close()

db = DB_Creator(spcs)