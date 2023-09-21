"""
Just a little program to move files into folders of the same name excluding the file extension.
It is meant to sort multiple file extension versions of content into folders for better visibility.
I want it to get the contents of the folder it's placed in, create a folder for the name of the file on top of the list,
if it doesn't already exist, and move it into the folder.
"""

import os, shutil

# List of to-be-ignored files (mainly for debugging purposes and for itself):
ignore = ['.git', 'README.md', 'folder-mover.py', '.gitignore']
# Make a set for for folders to be created:
nameset = set()
# Create list of non-ignored filenames:
filenames = [file for file in os.scandir() if file.name not in ignore]  # Comprehend a list of not ignored filenames

for file in filenames:
    nameset.add(os.path.splitext(file.name)[0])     # add names of files without extensions to the set (creating unique entries because set magic)

for item in nameset:
    os.mkdir(item)  # Create directory for every name in the set to then move files into

for filetomove in filenames:
    if os.path.splitext(filetomove)[0] not in ignore:
        shutil.move(filetomove, os.path.splitext(filetomove)[0])    # move files into their respective folders
