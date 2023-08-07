import os

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

def prompt_template():
    prompt = PromptTemplate(
        input_variables=["product"],
        template="What is a good name for a company that makes {product}?",
    )

    return prompt.format(product="colorful socks")

def prompt_basic(prompt_template=""):
    chat = ChatOpenAI(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        model_name=os.getenv("OPENAI_MODEL"),
        temperature=0.9,
        max_tokens=15,
        n=1,
    )
    
    print(chat.predict(prompt_template))

if __name__ == "__main__":
    prompt_basic(prompt_template())