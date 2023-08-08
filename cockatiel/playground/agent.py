import os

from langchain.utilities import GoogleSerperAPIWrapper
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.llms import OpenAI

def main():
    user = os.getenv("USER")

    agent = initialize_agent(
        [
            Tool(
                name="Intermediate Answer",
                func=GoogleSerperAPIWrapper().run,
                description="useful for when you need to ask with search",
            )
        ], OpenAI(temperature=os.getenv("OPENAI_PARAM_TEMPERATURE")),
            agent=AgentType.SELF_ASK_WITH_SEARCH,
            verbose=os.getenv("GOOGLE_SERPER_API_PARAM_VERBOSE")
    )

    print('Chat: Hello, what can I do for you?')

    while True:
        user_input = input(f'{user}: ')

        if (user_input.lower() == 'exit' or 
            user_input.lower() == 'clear'):

            print('Leaving chat... bye')
            break
        
        print(ask(agent, user_input))

def ask(agent, user_input):
    try:
        response = agent.run(user_input)
    except Exception as e:
        response = str(e)

        if response.startswith('Could not parse LLM output:'):
            response = response.replace('Could not parse LLM output:', ' ', 1)

    return response

if __name__ == '__main__':
    main()