import os
from pymongo import MongoClient
from datetime import datetime

# Get connection string from environment
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client.test_results_db
collection = db.results

def save_result(test_name, status, duration):
    collection.insert_one({
        "test_name": test_name,
        "status": status,
        "duration": duration,
        "timestamp": datetime.now()
    })
