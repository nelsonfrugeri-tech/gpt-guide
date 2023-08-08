import os

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
    SystemMessage
)

def main():
    user = os.getenv("USER")
    chat = ChatOpenAI(temperature=os.getenv("OPENAI_PARAM_TEMPERATURE"))
    batch_messages = [[SystemMessage(
        content="You are a software development and engineering assistant")]]

    print('Chat: Hello, what can I do for you?')

    while True:
        user_input = input(f'{user}: ')

        if user_input.lower() == 'exit':
            print('Leaving chat... bye')
            break

        batch_messages[0].append(HumanMessage(content=user_input))

        result = chat.generate(batch_messages)

        print(result.generations[0][0].text)
        print(result.llm_output['token_usage'])

if __name__ == '__main__':
    main()