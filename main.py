import getpass
import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
import json
from latex import create_resume


# Load environment variables from a .env file
load_dotenv()
tools = ['Git/GitHub', 'Bash', 'Yaml', 'Docker', 'FASTAPI']

# Retrieve the API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
prompt = PromptTemplate.from_template(
    '''
    Retrieve the skills that are purely about the tech stack from the job description {job_description} 
    Return it as a comma seperated string. 
    
    Example : "Javascript, Typescript, React"
    Do Not Add Slashes
    ' AWS/Google Cloud', ' SQL/ORM'
    '''
    )

f= open("JobDescription.txt", "r")
JOB_DESCRIPTION = f.read()
llm= OpenAI()
chain = prompt | llm
response = chain.invoke(
    {
        "job_description": JOB_DESCRIPTION,
        
    }
)
response = response.replace("\n","")
languages = response.split(",")
print(languages)
create_resume(languages,tools)