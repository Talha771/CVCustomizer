
from pylatex import Document, Subsection, NoEscape, Tabular, Table,Itemize
# from pylatex.utils import italic,bold


# # # def create_stack(stackList):
# # #     temp = ' ('
# # #     for i in range(len(stackList)-1):
# # #         temp+=stackList[i]+"/"
# # #     temp+=stackList[-1]
# # #     temp += ')'
# # #     return temp
 
# # # def createProjectLatex(company,stack,bullets, start, end='Current'):
# # #     experience = Subsection("", numbering=False)
# # #     stack = create_stack(stack)
# # #     date_range = start + " — " + end  
# # #     table = Table()
# # #     tabular = Tabular('c|cl') 
# # #     tabular.add_row((bold(company), italic(stack), date_range))
# # #     experience.append(tabular)
# # #     itemize=Itemize()
# # #     for bullet in bullets:
# # #         itemize.add_item(bullet)
# # #     experience.append(itemize)
# # #     return experience
# # # # # Create the document



# # # doc = Document()

# # # # Add the experience subsection
# # # doc.append(createProjectLatex("QLU",['Javascript','TypeScript','NodeJS'],["Developed scalable web applications","Collaborated with cross-functional teams","Implemented RESTful APIs"],"June 2024"))

# # # # Generate the PDF
# # # doc.generate_pdf("experience2")


# # from pylatex import Document, NoEscape
# # from pylatex.utils import bold

# # def create_heading(
# #     name="Muhammad Talha",
# #     github_icon=r'\faIcon{github}',
# #     github_url="https://github.com/Talha771",
# #     github_handle="/Talha771",
# #     linkedin_icon=r'\faIcon{linkedin}',
# #     linkedin_url="https://linkedin.com/in/tjbravo",
# #     linkedin_handle="in/tjbravo",
# #     email_icon=r'\faIcon{envelope}',
# #     email_url="mailto:talha.j771@gmail.com",
# #     email_address="talha.j771@gmail.com",
# #     phone_icon=r'\faIcon{phone}',
# #     phone_url="tel:0012149093357",
# #     phone_number="(214)-909-3357"
# # ):
    
# #     header_template = r"""
# # \begin{description}
# #     \item 
# #         \begin{center}
# #             \textbf{\Huge \scshape %(name)s} \\ \vspace{8pt}
# #             \small 
# #             %(github_icon)s
# #             \href{%(github_url)s}{\underline{%(github_handle)s}} $  $
# #             %(linkedin_icon)s
# #             \href{%(linkedin_url)s}{\underline{%(linkedin_handle)s}} $  $
# #             %(email_icon)s
# #             \href{%(email_url)s}{\underline{%(email_address)s}}
# #             %(phone_icon)s
# #             \href{%(phone_url)s}{\underline{%(phone_number)s}}
# #         \end{center}
# # \end{description}
# # """
# #     # Format the template with the provided variables
# #     header = header_template % {
# #         "name": name,
# #         "github_icon": github_icon,
# #         "github_url": github_url,
# #         "github_handle": github_handle,
# #         "linkedin_icon": linkedin_icon,
# #         "linkedin_url": linkedin_url,
# #         "linkedin_handle": linkedin_handle,
# #         "email_icon": email_icon,
# #         "email_url": email_url,
# #         "email_address": email_address,
# #         "phone_icon": phone_icon,
# #         "phone_url": phone_url,
# #         "phone_number": phone_number
# #     }
# #     return NoEscape(header)

# # # Create the document
# # doc = Document()

# # # Append the header to the document using the default values
# # doc.append(create_heading())

# # # Alternatively, you can override any of the default values:
# # # doc.append(create_heading(
# # #     name="John Doe",
# # #     github_url="https://github.com/JohnDoe",
# # #     github_handle="/JohnDoe",
# # #     linkedin_url="https://linkedin.com/in/JohnDoe",
# # #     linkedin_handle="in/JohnDoe",
# # #     email_address="john.doe@example.com",
# # #     phone_number="(123)-456-7890"
# # # ))

# # # Generate the PDF (set clean_tex=False to keep the .tex file for debugging)
# # doc.generate_pdf("heading", clean_tex=False)


# # header

# # Create the document
# doc = Document()
# doc.preamble.append(NoEscape(r'\usepackage{fontawesome5}'))  # Ensure FontAwesome icons work
# doc.append(NoEscape(create_header("Muhammad Talha", "Wolfbiter771", "tjbravo", "2149093357", "talha.j771@gmail.com")))

# # Generate the PDF
# pdf_filename = doc.generate_pdf("header", clean_tex=False)

# if pdf_filename:
#     print(f"PDF generated successfully: {pdf_filename}")
# else:
#     print("PDF generation failed. Check for LaTeX errors in resume.tex.")

from app.services.Education.education import createEducationLatex
from app.services.User.user import create_header 
from app.services.Experiences.experience import createExperienceLatex,createSection
from app.services.Projects.projects import createProjectLatex
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
doc.preamble.append(NoEscape(r'\usepackage{fontawesome5} \usepackage{titlesec} \usepackage{xcolor} % Ensures color functionality'))  # Ensure FontAwesome icons work
doc.append(NoEscape(r'''
% Section formatting
\titleformat{\section}{
  \vspace{-5pt}\scshape\raggedright\large
}{}{0em}{}[\color{black}\titlerule \vspace{-5pt}]

% Subsection formatting
\titleformat{\subsection}{
  \vspace{-4pt}\scshape\raggedright\large
}{\hspace{-.15in}}{0em}{}[\color{black}\vspace{-8pt}]
'''))

header = NoEscape(create_header("Muhammad Talha", "Wolfbiter771", "tjbravo", "2149093357", "talha.j771@gmail.com"))
Education = createEducationLatex("Habib University","Bachelors of Computer Science","2020","2024")
Education2 = createEducationLatex("Alpha College","Advanced Level GCSE","2018","2020")

educationSection = createSection("Education")
experienceSection = createSection("Experience")
projectSection = createSection("Projects")
doc.append(header)
doc.append(educationSection)
doc.append(Education)
doc.append(Education2)
doc.append(experienceSection)
doc.append(experience)
doc.append(experience2)
doc.append(projectSection)
doc.append(project1)
doc.append(project2)
doc.append(project3)
doc.generate_pdf("trial")