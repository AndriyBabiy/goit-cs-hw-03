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

def read_all():
    return db.find()

def read_distinct(name):
    return db.find({"name": name})

def create(name, age, features):
    return db.insert_one({
        "name": name,
        "age": age,
        "features": features
    })

def update(pk, name, age, features):
    return db.update_one({"_id": ObjectId(pk)}, {"$set": {"name":name, "age":age, "features":features}})

def update_age(name, age):
    return db.update_one({"name": name}, {"$set": {"age": age}})

def update_features_by_name(name, features):
    for feature in features:
        result = db.update_one({"name": name}, {"$push": {"features": feature}})
    return result

def delete_by_id(pk):
    return db.delete_one({'_id': ObjectId(pk)})

def delete_by_name(name):
    return db.delete_one({'name': name})

def delete_all():
    return db.delete_many({})
    


if __name__ == "__main__": 
    match action:
        case "create":
            result = create(name, age, features)
            print(result.inserted_id)
        case "read":
            [print(elem) for elem in read_all()]
        case "read-by-name":
            if name:
                for elem in read_distinct(name):
                    print(elem)
            else:
                print("You forgot to state the name using the --name CLI argument")
        case "update":
            result = update(pk, name, age, features)
            print(result.modified_count)
        case "update-age": 
            if name and age:
                result = update_age(name, age)
                print(result.modified_count)
            elif not name and not age:
                print("You forgot to state the name and age using the --name and --age CLI arguments")
            elif not name:
                print("You forgot to state the name using the --name CLI argument")
            elif not age:
                print("You forgot to state the age using the --age CLI argument")
        case "update-features": 
            if name and features:
                for feature in features:
                    result = update_features_by_name(name, features)
                print(result.modified_count)
            elif not name and not features:
                print("You forgot to state the name and features using the --name and --features CLI arguments")
            elif not name:
                print("You forgot to state the name using the --name CLI argument")
            elif not features:
                print("You forgot to state the features using the --features CLI argument")
        case "delete-by-id":
            result = delete_by_id(pk)
            print(result.deleted_count)
        case "delete-by-name":
            result = delete_by_name(name)
            print(result.deleted_count)
        case "delete-all":
            result = delete_all()
            print(result.deleted_count)
        case _:
            print('Wrong action')
