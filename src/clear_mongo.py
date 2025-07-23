from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client.test_results_db
collection = db.results

deleted_count = collection.delete_many({}).deleted_count
print(f"🧹 Cleared {deleted_count} old test records.")
