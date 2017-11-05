# ---
# index.py
# ---

import os

import htm
import filestr

page_markup = htm.index_master_markup
index_path = '../index.html'

# Write the index page_markup to index.html
def build():
   
    with open(index_path, 'w') as f:
        f.write(page_markup)

build()
