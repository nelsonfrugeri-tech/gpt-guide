import os
import sys

from langchain.agents import AgentType
from langchain.agents import initialize_agent
from langchain.agents.agent_toolkits.github.toolkit import GitHubToolkit
from langchain.llms import OpenAI
from langchain.utilities.github import GitHubAPIWrapper
from langchain.chat_models import ChatOpenAI

def main():

    agent = initialize_agent(
        tools = GitHubToolkit.from_github_api_wrapper(GitHubAPIWrapper()).get_tools(),
        llm = ChatOpenAI(temperature=os.getenv("AGENT_TEMPERATURE"), model=os.getenv("AGENT_MODEL")), 
        agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose = True,
        agent_kwargs={
            'prefix': """You are a software engineer specializing in Java and you have to create an automated test class 
                by reading a class that contains API call business rules."""
        },
    )

    agent.run(f"Run all the steps in the issue {sys.argv[1]}")

if __name__ == '__main__':
    main()