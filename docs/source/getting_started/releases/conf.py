import os

root_doc = 'release_note_572'

latex_elements = {
    'papersize': 'a4paper',
    'classoptions': ',oneside',
    'preamble': r'''
    \usepackage{titlesec}
    \setcounter{secnumdepth}{2}
    \usepackage{hyperref}
    ''',
}

latex_documents = [
    (root_doc,
     'release_note_572.tex',
     'Release note for version 5.7.2',
     "Meso-NH's support",
     'article',
     False),
]
