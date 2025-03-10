# Adapt this configuration file to new READTHEDOCS

import os

# Define the canonical URL if you are using a custom domain on Read the Docs
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")

# Tell Jinja2 templates the build is running on Read the Docs
if os.environ.get("READTHEDOCS", "") == "True":
    if "html_context" not in globals():
        html_context = {}
    html_context["READTHEDOCS"] = True

# Configuration file for the Sphinx documentation builder.

# -- Project information

project   = 'Meso-NH'
copyright = '2025, Meso-NH\'s support'
author    = 'Meso-NH\'s support'

release = '0.0'
version = '0.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.bibtex',
]

bibtex_bibfiles        = ['references.bib']
bibtex_default_style   = 'unsrt'
bibtex_reference_style = 'author_year'

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'
#html_theme = 'cloud'
#html_theme = 'bootstrap'
#html_theme = 'sphinx_book_theme'

html_logo = 'logos/LogoMesoNH-small.png'

#html_static_path = ['_static']
#html_css_files = ['custom.css']

#html_sidebars = {
#'index': [],
#'**': ['searchbox.html','globaltoc.html','sourcelink.html']
#'**': ['searchbox.html','globaltoc.html','relations.html', 'sourcelink.html']
#}

html_theme_options = {
'repository_url': 'https://github.com/JorisPianezze/mesonh_beta_test_guide',
'use_repository_button': True,
#'logo_only': True,
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
