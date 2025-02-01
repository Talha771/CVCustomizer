import getpass
import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
import json



# Load environment variables from a .env file

# f= open("JobDescription.txt", "r")
# JOB_DESCRIPTION = f.read()

load_dotenv()
tools = ['Git/GitHub', 'Bash', 'Yaml', 'Docker', 'FASTAPI']

# Retrieve the API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
prompt = PromptTemplate.from_template(
    '''
    Retrieve the skills that are purely about the tech stack from the job description {job_description} 
    Return it as a comma seperated string. Limit to top 10 skills
    
    Example : "Javascript, Typescript, React"
    Do Not Add Slashes
    ' AWS/Google Cloud', ' SQL/ORM'
    '''
    )

llm= OpenAI()
def extract_information(JOB_DESCRIPTION):
    chain = prompt | llm
    response = chain.invoke(
        {
            "job_description": JOB_DESCRIPTION,
            
        }
    )
    response = response.replace("\n","")
    languages = response.split(",")
    return [languages,tools]