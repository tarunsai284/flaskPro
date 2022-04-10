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


@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/about')
def about():
    return render_template('about.html')

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