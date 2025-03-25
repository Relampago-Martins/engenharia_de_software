#!/bin/bash

# Check if a directory was provided
if [[ $# -eq 0 ]]; then
    echo "Usage: $0 -d <directory> or $0 --dir=<directory>"
    exit 1
fi

# Parse arguments
for arg in "$@"
do
    case $arg in
        -d=*|--dir=*)
        DIR="${arg#*=}"
        shift
        ;;
        -d|--dir)
        DIR="$2"
        shift 2
        ;;
    esac
done

# Verify if directory was specified
if [[ -z "$DIR" ]]; then
    echo "Error: Directory not specified"
    exit 1
fi

# Verify if directory exists
if [[ ! -d "$DIR" ]]; then
    echo "Error: Directory '$DIR' not found"
    exit 1
fi

# Function to monitor directory
monitor_directory() {
    # Use find to get a snapshot of files and their modification times
    # Store this in a temporary file
    find "$DIR" -type f -printf "%p %T@\n" > /tmp/initial_state

    while true; do
        # Wait for a few seconds
        sleep 2

        # Create a new snapshot
        find "$DIR" -type f -printf "%p %T@\n" > /tmp/current_state

        # Compare the snapshots
        if ! cmp -s /tmp/initial_state /tmp/current_state; then
            echo "Changes detected in directory '$DIR'. Copying files..."
            
            # Copy all files to www directory
            ./copy2www.sh -d "$DIR"

            # Update the initial state
            cp /tmp/current_state /tmp/initial_state
        fi
    done
}

# Start monitoring
monitor_directory