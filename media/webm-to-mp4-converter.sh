#!/bin/bash

# Script to convert a .webm file to .mp4 using ffmpeg

# Check if ffmpeg is installed
if ! command -v ffmpeg &> /dev/null
then
    echo "ffmpeg could not be found. Please install ffmpeg first."
    exit 1
fi

# Check if input file is provided
if [ "$#" -lt 1 ]; then
    echo "Usage: $0 input_file.webm [output_file.mp4]"
    exit 1
fi

# Input file
input_file="$1"

# Check if the input file exists
if [ ! -f "$input_file" ]; then
    echo "Input file '$input_file' not found."
    exit 1
fi

# Set output file name
if [ "$#" -ge 2 ]; then
    output_file="$2"
else
    output_file="${input_file%.*}.mp4"
fi

# Convert .webm to .mp4 using ffmpeg
ffmpeg -i "$input_file" -c:v libx264 -preset slow -crf 23 -c:a aac "$output_file"

# Check if conversion was successful
if [ $? -eq 0 ]; then
    echo "Conversion successful. Output file: $output_file"
else
    echo "Conversion failed."
    exit 1
fi

