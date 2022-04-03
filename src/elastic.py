"""Integration with ElasticSearch."""
from elasticsearch import Elasticsearch

from src import configurations


class Elastic:

    def __init__(self, host: str = f"http://{configurations.ELASTIC_HOST}:{configurations.ELASTIC_PORT}"):
        self.es_connection = Elasticsearch(hosts=host)
        self.posts_index = "posts"
        self.comments_index = "comments"

    def info(self):
        return self.es_connection.info()
