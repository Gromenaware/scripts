#!/bin/bash

# Function to rename files and folders recursively
replace_spaces_with_underscores() {
    find "$1" -depth | while read -r item; do
        # Replace spaces with underscores in names
        new_item=$(echo "$item" | sed 's/-/_/g')
        
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
replace_spaces_with_underscores "$start_dir"

echo "Done!"
