import os
import chromadb


class Database:

    def __init__(self, name) -> None:
        self._client = chromadb.Client()
        self._collection = self._client.create_collection(name)
    
    @property
    def client(self):
        return self._client
    
    @property
    def collection(self):
        return self._collection