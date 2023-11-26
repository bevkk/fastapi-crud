from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv, find_dotenv
import os

# Load environment variables from a .env file (typically used to store sensitive information)
load_dotenv(find_dotenv())
pw = os.environ.get("MONGODB_PW")
username = os.environ.get("MONGODB_USERNAME")
url = os.environ.get("MONGODB_URL")

uri = f"mongodb+srv://{username}:{pw}@{url}/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Access the "posts" database and "posts" collection within the database
db = client["posts"]
Collection = db["posts"]