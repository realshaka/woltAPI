import logging

import flask
from flask import request, jsonify

from search import load_data, check_search_key_valid, get_restaurant_nearby

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/search-nearby', methods=['GET'])
def search_nearby():
    logging.info("search-nearby API")
    result = []
    search_key = request.args['q']
    lat = request.args['lat']
    lon = request.args['lon']

    try:
        restaurants = load_data()
    except IOError as e:
        logging.error(e)
        return "Cannot get data", 500

    if check_search_key_valid(search_key):
        result = get_restaurant_nearby(search_key, lat, lon, restaurants)            
    else:
        return 'Bad request', 404

    return jsonify(result), 200
    

if __name__ == '__main__':
    app.run()