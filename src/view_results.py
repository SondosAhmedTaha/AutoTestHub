# src/view_results.py

import os
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client.test_results_db
collection = db.results

print("\n📋 Last 10 test results:")
for doc in collection.find().sort("timestamp", -1).limit(10):
    print(f"🧪 {doc['test_name']} — {doc['status']} at {doc['timestamp']}")
