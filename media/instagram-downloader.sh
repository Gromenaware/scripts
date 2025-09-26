#!/bin/bash

OUTPUT_DIR="./downloads"
mkdir -p "$OUTPUT_DIR"

if [ -z "$1" ]; then
    echo "Usage: $0 <INSTAGRAM_REEL_URL>"
    exit 1
fi

URL="$1"

if ! command -v yt-dlp &> /dev/null; then
    echo "yt-dlp is required. Install it with: pip install yt-dlp"
    exit 2
fi

if ! command -v python3 &> /dev/null; then
    echo "Python3 is required. Please install it."
    exit 3
fi

# Export cookies.txt using Python script
python3 export_instagram_cookies.py
if [ ! -f cookies.txt ]; then
    echo "Failed to export cookies.txt. Aborting."
    exit 4
fi

# Use cookies.txt to handle private reels
yt-dlp --cookies cookies.txt "$URL" -o "$OUTPUT_DIR/%(title)s.%(ext)s"
echo "Download completed. Files are saved in $OUTPUT_DIR"
#rm cookies.txt