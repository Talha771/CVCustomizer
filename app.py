from fastapi import FastAPI
from pydantic import BaseModel
from getLanguages import extractInformation
from fastapi.responses import JSONResponse, FileResponse
from createResume import create_resume
from fastapi.middleware.cors import CORSMiddleware
from Resume.resume_generator import compile_resume, createCompiledResume
from apit_types import CVItem

app = FastAPI()

global CVData
CVData = {
        "education": [
            {
                "institution": "Habib University",
                "period": "September 2020 - June 2024",
                "degree": "B.S. Computer Science"
            },
            {
                "institution": "Alpha College",
                "period": "September 2018 - August 2020",
                "degree": "A-Levels"
            }
        ],
        "experience": [
            {
                "company": "QLU",
                "position": "Software Developer (Full Stack: TypeScript/Node.js/Next.js/Express)",
                "period": "June 2024 -- October 2024",
                "bullets": [
                    "Implemented a custom search algorithm using Cassandra on an at-rest encrypted database, ensuring security and efficiency.",
                    "Singlehandedly deployed attachment functionality, managing the complete development lifecycle for front-end and back-end integration.",
                    "Collaborated with design and product teams to create user-centric applications adhering to design principles and user flow requirements."
                ]
            }
        ],
        "projects": [
            {
                "name": "Yohsin Connect",
                "technologies": "Python, LangChain, FAISS, PyTorch, TensorFlow",
                "period": "2024",
                "bullets": [
                    "Developed a Retrival Augmented Generation (RAG) chatbot to provide instant responses to inquiries from prospective students at Habib University.",
                    "Integrated advanced LLM models using TensorFlow and PyTorch to understand and generate human-like responses.",
                    "Utilized LangChain for streamlined implementation of chat functionalities and FAISS for efficient information retrieval from a large vector database/store of university related documents."
                ]
            }
        ],
    } 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins. You can specify a specific URL here if needed.
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allows all headers
)
class DescriptionModel(BaseModel):
    description: str

stored_description = None
known_languages = ['Python',"Typescript","Javascript", "C++", "Cuda","SQL","NOSQL"]

@app.post("/description")
async def root(data: DescriptionModel):
    global stored_description
    if type(data.description) != str:
        return JSONResponse(content={"error": "Invalid Input"}, status_code=500)
    stored_description = data.description
    print(stored_description)
    return JSONResponse(content="Job Description Received", status_code=200)

@app.get("/customCV")
async def return_custom_cv():
    global stored_description
    if stored_description is None:
        return JSONResponse(content={"error": "No Job Description Entered"}, status_code=500)
    
    # Extract languages and tools from the description
    languages = extractInformation(stored_description,known_languages)
    
    # Try to generate the resume
    try:
        create_resume(languages)
    except Exception as e:
        return JSONResponse(content={"error": f"Failed to create resume: {str(e)}"}, status_code=500)
    
    # Path to the generated resume
    resume_path = "resume.pdf"
    
    # Return the file as a response
    return FileResponse(resume_path, media_type="application/pdf", filename="custom_resume.pdf")


@app.post("/getCV")
async def createCV(data:CVItem):
    personal_info_dict = data.personalInfo.model_dump() # Convert to dictionary
    skills_dict = data.skills.model_dump()
    CVData["personal_info"] = personal_info_dict
    CVData["skills"] = skills_dict
    CVData["education"] = data.education.model_dump()["Education"]
    CVData['experience']= data.experience.model_dump()["Experience"]
    CVData["projects"] = data.projects.model_dump()["Projects"]
    compile_resume(CVData)
    cv = createCompiledResume()
    return FileResponse(cv, media_type="application/pdf", filename="custom_resume.pdf")
