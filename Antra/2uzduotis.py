import pymongo as mdb


client = mdb.MongoClient('localhost',  27017)
restaurants_db = client.restaurantsDB
restaurants = restaurants_db.restaurants


def first():
    for restaurant in restaurants.find():
        print (restaurant)


def second():
    for restaurant in restaurants.find({}, {"restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1}):
        print (restaurant)


def third():
    for restaurant in restaurants.find({}, {"_id": 0, "restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1}):
        print (restaurant)


def fourth():
    for restaurant in restaurants.find({"borough": "Bronx"}):
        print (restaurant)


def fifth():
    for restaurant in restaurants.find({"grades": {"$elemMatch": {"score": {"$gte": 80, "$lte": 100}}}}):
        print (restaurant)


print("-------------------------------------------------------------------------------- First: --------------------------------------------------------------------------------")
first()
print("-------------------------------------------------------------------------------- Second: --------------------------------------------------------------------------------")
second()
print("-------------------------------------------------------------------------------- Third: --------------------------------------------------------------------------------")
third()
print("-------------------------------------------------------------------------------- Fourth: --------------------------------------------------------------------------------")
fourth()
print("-------------------------------------------------------------------------------- Fifth: --------------------------------------------------------------------------------")
fifth()
