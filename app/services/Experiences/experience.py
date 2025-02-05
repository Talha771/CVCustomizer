from pylatex import Document, Subsection, NoEscape, Tabular, Table,Itemize,Section
from pylatex.utils import italic,bold

def getExperience(id):
    return "getExperience"

def getExperiences():
    return "getExperiences"

def patchExperience(id):
    return "patchExperience"

def addExperience():
    return "addExperience"

def deleteExperience():
    return "deleteExperience"

def create_designation_stack(designation,stackList):
    temp = designation
    temp += ' ('
    for i in range(len(stackList)-1):
        temp+=stackList[i]+"/"
    temp+=stackList[-1]
    temp += ')'
    return temp
 
def createSection(name):
    section = Section(name,numbering=False)
    return section

def createExperienceLatex(company, designation, stack,bullets, start, end='Current'):
    experience = Subsection("", numbering=False)
    designation_stack = create_designation_stack(designation, stack)
    date_range = start + " — " + end  
    table = Table()
    tabular = Tabular('c|cl') 
    tabular.add_row((bold(company), italic(designation_stack), date_range))
    experience.append(tabular)
    itemize=Itemize()
    for bullet in bullets:
        itemize.add_item(bullet)
    experience.append(itemize)
    return experience

