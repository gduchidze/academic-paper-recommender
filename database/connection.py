from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from config.config import db_url

uri = db_url

client = MongoClient(uri, server_api=ServerApi('1'))
db = client["papersv2"]
collection = db["papers2"]