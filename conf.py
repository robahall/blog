# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


import os
import sys

import sphinx_material

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('../sphinxext'))

# -- Project information -----------------------------------------------------

project = 'Cloud Based Machine Learning Tutorials'
copyright = '2019, Rob Hall'
author = 'Rob Hall'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.mathjax',
              'nbsphinx',
              'sphinx.ext.viewcode',
              'sphinx.ext.githubpages',
              'sphinx.ext.autosummary',
              'sphinx.ext.inheritance_diagram',
              'sphinx.ext.intersphinx',
              'sphinx.ext.autosectionlabel'
              #'matplotlib.sphinxext.plot_directive',  # Need to update these.
              #'IPython.sphinxext.ipython_console_highlighting',  # Need to update these.
              #'IPython.sphinxext.ipython_directive'  # Need to update these.
              ]


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build','**.ipynb_checkpoints', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#Set the theme to sphinx_material
extensions.append('sphinx_material')
html_theme = 'sphinx_material'

# Get the theme path
html_theme_path = sphinx_material.html_theme_path()
# Register the required helpers for the html context
html_context = sphinx_material.get_html_context()

#Picture link:
# Material theme options (see theme.conf for more information)
html_theme_options = {

    # Set the name of the project to appear in the navigation.
    'nav_name': 'Project Name',

    # Set you GA account ID to enable tracking
    'google_analytics_account': 'UA-84085508-1',

    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    'base_url': 'https://www.robahall.com',
    # Set the color and the accent color
    'color_primary': 'green',
    'color_accent': 'light-green',

    # Set the repo location to get a badge with stats
    'repo_url': 'https://github.com/robahall/robahall.github.io',
    'repo_name': 'Project',

    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': 1,
    # If False, expand all TOC entries
    'globaltoc_collapse': True,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': True
}

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
## Need to download this.
html_logo = 'https://avatars0.githubusercontent.com/u/13205851?v=3&s=460'