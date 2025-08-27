#!/bin/bash

# Function to rename files and folders recursively
rename_files_and_folders() {
    find "$1" -depth | while read -r item; do
        # Remove parentheses from names
        new_item=$(echo "$item" | sed 's/[()]//g')
        
        # Rename item if the new name is different
        if [ "$item" != "$new_item" ]; then
            mv "$item" "$new_item"
            echo "Renamed: $item -> $new_item"
        fi
    done
}

# Starting directory (default is current directory if no argument is provided)
start_dir="${1:-.}"

echo "Starting from directory: $start_dir"
rename_files_and_folders "$start_dir"

echo "Done!"
