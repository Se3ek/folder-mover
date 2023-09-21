# folder-mover
Moves files into folders of the same name

Just a little program to move files into folders of the same name excluding the file extension.
It is meant to sort multiple file extension versions of content into folders for better visibility.
I want it to get the contents of the folder it's placed in, create a folder for the name of the file on top of the list,
if it doesn't already exist, and move it into the folder.

## How-to
Execute the program with the following scheme:

```bash
python *path-to-script*/folder-mover.py [-p | --path] PATH(str)
```

You have to pass one of the following inputs:

```
[-p | --path]
```
Pass in an absolute path of a directory on which contents the script is supposed to do its work (as a string).
Default path is that of the current working directory from which the script is called (Note that it's *not* necessarily the location of the script).
There is a default list of ignored filenames, mainly for debugging and the git files:
```
['.git', 'README.md', 'folder-mover.py', '.gitignore']
```
The list is honoured for whichever location the script is run on or from. My assumption is if you're having it work on a directory with a git repo inside, you'd still want the associated repo files to be left alone if present.
However, if you are in a git repo, know that there may be files and folders that are *not* ignored, perhaps a .github or whatever.
A future release will give you the possibility to pass in a list of additional to-be-ignored files.

## Project info
I personally needed a script like this to sort files downloaded from Humble Bundle where you get multiple files of different types with the same name and contents (e. g. books in pdf, epub, etc.). I wanted these to be saved into a respective folder each to then be stored without having to do it myself.

It's also very much a learning project to keep myself in practice with python and git. Pull requests if there are any ideas on optimizations are welcomed.
