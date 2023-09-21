#!/bin/bash

# =====================================================
# Set up the Testing folder, files and functions
# =====================================================

dir=$HOME/temp/folder-mover-tests  # Directory for the testing
declare -a check_folders    # Create the empty array to check the folders against
interval=(1 2 3 4 5)

mkdir -p $dir   # Make the test directory if it doesn't already exist

init () {   # Run once; set up everything that's needed for testing
    for i in ${interval[@]}; do
        check_folders=("${check_folders[@]}" "${dir}/Test${i}")  # Build an array of the desired outcome to compare against
    done
}

setup () {   # Nuke the test folder and set it up again for a new test after you got the result for a test case
    rm -r ${dir}/*  # Remove everything that's in the directory for a clean slate
    # Create some Test files with different extensions under the same name
    for i in ${interval[@]}; do     # Create 5 Testfiles of different extensions
        touch ${dir}/Test${i}.txt
        touch ${dir}/Test${i}.html
        touch ${dir}/Test${i}.py
    done
}

analyze () {    # Inspect the test folder and echo if there are any problems
    # Analyze the Test directory to see if it contains what it is supposed to
    # This is but one step of a complete test run

    declare -a fails    # Declare an empty array of folder contents

    # Add elements as read from the Test folder:
    for item in ${dir}/*; do
        items=("${items[@]}" "$item")
    done

    # Compare folders to the blueprint array:
    if [[ ${items[*]} == ${check_folders[*]} ]]; then
        echo "Folder structure is ok. "
    else
        echo "Folder structure is NOT RIGHT!"
    fi

    # Check if every folder's content is the correct one and if not echo the number that's wrong
    # This is meant to not create an obnoxious amount of output if everything is ok
    for i in ${interval[@]}; do
        for file in ${dir}/Test${i}/*; do
            if [[ ${file##*/} = "Test${i}.txt" ]]; then
                true
            elif [[ ${file##*/} = "Test${i}.html" ]]; then
                true
            elif [[ ${file##*/} = "Test${i}.py" ]]; then
                true
            else
                echo "Content of folder ${i} structure is NOT RIGHT"
            fi
        done
    done
}

init    # Initialize the data to test against

# =====================================================
# Go through the process of testing:
# =====================================================

# setup   # Set up the test folder
analyze # Analyze the output from the test

# ==== Tests finished, remove the testing directory also ====
# rm -r dir
