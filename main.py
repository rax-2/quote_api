from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv
from random import randint

load_dotenv()
mongo_uri = getenv("URI")

client = MongoClient(mongo_uri)
# print(client.admin.command("ping"))


db = client["quote_data"]
coll = db["quote"]

# coll.insert_one({"uname": "666"})

ids = []
for id in coll.find({}, {"_id": 1}):
    # print(id)
    ids.append(id["_id"])

# print(len(ids))


def getRandomQuote(ids: list, coll=coll):
    random_id = ids[randint(0, len(ids))]
    print(random_id)
    obj = coll.find({"_id": random_id})
    quote = None
    for data in obj:
        # print(data)
        quote = data
    # print(quote)
    if quote.get("quote") and quote.get("author"):
        return {
            "quote": quote["quote"],
            "author": quote["author"],
            "_id": str(quote["_id"]),
        }
    else:
        return {"error": "quote not found"}


# print(getRandomQuote(ids=ids))
from fastapi import FastAPI

root = FastAPI()


@root.get("/")
def home():
    return {"hello": "user", "welcome": "quote api"}


@root.get("/quote")
def getQuote():
    return getRandomQuote(ids=ids)


@root.get("/status")
def status():
    return "i'am alive"
