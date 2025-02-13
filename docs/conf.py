# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import shutil
import sys

# Get version from setup.py
with open("../setup.py", "r") as f:
    for i in f.readlines():
        if i.startswith("version"):
            version = i.split("= ")[1]

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'mlr-gd'
copyright = '%Y, DrSolidDevil'
author = 'DrSolidDevil'
release = version

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode', 'sphinx.ext.napoleon', 'myst_parser']
# Display todos
todo_include_todos = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
myst_heading_anchors = 5

html_logo = "../logo.png"

html_theme_options = {
    "logo": {
        "link": "index.html",
        "alt_text": "mlr-gd"
    },
    "external_links": [
      {"name": "PyPi", "url": "https://pypi.org/project/mlr-gd/"},
      {"name": "Releases", "url": "https://github.com/DrSolidDevil/mlr-gd//releases/"}
    ],

    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/drsoliddevil/mlr-gd",
            "icon": "fa-brands fa-github",
        }
    ]
}

# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute.
sys.path.insert(0, os.path.abspath('../'))

# -- Miscellaneous Tasks -----------------------------------------------------

# Copying other documentation files form outside docs.
shutil.copy('../README.md', '../docs/')
shutil.copy('../CONTRIBUTING.md', '../docs/')
shutil.copy('../SECURITY.md', '../docs/')
shutil.copy('../CODE_OF_CONDUCT.md', '../docs/')

# Removes the badges from the readme
with open("README.md", "r+") as f:
    f_r = f.read()
    f.seek(0)
    pre, post = f_r.split('<div id="badges"')
    post = post.split('</div>')[1]
    extra = post.split('<h2>')
    f.write(pre + extra[0])
    f.truncate()

    with open("post.md", "w+") as f2:
        f2.write("<h2>" + "<h2>".join(extra[1:]))

if os.path.exists('pre.md'):
    os.remove('pre.md')
os.rename('README.md', 'pre.md')
