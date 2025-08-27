#!/bin/bash

# Function to convert MP4 to WebM
convert_mp4_to_webm() {
    input_file="$1"
    output_file="$2"

    # Check if input file exists
    if [ ! -f "$input_file" ]; then
        echo "Error: File '$input_file' does not exist."
        exit 1
    fi

    # Check if the input file is an MP4
    if [[ "$input_file" != *.mp4 ]]; then
        echo "Error: Input file must be an MP4 file."
        exit 1
    fi

    # Set output file name if not provided
    if [ -z "$output_file" ]; then
        output_file="${input_file%.mp4}.webm"
    fi

    # Convert the MP4 to WebM using ffmpeg
    ffmpeg -i "$input_file" -c:v libvpx -c:a libvorbis "$output_file"

    # Check if conversion was successful
    if [ $? -eq 0 ]; then
        echo "Successfully converted to '$output_file'."
    else
        echo "Error: Conversion failed."
        exit 1
    fi
}

# Check for input arguments
if [ $# -lt 1 ]; then
    echo "Usage: $0 <input_file> [output_file]"
    exit 1
fi

# Call the function with arguments
convert_mp4_to_webm "$1" "$2"

