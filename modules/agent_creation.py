from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_openai import OpenAI
from langchain.agents.agent_types import AgentType
import configparser

def create_agent(csv_file):
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    openai_api_key = config['OPENAI']['OPENAI_API_KEY']
    agent_verbose = config['AGENT']['VERBOSE']
    
    openai = OpenAI(
        api_key=openai_api_key,
        temperature=0,
        top_p=1,
        model='gpt-3.5-turbo-instruct'
    )

    agent = create_csv_agent(
        openai,
        csv_file,
        verbose=agent_verbose,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        allow_dangerous_code=True,
    )

    return agent

