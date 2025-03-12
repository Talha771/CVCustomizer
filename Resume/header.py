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

