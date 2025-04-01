from pydantic import BaseModel
from typing import List


class EducationInstance(BaseModel):
    institution : str
    period:str
    degree:str 
class Education(BaseModel):
    Education:List[EducationInstance]
class ExperienceInstance(BaseModel):
    company:str
    position:str 
    period: str 
    bullets: List[str]
class Experience(BaseModel):
    Experience: List[ExperienceInstance]
class ProjectInstance(BaseModel):
      name:str
      technologies:List[str]
      period: str
      bullets: List[str]
class Projects(BaseModel):
    Projects : List[ProjectInstance]

class personal_info(BaseModel):
    name: str
    github_link: str
    linkedin_link: str
    email: str  # Ensures valid email format
    phone: str

class Skills(BaseModel):
    languages: List[str]
    skills : List[str]

class CVItem(BaseModel):
    personalInfo:personal_info
    education:Education
    experience : Experience
    projects : Projects 
    skills:Skills
