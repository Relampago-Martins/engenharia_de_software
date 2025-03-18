#!/bin/bash

# Define the web directory as a variable
WEB_DIR="/var/www/html"
FILE_NAME="index.php"

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -f|--file)
            FILE_NAME="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1"
            echo "Usage: $0 [-f|--file filename]"
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

# Check if specified file exists in the current directory
if [ -f "./$FILE_NAME" ]; then
    echo "Updating $WEB_DIR/$FILE_NAME with the contents of ./$FILE_NAME"
    sudo cp "./$FILE_NAME" "$WEB_DIR/$FILE_NAME"
    sudo chown www-data:www-data "$WEB_DIR/$FILE_NAME"
    sudo chmod 644 "$WEB_DIR/$FILE_NAME"
    echo "Update complete."
else
    echo "Error: ./$FILE_NAME not found. Please make sure the file exists."
    exit 1
fi