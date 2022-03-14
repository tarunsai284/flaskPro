import requests
import time
from pymongo import MongoClient

client = MongoClient("mongodb+srv://<username>:<password>@cluster0.qvnyy.mongodb.net/Crypto_db?ssl=true&ssl_cert_reqs=CERT_NONE")   #this will be our mongo db
db = client.get_database('Crypto_db')    #this will be the name of our db in mongo
records = db.Bitcoin_price      #we can have a collection for each type of crypto maybe????

list(records.find({}, {"bpi":{"USD":{"rate_float":1}}}))