
import os
from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client.test_results_db
collection = db.results

# Fetch the last 10 results, sorted by timestamp descending
results = list(collection.find().sort("timestamp", -1).limit(50))

# Group tests by timestamp (i.e., test run)
from collections import defaultdict

grouped = defaultdict(list)
for r in results:
    key = r.get("timestamp", "unknown").strftime("%Y-%m-%d %H:%M:%S") if isinstance(r.get("timestamp"), datetime) else r.get("timestamp")
    grouped[key].append(r)

print("\n📋 Test Run History (Grouped by Timestamp):")
for timestamp in sorted(grouped.keys(), reverse=True):
    print(f"\n🕒 Run at {timestamp}:")
    for test in grouped[timestamp]:
        name = test.get("test_name", "<unknown>")
        status = test.get("status", "?")
        duration = test.get("duration", 0.0)
        symbol = "✔" if status == "PASSED" else ("✘" if status == "FAILED" else "❓")
        print(f"  {symbol} {name} — {status} ({duration:.2f}s)")
