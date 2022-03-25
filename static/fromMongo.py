# import requests
import time
from pymongo import MongoClient

client = MongoClient("mongodb+srv://<username>:<password>@cluster0.qvnyy.mongodb.net/Crypto_db?ssl=true&ssl_cert_reqs=CERT_NONE")   #this will be our mongo db
db = client.get_database('Crypto_db')    #this will be the name of our db in mongo
records = db.Bitcoin_price      #we can have a collection for each type of crypto maybe????

# while True:   #infinite loop
#     r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")     #this will be the connection to CoinGecko
#     if r.status_code == 200:    #status code 200 means everything is 'good to go'
#         data = r.json()     #data is going to be request as json
#         print(data)
#         records.insert_one(data)
#         time.sleep(60)      #will this be set to 24 hours??
#     else:
#         exit()