import subprocess
def generate_header(name, github_link, linkedin_link, email, phone):
    return f'''
\\begin{{description}}
    \\item 
        \\begin{{center}}
            \\textbf{{\\Huge \\scshape {name}}} \\\\ \\vspace{{8pt}}
            \\small 
            \\faIcon{{github}}
            \\href{{{github_link}}}
            {{\\underline{{{github_link.split('/')[-1]}}}}} $  $
            \\faIcon{{linkedin}}
            \\href{{{linkedin_link}}}{{\\underline{{{linkedin_link.split('/')[-1]}}}}} $  $
            \\faIcon{{envelope}}
            \\href{{mailto:{email}}}
            {{\\underline{{{email}}}}}
            \\faIcon{{phone}}
            \\href{{tel:{phone.replace('-', '')}}}{{\\underline{{{phone}}}}}
        \\end{{center}}
\\end{{description}}
'''

def generate_education(education_list):
    """
    education_list: list of dicts with keys:
        - institution
        - period
        - degree
        - bullets (optional)
    """
    content = "\\section{Education}\n\\resumeSubHeadingListStart\n"
    
    for edu in education_list:
        content += f'''
    \\resumeSubheading
      {{{edu['institution']}}}{{{edu['period']}}}
      {{{edu['degree']}}}{{{edu.get('bullets', '')}}}'''
    
    content += "\n\\resumeSubHeadingListEnd\n"
    return content

def generate_experience(experience_list):
    """
    experience_list: list of dicts with keys:
        - company
        - position
        - period
        - bullets (list of bullet points)
    """
    content = "\\section{Experience}\n\\resumeSubHeadingListStart\n"
    
    for exp in experience_list:
        content += f'''
    \\resumeProjectHeading
    {{\\textbf{{{exp['company']}}}\\vspace{{8pt}} $|$ \\footnotesize\\emph{{{exp['position']}}}}}{{{exp['period']}}}
    \\begin{{itemize}}'''
        
        for detail in exp['bullets']:
            content += f"\n        \\item {detail}"
        
        content += "\n    \\end{itemize}\n"
    
    content += "\\resumeSubHeadingListEnd\n"
    return content

def generate_projects(project_list):
    """
    project_list: list of dicts with keys:
        - name
        - technologies
        - period
        - bullets (list of bullet points)
        - github_link (optional)
    """
    content = "\\section{Personal Projects}\n\\resumeSubHeadingListStart\n"
    
    for proj in project_list:
        name = proj['name']
        if 'github_link' in proj:
            name = f"\\href{{{proj['github_link']}}}{{\\textbf{{{proj['name']}}}}}"
        else:
            name = f"\\textbf{{{proj['name']}}}"
            
        content += f'''
    \\resumeProjectHeading
    {{{name} $|$ \\footnotesize\\emph{{{proj['technologies']}}}}}{{{proj['period']}}}
    \\resumeItemListStart'''
        
        for detail in proj['bullets']:
            content += f"\n        \\resumeItem{{{detail}}}"
        
        content += "\n    \\resumeItemListEnd\n"
    
    content += "\\resumeSubHeadingListEnd\n"
    return content

def generate_skills(skills_dict):
    """
    skills_dict: dict with categories as keys and list of skills as values
    Example: {
        'Languages': ['Python', 'JavaScript', 'C++'],
        'Tools': ['Git', 'Docker', 'AWS']
    }
    """
    content = '''
\\section{Skills}
 \\begin{itemize}[leftmargin=0.15in, label={}]
    \\small{\\item{'''
    
    for category, skills in skills_dict.items():
        content += f"\n     \\textbf{{{category}}}{{: {', '.join(skills)} }}\\\\"
    
    content += '''
    }}
 \\end{itemize}
'''
    return content

def compile_resume(resume_data):
    """
    Compiles all resume sections into a single LaTeX file
    
    resume_data: dict containing all resume information with keys:
        - personal_info: dict with name, github_link, linkedin_link, email, phone
        - education: list of education entries
        - experience: list of experience entries
        - projects: list of project entries
        - skills: dict of skill categories and their lists
    """
    
    # Read the preamble
    with open('Resume/preamble.tex', 'r', encoding='utf-8') as f:
        preamble = f.read()
    
    # Generate all sections
    header = generate_header(**resume_data['personal_info'])
    education = generate_education(resume_data['education'])
    experience = generate_experience(resume_data['experience'])
    projects = generate_projects(resume_data['projects'])
    skills = generate_skills(resume_data['skills'])
    
    # Combine all sections
    full_document = f'''\\documentclass{{article}}
{preamble}

\\begin{{document}}

{header}

{education}

{experience}

{projects}

{skills}

\\end{{document}}
'''
    
    # Write to file
    with open('Resume/compiled.tex', 'w', encoding='utf-8') as f:
        f.write(full_document)
    
    return full_document

# Example usage:
# if __name__ == "__main__":
#     resume_data = {
#         "personal_info": {
#             "name": "Muhammad Talha",
#             "github_link": "https://github.com/Talha771",
#             "linkedin_link": "https://linkedin.com/in/tjbravo",
#             "email": "talha.j771@gmail.com",
#             "phone": "(214)-909-3357"
#         },
#         "education": [
#             {
#                 "institution": "Habib University",
#                 "period": "September 2020 - June 2024",
#                 "degree": "B.S. Computer Science"
#             },
#             {
#                 "institution": "Alpha College",
#                 "period": "September 2018 - August 2020",
#                 "degree": "A-Levels"
#             }
#         ],
#         "experience": [
#             {
#                 "company": "QLU",
#                 "position": "Software Developer (Full Stack: TypeScript/Node.js/Next.js/Express)",
#                 "period": "June 2024 -- October 2024",
#                 "bullets": [
#                     "Implemented a custom search algorithm using Cassandra on an at-rest encrypted database, ensuring security and efficiency.",
#                     "Singlehandedly deployed attachment functionality, managing the complete development lifecycle for front-end and back-end integration.",
#                     "Collaborated with design and product teams to create user-centric applications adhering to design principles and user flow requirements."
#                 ]
#             }
#         ],
#         "projects": [
#             {
#                 "name": "Yohsin Connect",
#                 "technologies": "Python, LangChain, FAISS, PyTorch, TensorFlow",
#                 "period": "2024",
#                 "bullets": [
#                     "Developed a Retrival Augmented Generation (RAG) chatbot to provide instant responses to inquiries from prospective students at Habib University.",
#                     "Integrated advanced LLM models using TensorFlow and PyTorch to understand and generate human-like responses.",
#                     "Utilized LangChain for streamlined implementation of chat functionalities and FAISS for efficient information retrieval from a large vector database/store of university related documents."
#                 ]
#             }
#         ],
#         "skills": {
#             "Languages": ["C/C++", "Python", "JavaScript", "HTML/CSS", "CUDA", "SQL", "LaTeX"],
#             "Tools": ["Git/GitHub", "Bash", "Yaml", "Docker", "FASTAPI"]
#         }
#     }
    
#     # Generate the complete resume
#     compile_resume(resume_data) 
#     # subprocess.run(['tectonic','compiled.tex'])
#     subprocess.run(['tectonic', 'Resume/compiled.tex'])

    

