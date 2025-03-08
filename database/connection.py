from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from config.main import db_url

uri = db_url

client = MongoClient(uri, server_api=ServerApi('1'))
db = client["papersv2"]
collection = db["papers2"]

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)