from pylatex import Document, Section, Command
from pylatex.utils import italic, NoEscape

def add_education(doc, university, degree, start_date, end_date):
    # University Name with date aligned to the right
    doc.append(NoEscape(r'\textbf{' + university + '}'))
    doc.append(NoEscape(r'\hfill'))
    doc.append(NoEscape(start_date + " - " + end_date))
    doc.append("\n")
    
    # Italicized degree
    doc.append(NoEscape(r'\textit{' + degree + '}'))
    doc.append("\n\n")

# Example usage
doc = Document()
add_education(doc, "Habib University", "B.S. Computer Science", "September 2020", "June 2024")
doc.generate_pdf("education_section", clean_tex=False)
