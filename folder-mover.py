import os, shutil, sys

def movefiles(directory):
    """Actual part of the work to be done

    Args:
        directory (str): Absolute directory path where the program should be executed
    """
        
    # List of to-be-ignored files (mainly for debugging purposes and for itself):
    ignore = ['.git', 'README.md', 'folder-mover.py', '.gitignore']

    # Create list of non-ignored filenames:
    files = [file for file in os.scandir(directory) if file.name not in ignore]  # Comprehend a list of not ignored filenames

    nameset = {os.path.splitext(file.name)[0] for file in files} # Make a set for for folders to be created

    for item in nameset: os.mkdir(os.path.join(directory, item))  # Create directory for every name in the set to then move files into

    for filetomove in files: shutil.move(filetomove, os.path.join(directory, os.path.splitext(filetomove)[0]))    # move files into their respective folders

def main(input):
    """Take the given input and call the work function to move contained files into folders of the name without extension

    Args:
        input (str): Either --here flag (Starts process in script's location) or absolute path of a directory
    """
    
    # If the --here flag is called, get the current path and pass that into the work function
    if input == "--here":
        # Get the current path through the os package and overwrite with current working directory
        input = os.getcwd()
        
    movefiles(input)  # Call the working function with the determined path string

main(sys.argv[1])
