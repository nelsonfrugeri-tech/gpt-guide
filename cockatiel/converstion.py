import os
from langchain import OpenAI, ConversationChain

def main():
    chat = "Assistant"
    user = os.getenv("USER")

    conversation = ConversationChain(
        llm=OpenAI(temperature=os.getenv('OPENAI_PARAM_TEMPERATURE')), 
        verbose=os.getenv('CONVERSATION_CHAIN_PARAM_VERBOSE')
    )

    print(f'{chat}: Hello, what can I do for you?')

    while True:
        user_input = input(f'{user}: ')

        if user_input.lower() == 'exit':
            print('Leaving chat... bye')
            break

        print(chat + conversation.predict(input=user_input))

if __name__ == '__main__':
    main()