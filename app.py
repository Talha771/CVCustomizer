from fastapi import FastAPI
from pydantic import BaseModel
from getLanguages import extractInformation
from fastapi.responses import JSONResponse, FileResponse
from createResume import create_resume

app = FastAPI()

class DescriptionModel(BaseModel):
    description: str

stored_description = None

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
    languages = extractInformation(stored_description)
    
    # Try to generate the resume
    try:
        create_resume(languages)
    except Exception as e:
        return JSONResponse(content={"error": f"Failed to create resume: {str(e)}"}, status_code=500)
    
    # Path to the generated resume
    resume_path = "resume.pdf"
    
    # Return the file as a response
    return FileResponse(resume_path, media_type="application/pdf", filename="custom_resume.pdf")
