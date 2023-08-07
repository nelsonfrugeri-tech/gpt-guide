import os

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

def main():
    llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

    prompt = PromptTemplate.from_template("What is a good name for a company that makes {product}?")
    
    print(llm.predict(prompt.format(product="colorful socks")))

if __name__ == "__main__":
    main()