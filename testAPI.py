import json

import pytest 

from search import get_restaurant_nearby
from searchNearbyAPI import app

restaurant_test = [{
    "blurhash": "UYLW^ead*0%24nf6DiRjI]RjMxSgMxx]kBRQ",
    "city": "Helsinki",
    "currency": "EUR",
    "delivery_price": 390,
    "description": "Sushia tuoreista raaka-aineista",
    "image": "https://prod-wolt-venue-images-cdn.wolt.com/5ccab0d56f0ac41e1cd75f7f/3204aff8bf9036615d694f0f85755726",
    "location": [
        24.942486584186554,
        60.16846747856398
    ],
    "name": "Hanko Sushi Stockmann",
    "online": False,
    "tags": [
        "sushi",
        "japanese"
    ]
}]

def test_search_key_in_name():
    assert len(get_restaurant_nearby('HanKo', 
                            24.942486584186554, 
                            60.16846747856398, 
                            restaurant_test)) == 1
    assert len(get_restaurant_nearby('HANKO', 
                            24.942486584186554, 
                            60.16846747856398, 
                            restaurant_test)) == 1
    
def test_search_key_in_description():
    assert len(get_restaurant_nearby('raAka', 
                            24.942486584186554, 
                            60.16846747856398, 
                            restaurant_test)) == 1

def test_search_key_in_tag():
    assert len(get_restaurant_nearby('Japan', 
                            24.942486584186554, 
                            60.16846747856398, 
                            restaurant_test)) == 1

def test_search_key_no_result():
    assert len(get_restaurant_nearby('burger', 
                            24.942486584186554, 
                            60.16846747856398, 
                            restaurant_test)) == 0
    
def test_distance():
    #Test distance > 3km
    assert len(get_restaurant_nearby('sushi', 
                            25.942486584186554, 
                            60.16846747856398, 
                            restaurant_test)) == 0
    #Test distance <= 3km
    assert len(get_restaurant_nearby('sushi', 
                            24.962486584186554, 
                            60.16846747856398, 
                            restaurant_test)) == 1


@pytest.fixture
def client():
    test_client = app.test_client()
    return test_client


def test_API(client):
    test_url = '/search-nearby?q={}&lat=24.9400752782822&lon=60.2001494897883'
    response = client.get(test_url.format('burger'))
    assert response.status_code == 200


    
    
