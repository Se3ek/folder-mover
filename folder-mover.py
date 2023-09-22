import os, shutil, argparse

def movefiles(directory, ignore):
    """Actual part of the work to be done

    Args:
        directory (str): Absolute directory path where the program should be executed
        ignore (list): List of to be ignored files (file name with extension, no wildcards)
    """

    # Create list of non-ignored filenames:
    files = [file for file in os.scandir(directory) if file.name not in ignore]  # Comprehend a list of not ignored filenames

    nameset = {os.path.splitext(file.name)[0] for file in files} # Make a set for for folders to be created

    for item in nameset: os.mkdir(os.path.join(directory, item))  # Create directory for every name in the set to then move files into

    for filetomove in files: shutil.move(filetomove, os.path.join(directory, os.path.splitext(filetomove)[0]))    # move files into their respective folders

def main(args):
    """Take the given input and call the work function to move contained files into folders of the name without extension

    Args:
        args: Parsed arguments from Arguments Parser to be analyzed on what to do
    """
        
    # Path string
    path = args.path
    
    # List of default to-be-ignored files (mainly for debugging purposes and for itself):
    ignore = ['.git', 'README.md', 'folder-mover.py', '.gitignore', 'Test.sh']
    
    # Add custom ignore list to the default list if there is one
    if args.ignore:
        ignore += args.ignore.split(",")
    
    # Overwrite the ignore list with the exclusive ignore list if there is one
    if args.ignore_only:
        ignore = args.ignore_only.split(",")
        
    # If required, log the ignore list
    if args.verbose_ignore:
        print(ignore)
    else:
        movefiles(path, ignore)  # Call the working function with the determined path string    
    
# Initialize a new parser for the CLI
parser = argparse.ArgumentParser(description='Moves files of a given directory into folders with the same name without the extension')

# store the path as a variable
parser.add_argument(
    '-p', '--path',
    type = str,
    default = os.getcwd(),
    help = 'Path for the script to work in. Default is the working directory from where the script is called'
)

# store the custom ignore list
parser.add_argument(
    '-i', '--ignore',
    type = str,
    help = 'Comma-separated list of files to be ignored by the script (with file extensions) including list: [".git", "README.md", "folder-mover.py", ".gitignore", "Test.sh"]'
)

# store the exclusive custom ignore list
parser.add_argument(
    '-io', '--ignore_only',
    type = str,
    help = 'Comma-separated list of files to be ignored by the script (with file extensions). Overgoes the default list.'
)

# See if the ignore list is supposed to be logged for testing
parser.add_argument(
    '-vi', '--verbose_ignore',
    action = 'store_true',
    help = argparse.SUPPRESS
)

args = parser.parse_args()  # Get the arguments given by the caller

main(args)
