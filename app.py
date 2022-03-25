from flask import Flask, jsonify, request, render_template
from mongoClient import setupMongoClient
from logging.config import fileConfig
import logging


app = Flask(__name__)
app.config.from_object('config')
fileConfig('logging.cfg')
db = setupMongoClient(app)


@app.route('/')
def index():
    app.logger.debug("Jelkvn sdl v")
    app.logger.debug(db.list_collection_names())
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/charts/{param}')
def charts():
    app.logger.debug("Jelkvn sdl v")
    db.query({})
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

@app.route('/mongo/delete/{}')


if __name__ == "__main__":
    app.run()