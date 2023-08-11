import os

from database import Database


def query_collection(docs_collection, query):
    return docs_collection.collection.query(
        query_texts=[query],
        n_results=1
    )

def create_collection(docs_collection):
    documents = []
    metadatas = []
    ids = []

    for index, data in enumerate(read_files_from_folder(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/txt'))
        ):
        documents.append(data['content'])
        metadatas.append({'source': data['file_name']})
        ids.append(str(index + 1))

    docs_collection.collection.add(
        documents=documents,
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
    docs_collection = Database("docs_db")

    create_collection(docs_collection)

    while True:
        user_input = input(f'{user}: ')

        if (user_input.lower() == 'exit' or 
            user_input.lower() == 'clear'):

            print('Leaving chat... bye')
            break
        
        print(query_collection(docs_collection, user_input))

if __name__ == '__main__':
    main()