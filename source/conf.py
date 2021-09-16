import recommonmark
from recommonmark.transform import AutoStructify
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

project = 'VapoR'
copyright = '2021, VapoR'
author = 'VapoR'

# The full version, including alpha/beta/rc tags
release = '2050'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'recommonmark',
    'sphinx.ext.todo',
    'sphinx.ext.extlinks',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.duration',
    'sphinx_markdown_tables'
]
todo_include_todos = True
todo_emit_warnings = True
autosectionlabel_prefix_document = True

html_theme = 'sphinx_rtd_theme'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['../common/_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 4,
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../common/_static']

html_css_files = [
    'css/textstyles.css',
    'css/custom.css'
]

html_favicon = '../common/_static/img/logo.png'
html_title = "VapoR Docs"
html_short_title = "VDocs"

rst_prolog = """
.. include:: /../common/.textstyles.rst
"""

def setup(app):
    app.add_config_value('recommonmark_config', {
            #'url_resolver': lambda url: github_doc_root + url,
            'enable_math': False,
            'enable_inline_math': False,
            'enable_eval_rst': True,
        }, True)
    app.add_transform(AutoStructify)