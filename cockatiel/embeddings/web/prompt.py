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
    url = "https://g1.globo.com/economia/noticia/2023/08/14/argentina-dolarizar-a-economia-crise-economica.ghtml"
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

    parser = argparse.ArgumentParser(description='Paepper.com Q&A')
    parser.add_argument('question', type=str, help='Quetion to be answered')
    args = parser.parse_args()

    with open("faiss_store.pkl", "rb") as f:
        store = pickle.load(f)

    chain = VectorDBQAWithSourcesChain.from_llm(
                llm=OpenAI(temperature=0), vectorstore=store)
    
    result = chain({"question": args.question})

    print(f"Answer: {result['answer']}")
    print(f"Sources: {result['sources']}")

if __name__ == '__main__':
    main()