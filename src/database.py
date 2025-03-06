from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from config.main import db_url
from sentence_transformers import SentenceTransformer
from config.main import logger
uri = db_url

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    logger.info("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    logger.warning(e)

db = client["research_papers"]
collection = db["research_papers"]