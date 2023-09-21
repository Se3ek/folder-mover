#!/bin/bash

# ====================================
# Set up the Testing folder and files
# ====================================

dir=$HOME/temp/folder-mover-tests  # Directory for the testing
declare -a check_folders    # Create the empty array to check the folders against
interval=(1 2 3 4 5)

mkdir -p $dir   # Make the test directory if it doesn't already exist

init () {
    for i in ${interval[@]}; do
        check_folders=("${check_folders[@]}" "${dir}/Test${i}")  # Build an array of the desired outcome to compare against
    done
}

setup () {   # Nuke the test folder and set it up again for a new test after you got the result for a test case
    rm -r ${dir}/*  # Remove everything that's in the directory for a clean slate
    # Create some Test files with different extensions under the same name
    for i in $interval; do     # Create 5 Testfiles of different extensions
        touch ${dir}/Test${i}.txt
        touch ${dir}/Test${i}.html
        touch ${dir}/Test${i}.py
    done
}

analyze () {    # Analyze the Test directory to see if it contains what it is supposed to
    declare -a items    # Declare an empty array of folder contents

    for item in ${dir}/*; do
        items=("${items[@]}" "$item")   # Add elements as read from the Test folder 
    done
}

# Go through the process of testing:
init    # Initialize the data to test against
setup   # Set up the test folder
analyze # Analyze the output from the test

# ==== Tests finished, remove the testing directory also ====
# rm -r dir
