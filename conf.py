# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'ET: Legacy'
copyright = '2012-2025, ET: Legacy Team'
author = 'ET: Legacy Team'

# The full version, including alpha/beta/rc tags
release = '2.82.2'

# -- General configuration ---------------------------------------------------

# The master toctree document.
master_doc = 'index'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    'sphinx.ext.autosectionlabel',
    'sphinx_rtd_theme',
]

# Section titles are only labeled up to the second level, and the labels are
# prefixed with the document name. This keeps the references unique, as the
# same subsection titles are repeated in several documents.
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 2

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# The favicon of the docs (the ET: Legacy logo).
html_favicon = '_static/images/favicon.ico'

# The ET: Legacy website look & feel is applied through custom-styles.css.
# Hide the default "Built with Sphinx" and copyright lines: they are replaced
# by a website-style footer (see _templates/footer.html).
html_show_sphinx = False
html_show_copyright = False

# Read the Docs theme options.  The documentation mimics the look and feel of
# https://www.etlegacy.com (dark background, coral accent, Kenzo/Bitter/Open
# Sans typography) through _static/custom-styles.css.
html_theme_options = {
    'logo_only': True,
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': False,
    'titles_only': False,
    'style_external_links': True,
    'prev_next_buttons_location': 'bottom',
}

# Extra links shown in the documentation top header, mirroring the website
# main navigation.
html_context = {
    'etl_nav': [
        ('Downloads', 'https://www.etlegacy.com/download'),
        ('Blog', 'https://www.etlegacy.com/blog'),
        ('Servers', 'https://www.etlegacy.com/servers'),
        ('About', 'https://www.etlegacy.com/about'),
        ('Wiki', 'https://github.com/etlegacy/etlegacy/wiki'),
        ('GitHub', 'https://github.com/etlegacy/etlegacy'),
        ('Discord', 'https://discord.gg/UBAZFys'),
    ],
}

# The name of the Pygments (syntax highlighting) style to use.  A dark style
# is used so that code blocks blend with the website-inspired dark theme.
pygments_style = 'monokai'

# -- Extension configuration -------------------------------------------------

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


def setup(app):
    app.add_css_file('custom-styles.css')
