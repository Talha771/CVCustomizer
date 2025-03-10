from pylatex import Document, Section, Tabularx, NoEscape, Itemize
from pylatex.utils import italic, bold

def create_experience_latex(company, designation, stack, bullets, start, end="Current"):
    format = r'''
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
      \textit{\small+}} & \textit{\small #2} \\
    \end{tabular*}\vspace{-7pt}'''
    