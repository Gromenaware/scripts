#!/bin/bash

# Instagram Reel Downloader
# Usage: ./instagram-downloader.sh <INSTAGRAM_REEL_URL>

# Directory to save downloaded videos
OUTPUT_DIR="./downloads"
mkdir -p "$OUTPUT_DIR"

if [ -z "$1" ]; then
    echo "Usage: $0 <INSTAGRAM_REEL_URL>"
    exit 1
fi

URL="$1"

# Check for yt-dlp
if ! command -v yt-dlp &> /dev/null; then
    echo "yt-dlp is required. Install it with: pip install yt-dlp"
    exit 2
fi

yt-dlp "$URL" -o "$OUTPUT_DIR/%(title)s.%(ext)s"
