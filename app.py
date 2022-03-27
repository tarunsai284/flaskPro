from asyncio import constants
from flask import Flask, jsonify, request, render_template
from static.mongoClient import setupMongoClient
import static.mongoDBLayer as mongoLayer
import logging, logging.config, constants, yaml



app = Flask(__name__)
app.config.from_object('config')
db = setupMongoClient(app)
collection = db[constants.OHLCV]

with open('./static/logConfig.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/charts/')
def charts():
    logging.debug("Charts")
    data = {
        "pie": {            #connect with the mongo db (find USD query??)
            'Task' : 'Hours per Day',
            'Work' : 11, 
            'Eat' : 2, 
            'Commute' : 2, 
            'Watching TV' : 2, 
            'Sleeping' : 7
        },
        "candle": [         #connect with mongo db??
            ['Mon', 20, 28, 38, 45],
            ['Tue', 31, 38, 55, 66],
            ['Wed', 50, 55, 77, 80],
            ['Thu', 77, 77, 66, 50],
            ['Fri', 68, 66, 22, 15]
        ]
    }
    return render_template('charts.html', data=data)

@app.route('/mongo')
def mongo():
    fromTimeStamp=1609459200000
    toTimestamp=1640995200000
    data = mongoLayer.getCrytoDataForTimeRange(collection, "BTC", fromTimeStamp, toTimestamp)
    return render_template('mongo.html', data=data)

if __name__ == "__main__":
    print("app")
    app.run()