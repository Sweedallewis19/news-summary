from pymongo import MongoClient
import datetime
from bson.objectid import ObjectId
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client['news_summary_db']
collection = db['summaries']

def save_summary(username, text, summary):
    collection.insert_one({
        "username": username,
        "original_text": text,
        "summary": summary,
        "timestamp": datetime.datetime.utcnow()
    })

def get_user_summaries(username):
    data = list(collection.find({"username": username}).sort("timestamp", -1))
    for item in data:
        item["_id"] = str(item["_id"])
    return data