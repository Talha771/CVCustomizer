from pylatex import Document, Section, Itemize, Command, Description
from pylatex.utils import NoEscape
import subprocess
from Resume.header import generate_header



def create_skills_section(languages, tools):
    skills_section = Section('Skills')
    skills_list = Description()
    skills_list.add_item('', f"Languages: {', '.join(languages)}")
    skills_list.add_item('', f"Tools: {', '.join(tools)}")
    skills_section.append(skills_list)
    return skills_section

def create_section_from_file(file_path):
    file_path = "./Resume/"+file_path+".tex"
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return NoEscape(content)


def create_resume(skills):
    languages = skills[0]
    tools = skills[1]
    # Create the LaTeX document
    doc = Document()
    # Add preamble
    preamble = r"""
\usepackage{latexsym}
\usepackage[a4paper, total={6in, 8in}]{geometry}
\usepackage{titlesec}
\usepackage{marvosym}
\usepackage[usenames,dvipsnames]{color}
\usepackage{verbatim}
\usepackage{enumitem}
\usepackage{hyperref}
\usepackage{fancyhdr}
\usepackage[english]{babel}
\usepackage{tabularx}
\usepackage{xcolor}
\usepackage{fontawesome5}
% \include{Skills}
% -------------------- FONT OPTIONS --------------------
% sans-serif
% \usepackage[sfdefault]{roboto}
% \usepackage[sfdefault]{noto-sans}
% serif
% \usepackage{charter}

\pagestyle{fancy}
\fancyhf{} % clear all header and footer fields
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% Adjust margins
\addtolength{\oddsidemargin}{-0.5in}
\addtolength{\evensidemargin}{-0.5in}
\addtolength{\textwidth}{1in}
\addtolength{\topmargin}{-1in} % Default was -.5in
\addtolength{\textheight}{1.0in}

\urlstyle{same}

\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}

% Section formatting
\titleformat{\section}{
  \vspace{-5pt}\scshape\raggedright\large
}{}{0em}{}[\color{black}\titlerule \vspace{-5pt}]

% Subsection formatting
\titleformat{\subsection}{
  \vspace{-4pt}\scshape\raggedright\large
}{\hspace{-.15in}}{0em}{}[\color{black}\vspace{-8pt}]

% Ensure that generate pdf is machine readable/ATS parsable

% -------------------- CUSTOM COMMANDS --------------------
\newcommand{\resumeItem}[1]{
  \item\small{
    {#1 \vspace{-2pt}}
  }
}

\newcommand{\resumeSubheading}[4]{
  \vspace{-2pt}\item
    \begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}
      \textbf{#1} & #2 \\
      \textit{\small#3} & \textit{\small #4} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubSubheading}[2]{
    \item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
      \textit{\small#1} & \textit{\small #2} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeProjectHeading}[2]{
    \item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
      \small#1 & #2 \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubItem}[1]{\resumeItem{#1}\vspace{-4pt}}
\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.15in, label={}]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeItemListStart}{\begin{itemize}}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-5pt}}

\renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}

\setlength{\footskip}{4.08003pt}
"""
    sections = ['education','experience','projects']
    tex_header = generate_header(
    name="John Doe",
    github_link="https://github.com/johndoe",
    linkedin_link="https://www.linkedin.com/in/johndoe",
    email="johndoe@example.com",
    phone="+1-234-567-8901"
)
    doc.preamble.append(NoEscape(preamble))
    # print(tex_header)
    doc.append(NoEscape(tex_header))
    for section in sections: 
        doc.append(create_section_from_file(section))
    doc.append(create_skills_section(languages, tools))

    doc.generate_tex("resume")  
    subprocess.run(["tectonic", "resume.tex"])


# create_resume([[],[]])