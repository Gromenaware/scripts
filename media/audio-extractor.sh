#!/bin/bash


# Check if ffmpeg is installed
if ! command -v ffmpeg &> /dev/null
then
    echo "ffmpeg could not be found. Please install ffmpeg first."
    exit 1
fi

# Check for correct number of arguments
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <input_mp4_file> <output_mp3_file>"
    exit 1
fi

# Input and output files
INPUT_FILE="$1"
OUTPUT_FILE="$2"

# Check if the input file exists
if [ ! -f "$INPUT_FILE" ]; then
    echo "Input file '$INPUT_FILE' does not exist."
    exit 1
fi

# Extract MP3 from MP4
ffmpeg -i "$INPUT_FILE" -q:a 0 -map a "$OUTPUT_FILE"

# Check if the operation was successful
if [ $? -eq 0 ]; then
    echo "MP3 file successfully created: $OUTPUT_FILE"
else
    echo "Failed to extract MP3 from $INPUT_FILE."
    exit 1
fi
