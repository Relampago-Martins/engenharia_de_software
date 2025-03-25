#!/bin/bash

# Define the web directory as a variable
WEB_DIR="/var/www/html"
FILE_NAME="index.php"
DIR_MODE=false
DIR_PATH=""

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -f|--file)
            FILE_NAME="$2"
            shift 2
            ;;
        -d|--dir)
            DIR_MODE=true
            DIR_PATH="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1"
            echo "Usage: $0 [-f|--file filename] [-d|--dir directory]"
            exit 1
            ;;
    esac
done

# Check if Apache is running
if systemctl is-active --quiet apache2; then
    echo "Apache is already running."
else
    echo "Starting Apache..."
    sudo systemctl start apache2
    sudo systemctl enable apache2
fi

# Handle file mode
if [ "$DIR_MODE" = false ]; then
    # Check if specified file exists in the current directory
    if [ -f "./$FILE_NAME" ]; then
        echo "Updating $WEB_DIR/$FILE_NAME with the contents of ./$FILE_NAME"
        sudo cp "./$FILE_NAME" "$WEB_DIR"
        sudo chown -R www-data:www-data "$WEB_DIR"
        echo "Update complete."
    else
        echo "Error: ./$FILE_NAME not found. Please make sure the file exists."
        exit 1
    fi
fi

# Handle directory mode
if [ "$DIR_MODE" = true ]; then
    # Check if specified directory exists
    if [ -d "$DIR_PATH" ]; then
        echo "Copying all files from $DIR_PATH to $WEB_DIR"
        sudo cp -r "$DIR_PATH"/* "$WEB_DIR"
        sudo chown -R www-data:www-data "$WEB_DIR"
        echo "Directory copy complete."
    else
        echo "Error: Directory $DIR_PATH not found. Please provide a valid directory path."
        exit 1
    fi
fi