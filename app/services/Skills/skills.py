# controllers/skills.py
from pylatex import Section,Description
def getSkill(id):
    return "getSkill"

def getSkills():
    return "getSkills"

def patchSkill(id):
    return "patchSkill"

def addSkill():
    return "addSkill"

def deleteSkill():
    return "deleteSkill"

def create_skills_section(languages, tools):
    skills_section = Section('Skills')
    skills_list = Description()
    skills_list.add_item('', f"Languages: {', '.join(languages)}")
    skills_list.add_item('', f"Tools: {', '.join(tools)}")
    skills_section.append(skills_list)
    return skills_section
