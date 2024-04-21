import argparse
from bson.objectid import ObjectId

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://goitlearn:12341234@goitlearn.ilwgpcj.mongodb.net/?retryWrites=true&w=majority&appName=goitlearn"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection

db = client.test.cats

parser = argparse.ArgumentParser(description='Create CRUD functionality')
parser.add_argument('--action', help='[create, read, update, delete]')
parser.add_argument('--id', help='ID of the cat')
parser.add_argument('--name', help='name of the cat')
parser.add_argument('--age', help='age of the cat')
parser.add_argument('--features', nargs='+', help='features of the cat')

args = vars(parser.parse_args())
action = args["action"]
pk = args["id"]
name = args["name"]
age = args["age"]
features = args["features"]

def read():
    return db.find()

def create(name, age, features):
    return db.insert_one({
        "name": name,
        "age": age,
        "features": features
    })

def update(pk, name, age, features):
    return db.update_one({"_id": ObjectId(pk)}, {"$set": {"name":name, "age":age, "features":features}})

def delete(pk):
    if (pk):
        return db.delete_one({'_id': ObjectId(pk)})
    else:
        return db.delete_many()

if __name__ == "__main__": 
    match action:
        case "create":
            result = create(name, age, features)
            print(result.inserted_id)
        case "read":
            [print(elem) for elem in read()]
        case "update":
            result = update(pk, name, age, features)
            print(result.modified_count)
        case "delete":
            result = delete(pk)
            print(result.deleted_count)
        case _:
            print('Wrong action')
