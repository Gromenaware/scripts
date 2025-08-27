#!/bin/bash

# Function to rename folders recursively
rename_folders() {
    find "$1" -depth -type d | while read -r dir; do
        # Remove parentheses from folder names
        new_dir=$(echo "$dir" | sed 's/[()]//g')
        
        # Rename folder if the new name is different
        if [ "$dir" != "$new_dir" ]; then
            mv "$dir" "$new_dir"
            echo "Renamed: $dir -> $new_dir"
        fi
    done
}

# Starting directory (default is current directory if no argument is provided)
start_dir="${1:-.}"

echo "Starting from directory: $start_dir"
rename_folders "$start_dir"

echo "Done!"
