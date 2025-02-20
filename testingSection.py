
from pylatex import Document, Subsection, NoEscape, Tabular, Table,Itemize
from app.services.Education.education import createEducationLatex
from app.services.User.user import create_header 
from app.services.Experiences.experience import createExperienceLatex,createSection
from app.services.Projects.projects import createProjectLatex
from app.services.Skills.skills import create_skills_section

experience = createExperienceLatex(
    company="Acme Corp",
    designation = "Full Stack Engineer",
    stack = ["NodeJs","Express","React","Typescript"],
    start="January 2022",
    bullets=[
        "Developed scalable web applications",
        "Collaborated with cross-functional teams",
        "Implemented RESTful APIs"
    ]
)
experience2 = createExperienceLatex(
    company="Tech Innovators Inc.",
    designation="Software Engineer",
    stack=["Python", "Django", "PostgreSQL", "Docker"],
    start="June 2020",
    end="December 2021",
    bullets=[
        "Designed and developed RESTful APIs using Django",
        "Optimized database queries for better performance",
        "Deployed applications using Docker and Kubernetes"
    ]
)

project1 = createProjectLatex(
    company="Yohsin Connect",
    stack=["Python", "LangChain", "FAISS", "PyTorch", "TensorFlow"],
    bullets=[
        "Developed a Retrieval Augmented Generation (RAG) chatbot to provide instant responses to inquiries from prospective students at Habib University.",
        "Integrated advanced LLM models using TensorFlow and PyTorch to understand and generate human-like responses.",
        "Utilized LangChain for streamlined implementation of chat functionalities and FAISS for efficient information retrieval from a large vector database/store of university-related documents."
    ],
    start="2024"
)

project2 = createProjectLatex(
    company="Personal Home Lab and Smart Home Setup",
    stack=["YAML", "Python", "Docker"],
    bullets=[
        "Configured diverse services: Jellyfin, Home Assistant, Transmission Daemon with public access.",
        "Managed Docker containers for efficient deployment."
    ],
    start="Ongoing"
)

project3 = createProjectLatex(
    company="BomberMan Clone",
    stack=["C++", "SDL2", "Sprite Animations", "Polymorphism"],
    bullets=[
        "Recreated the famous Bomberman game in C++ using SDL2, including sprite animations and custom game mechanics.",
        "Implemented OOP design patterns and polymorphism."
    ],
    start="December 2021"
)
doc = Document()
doc.preamble.append(layout_adjustments)
doc.preamble.append(NoEscape(r'\usepackage{fontawesome5} \usepackage{titlesec} \usepackage{xcolor} % Ensures color functionality'))  # Ensure FontAwesome icons work
languages = ["Python", "JavaScript", "C++", "SQL"]
tools = ["Docker", "PostgreSQL", "Git", "AWS", "Kubernetes"]


doc.append(NoEscape(r"\vspace{-10mm}"))
header = NoEscape(create_header("Muhammad Talha", "Wolfbiter771", "tjbravo", "2149093357", "talha.j771@gmail.com"))
Education = createEducationLatex("Habib University","Bachelors of Computer Science","2020","2024")
Education2 = createEducationLatex("Alpha College","Advanced Level GCSE","2018","2020")
skills_section = create_skills_section(languages, tools)
educationSection = createSection("Education")
experienceSection = createSection("Experience")
projectSection = createSection("Projects")
doc.append(header)
doc.append(educationSection)
doc.append(Education)
doc.append(Education2)
doc.append(skills_section)
doc.append(experienceSection)
doc.append(experience)
doc.append(experience2)
doc.append(projectSection)
doc.append(project1)
doc.append(project2)
doc.append(project3)
doc.generate_tex("trial.tex")
doc.generate_pdf("trial")