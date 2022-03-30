from flask import Flask, jsonify, request, render_template, Response
import logging, logging.config, constants, yaml 
from static.mongoClient import setupMongoClient
import static.mongoDBLayer as mongoLayer
import services.cryptoChartService as cryptoChartService
#import services.btcChartService as btcChartService
import services.bnbChartService as bnbChartService
import services.ethChartService as ethChartService
import services.ltcChartService as ltcChartService
import services.neoChartService as neoChartService


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

@app.route('/cryptoChart', methods=['GET', 'POST'])   #, methods=['GET', 'POST']
def cryptoChart():
    symbolGet = request.args.get("crypto_select")
    graphJSON = {"line": cryptoChartService.plotlyChartService(collection, symbolGet),
                "candle": cryptoChartService.plotlyChartServiceCandle(collection, symbolGet)}
    return render_template('cryptoChart.html', graphJSON=graphJSON)

@app.route('/bnbChart')
def bnbChart():
    graphJSON = {"line": bnbChartService.plotlyChartService(collection),
                "candle": bnbChartService.plotlyChartServiceCandle(collection)}
    return render_template('bnbChart.html', graphJSON=graphJSON)

@app.route('/ethChart')
def ethChart():
    graphJSON = {"line": ethChartService.plotlyChartService(collection),
                "candle": ethChartService.plotlyChartServiceCandle(collection)}
    return render_template('ethChart.html', graphJSON=graphJSON)

@app.route('/ltcChart')
def ltcChart():
    graphJSON = {"line": ltcChartService.plotlyChartService(collection),
                "candle": ltcChartService.plotlyChartServiceCandle(collection)}
    return render_template('ltcChart.html', graphJSON=graphJSON)

@app.route('/neoChart')
def neoChart():
    graphJSON = {"line": neoChartService.plotlyChartService(collection),
                "candle": neoChartService.plotlyChartServiceCandle(collection)}
    return render_template('neoChart.html', graphJSON=graphJSON)

if __name__ == "__main__":
    print("app")
    app.run()