import os
from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client.test_results_db
collection = db.results

def show_all():
    results = list(collection.find().sort("test_name"))
    if not results:
        print("No test results found.")
        return

    timestamp = results[0].get("timestamp")
    print(f"\n📋 Showing results for the latest test run at {timestamp.strftime('%Y-%m-%d %H:%M:%S')}:")

    for test in results:
        name = test.get("test_name", "<unknown>")
        status = test.get("status", "?")
        duration = test.get("duration", 0.0)
        symbol = "✔" if status == "PASS" else ("✘" if status == "FAIL" else "❓")
        print(f"  {symbol} {name} — {status} ({duration:.2f}s)")

if __name__ == "__main__":
    show_all()
