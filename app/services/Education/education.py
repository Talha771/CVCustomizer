from pylatex import Document, Section, Command,Subsection
from pylatex.utils import italic, NoEscape


def getEducation(id):
    return ("getEducation")

def getEducations(id):
    return ("getEducations")

def patchEducation(id):
    # input : all fields to be updated
    return ("patchEducation")

def addEducation():
    return ("addEducation")

def deleteEducation():
    return ("deleteEducation")

def createEducationLatex(institution, program, start_date, end_date="Ongoing"):
    education_subsection = Subsection("",numbering=False)
    education_subsection.append(NoEscape(r'\noindent'))
    education_subsection.append(NoEscape(r'\textbf{' + institution + '}'))
    education_subsection.append(NoEscape(r'\hfill'))
    education_subsection.append(NoEscape(start_date + " - " + end_date))
    education_subsection.append("\n")
    education_subsection.append(NoEscape(r'\textit{' + program + '}'))
    education_subsection.append("\n\n")
    return education_subsection

