from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb+srv://sasanksaimanda:Sasank%40123@cluster0.n3cyl.mongodb.net/")  # Replace with your MongoDB URI
db = client['visit_counter']
collection = db['visits']

# Initialize visit count if not present
if collection.count_documents({}) == 0:
    collection.insert_one({"count": 0})

@app.route("/")
def index():
    # Increment visit count
    visit_data = collection.find_one()
    new_count = visit_data['count'] + 1
    collection.update_one({}, {"$set": {"count": new_count}})
    
    # Render the webpage with visit count
    return render_template("index.html", count=new_count)

if __name__ == "__main__":
    app.run(debug=True)
