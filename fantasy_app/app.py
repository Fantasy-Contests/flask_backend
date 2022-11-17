# Third-party imports
from flask import Flask, jsonify, request
import json
##from decouple import config
from .fff import current_week, get_highest, order_positions_by_points
from .contest_list import contests


def create_app():

    app = Flask(__name__)
    #app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')

    # stop tracking modifications
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #DB.init_app(app)

    @app.route('/')
    def hello1():
        return 'Hello, World!!!!'

    @app.route('/test_submodule', methods=['GET', 'POST'])
    def submodule():
        week = current_week()
        return str(week)
    
    @app.route('/most_points', methods=['GET', 'POST'])
    def calculate_yards():
        position =  'total_punter_points'
        points = get_highest(contests[position]['position_list'], 'puntYards')
        ranks = order_positions_by_points(points)
        data = json.dumps(ranks)
        return data
    return app