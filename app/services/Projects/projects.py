from pylatex import Document, Subsection, NoEscape, Tabularx, Table,Itemize
from pylatex.utils import italic,bold

def getProject(id):
    return "getProject"

def getProjects():
    return "getProjects"

def patchProject(id):
    return "patchProject"

def addProject():
    return "addProject"

def deleteProject():
    return "deleteProject"


def create_stack(stackList):
    temp =' ('
    for i in range(len(stackList)-1):
        temp+=stackList[i]+"/"
    temp+=stackList[-1]
    temp += ')'
    return temp
 
def createProjectLatex(company,stack,bullets, start, end='Current'):
    experience = Subsection("", numbering=False)
    experience.append(NoEscape(r"\vspace{-4mm}"))

    stack = create_stack(stack)
    date_range = start + " — " + end  
    table = Table()
    tabular = Tabularx('cXr',width=3) 
    tabular.add_row((bold(company + " |"), italic(stack), date_range))
    experience.append(tabular)
    itemize=Itemize()
    for bullet in bullets:
        itemize.add_item(bullet)
    experience.append(itemize)
    return experience
