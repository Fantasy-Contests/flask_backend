# Third-party imports
from flask import Flask, jsonify, request
##from decouple import config
from fantasy_app.fff import current_week



app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')

# stop tracking modifications
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#DB.init_app(app)

@app.route('/')
def hello1():
    return jsonify('Hello, World!!!!')

@app.route('/test_submodule', methods=['GET', 'POST'])
def submodule():
    week = current_week()
    return str(week)
