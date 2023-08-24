import os

from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain import OpenAI


def main():
    user = os.getenv("USER")
    db = FAISS.from_documents(
        PyPDFLoader("resume.pdf").load_and_split(), 
        OpenAIEmbeddings()
    )

    chain = RetrievalQA.from_llm(llm=OpenAI(), retriever=db.as_retriever())

    print("Chat: Hello, I already know all the content of the doc, "+
          "I'm here to answer all your questions")

    while True:
        user_input = input(f'{user}: ')

        if (user_input.lower() == 'exit' or 
            user_input.lower() == 'clear'):

            print('Leaving chat... bye')
            break

        print(chain(user_input, return_only_outputs=True))

if __name__ == '__main__':
    main()