# controllers/user.py
def getUser(id):
    return "getUser"

def getUsers():
    return "getUsers"

def patchUser(id):
    return "patchUser"

def addUser():
    return "addUser"

def deleteUser():
    return "deleteUser"

from pylatex import Document, NoEscape

def create_header(name, github, linkedin, number, email):
    header = f"""
    \\begin{{description}}
    \\item 
        \\begin{{center}}
            \\textbf{{\\Huge \\scshape {name}}} \\\\ \\vspace{{8pt}}
            \\small 
            \\faIcon{{github}}
            {{\\underline{{/{github}}}}} $  $
            \\faIcon{{linkedin}}
            {{\\underline{{in/{linkedin}}}}} $  $
            \\faIcon{{envelope}}
            {{\\underline{{{email}}}}} $  $
            \\faIcon{{phone}}
            {{\\underline{{{number}}}}}
        \\end{{center}}
    \\end{{description}}
    """
    return header
