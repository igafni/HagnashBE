from elasticsearch import Elasticsearch
from typing import Dict

CONNECTION_STRING = "https://site:7862527dfefd4ee35458c6498900a16f@gimli-eu-west-1.searchly.com"
API_KEY = "7862527dfefd4ee35458c6498900a16f"


class ElasticAdapter(object):
    def __init__(self, connection_string: str, api_key: str, index: str):
        self.connection_string = connection_string
        self.api_key = api_key
        self.index = index
        self.es = None

    def connect(self):
        self.es = Elasticsearch(self.connection_string, api_key=self.api_key)

    def close(self):
        self.es.close()

    def index_document(self, document: Dict):
        self.es.index(index=self.index, body=document)

    def search_document(self, query: Dict):
        return self.es.search(index=self.index, body=query)

    def delete_document(self, document: Dict):
        self.es.delete_by_query(index=self.index, body=document)
