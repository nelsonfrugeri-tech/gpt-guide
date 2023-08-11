import os

from database import Database
from sentence_transformers import SentenceTransformer


def query_collection(docs, query):
    return docs.collection.query(
        query_embeddings=[query],
        n_results=1
    )

def create_collection(docs, model):
    documents = []
    embeddings = []
    metadatas = []
    ids = []

    for index, data in enumerate(read_files_from_folder(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/txt'))
        ):
        documents.append(data['content'])
        embeddings.append(model.encode(data['content']).tolist())
        metadatas.append({'source': data['file_name']})
        ids.append(str(index + 1))

    docs.collection.add(
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids
    )

def read_files_from_folder(folder_path):
    file_data = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            with open(os.path.join(folder_path, file_name), 'r') as file:
                content = file.read()
                file_data.append({"file_name": file_name, "content": content})

    return file_data

def main():
    user = os.getenv("USER")
    docs = Database("docs_db")
    model = SentenceTransformer('paraphrase-MiniLM-L3-v2')

    create_collection(docs, model)

    while True:
        user_input = input(f'{user}: ')

        if (user_input.lower() == 'exit' or 
            user_input.lower() == 'clear'):

            print('Leaving chat... bye')
            break
        
        print(query_collection(docs, model.encode(user_input).tolist()))

if __name__ == '__main__':
    main()