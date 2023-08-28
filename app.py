# Third-party imports
from flask import Flask, jsonify, request
import json
import connexion
##from decouple import config
from fantasy_app_project.fff import current_week,get_most_position_points,order_positions_by_points, hello11
from fantasy_app_project.contest_list import contests


app = connexion.FlaskApp(__name__, specification_dir="./")
app.add_api("swagger.yml")

    #app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')

    # stop tracking modifications
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #DB.init_app(app)

@app.route('/')
def hello1():
    return 'Hello, World!!!!'

@app.route('/test_submodule', methods=['GET'])
def submodule():
    week = current_week()
    return str(week)
    
@app.route('/most_points', methods=['GET', 'POST'])
def calculate_yards():
    position =  'total_punter_points'
    points = get_most_position_points(contests[position]['position_list'], 8)
    ranks = order_positions_by_points(points)
    data = json.dumps(ranks)
    return jsonify(data)
  
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
