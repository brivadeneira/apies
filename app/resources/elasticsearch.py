import os

from dotenv import load_dotenv
from elasticsearch import AsyncElasticsearch

load_dotenv()

es_host = os.getenv("ES_HOST")
es_mon_index = os.getenv("ES_MON_INDEX")
es_text_index = os.getenv("ES_MON_INDEX")

es = AsyncElasticsearch(es_host)
