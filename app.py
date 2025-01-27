from flask import Flask, render_template, request
from pymongo import MongoClient
from datetime import datetime
import os

app = Flask(__name__)

# Connect to MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://sasanksaimanda:Sasank%40123@cluster0.n3cyl.mongodb.net/")
client = MongoClient(MONGO_URI)
db = client['testing']
collection = db['testing']

@app.route("/")
def index():
    # Save a new visit with details in the database
    visit = {
        "ip_address": request.remote_addr,  # Get the user's IP address
        "user_agent": request.headers.get('User-Agent'),  # Get the user's browser details
        "timestamp": datetime.now()  # Save the current timestamp
    }
    collection.insert_one(visit)  # Save the visit to the database

    # Count total visits
    total_visits = collection.count_documents({})

    return render_template("index.html", count=total_visits)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
