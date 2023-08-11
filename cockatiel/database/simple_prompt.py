from database import Database


def simple():
    db = Database("simple_db")

    db.collection.add(
        documents=["This is a document about eletric cars", "This is a document about combustion cars", "This is a document about combustion motorcycles"],
        metadatas=[{"category": "eletric"}, {"category": "combustion"}, {"category": "combustion"}],
        ids=["1", "2","3"]
    )

    results = db.collection.query(
        query_texts=["combustion"],
        n_results=2
    )

    print(results)

if __name__ == '__main__':
    simple()