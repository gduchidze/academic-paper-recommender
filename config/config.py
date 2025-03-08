import logging, os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

db_url = os.getenv('DATABASE_URL')
model = SentenceTransformer('all-MiniLM-L6-v2')