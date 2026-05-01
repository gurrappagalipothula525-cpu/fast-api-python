from pymongo import MongoClient
# conn= MongoClient("mongodb+srv://gurrappa:guru1234@cluster0.ofmvxg6.mongodb.net/Project0")

conn = MongoClient("mongodb://localhost:27017")
database = conn["usersdb"]
collection = database["users"]