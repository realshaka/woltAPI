import json

from geopy.distance import geodesic as distance

def load_data():
    with open('restaurants.json') as json_file:
        data = json.load(json_file)
        restaurants = data['restaurants']
        return restaurants

def check_search_key_valid(search_key):
    if len(search_key) >= 1:
        return True
    return False

def check_distance(lat, lon, restaurant_location):
    user_coordinates = (lat, lon)
    restaurant_coordinates = (restaurant_location[0], restaurant_location[1])
    # Check distance between user and restaurant under 3km 
    if distance(user_coordinates, restaurant_coordinates).km <= 3:
        return True
    return False

def check_name(search_key, restaurant_name):
    if search_key.lower() in restaurant_name.lower():
        return True
    return False

def check_description(search_key, restaurant_description):
    if search_key.lower() in restaurant_description.lower():
        return True
    return False

def check_tags(search_key, restaurant_tag):
    for tag in restaurant_tag:
        if search_key.lower() in tag.lower():
            return True
    return False

def check_restaurant(search_key, lat, lon, restaurant):
    if check_distance(lat, lon, restaurant['location']):
        if (check_name(search_key, restaurant['name']) or
                check_description(search_key, restaurant['description']) or
                check_tags(search_key, restaurant['tags'])):
            return True
    return False

def get_restaurant_nearby(search_key, lat, lon, restaurants):
    result = []
    for restaurant in restaurants:
        if check_restaurant(search_key, lat, lon, restaurant):
                result.append(restaurant)
    return result