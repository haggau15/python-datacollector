import pprint
import time
import urllib.request
import json
from pymongo import MongoClient

from pythonProject.venv.env import API_KEY

COORDINATES = "59.913643%2C10.750383"
RADIUS = "10"
CONNECT = "mongodb+srv://123:123@menu.hmcvdtv.mongodb.net/"
# GET_REVIEWS = 'https://mybusiness.googleapis.com/v4/accounts/{accountId}/locations/{locationId}/reviews'
FIND_PLACE = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?fields=formatted_address%2Cname%2Crating&input=fast%20food&inputtype=textquery&locationbias=circle%3A700%40" + COORDINATES + "&key="

NEARBY_SEARCH = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=fast%20food&location=" + COORDINATES + "&radius=" + RADIUS + "&type=restaurant&key="

PLACE_ID = "ChIJa_rEoF9uQUYRrFqJ3brGxfs"
client = MongoClient(CONNECT)
print(client.list_database_names())
db = client.eksamen
print(db.list_collection_names())
user = db.users
u = {"Name": "Obama"}


def get_locations():
    with urllib.request.urlopen(NEARBY_SEARCH + API_KEY) as response:
        data = response.read()
        data = json.loads(data)
        l = data["results"]
        print(l)
        for i in l:
            print(json.dumps(i, indent=4))
            exit(1)

            # print(json.dumps(data, indent=4))
        # result = user.insert_one(u)


get_locations()

# res = gmaps.places.nearby_search(location = '59.922498, 10.751539', radius = 100, open_now = False, type='resturant')  #gmaps.places(query='Eineåsen skole')
# print(res.get('results'))


# with urllib.request.urlopen('https://maps.googleapis.com/maps/api/place/details/json?place_id=ChIJa_rEoF9uQUYRrFqJ3brGxfs&fields=place_id&reviews&key='+API_KEY) as response:
# res = response.read()
# my_json = res.decode('utf8').replace("'", '"')
# data = json.loads(my_json)

# print(res)

with urllib.request.urlopen(
        'https://maps.googleapis.com/maps/api/place/details/json?fields=name%2Crating%2Creviews&place_id=' + PLACE_ID + '&key=' + API_KEY) as response:
    res = json.loads(response.read())
    # my_json = res.decode('utf8').replace("'", '"')
    # data = json.loads(my_json)
    for i in res['result']['reviews']:
        print(i['rating'])
        print(i['text'] + "\n")
        # print(res['result']['reviews'][]['rating'])
