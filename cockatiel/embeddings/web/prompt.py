import os
import requests
import pickle
import argparse

from bs4 import BeautifulSoup
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain import OpenAI
from langchain.chains import VectorDBQAWithSourcesChain

def extract_text_from(url):
    return '\n'.join(line for line in (line.strip() for line in BeautifulSoup(
        requests.get(url).text,
        features="html.parser"
    ).get_text().splitlines()) if line)

def main(): 
    pages = []
    user = os.getenv("USER")
    url = os.getenv("URL")
    pages.append({'text': extract_text_from(url), 'source': url})

    text_splitter = CharacterTextSplitter(chunk_size=1500, separator="\n")
    docs, metadatas = [], []

    for page in pages:
        splits = text_splitter.split_text(page['text'])
        docs.extend(splits)
        metadatas.extend([{"source": page['source']}] * len(splits))
        print(f"Split {page['source']} into {len(splits)} chunks")

    store = FAISS.from_texts(docs, OpenAIEmbeddings(), metadatas=metadatas)
    
    with open("faiss_store.pkl", "wb") as f:
        pickle.dump(store, f)

    with open("faiss_store.pkl", "rb") as f:
        store = pickle.load(f)

    chain = VectorDBQAWithSourcesChain.from_llm(
                llm=OpenAI(temperature=0), vectorstore=store)
    
    print("Chat: Hello, I already know all the content of the web site, "+ 
          "I'm here to answer all your questions")

    while True:
        user_input = input(f'{user}: ')

        if (user_input.lower() == 'exit' or 
            user_input.lower() == 'clear'):

            print('Leaving chat... bye')
            break

        print(chain({"question": user_input})['answer'])

if __name__ == '__main__':
    main()