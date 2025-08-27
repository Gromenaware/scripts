#!/bin/bash

# Script to download videos from URLs shared on Bluesky
# Requires yt-dlp and ffmpeg to be installed

# Directory to save downloaded videos
OUTPUT_DIR="./downloads"
mkdir -p "$OUTPUT_DIR"

# Check if yt-dlp is installed
if ! command -v yt-dlp &>/dev/null; then
    echo "yt-dlp is not installed. Please install it and try again."
    exit 1
fi

# Check if the URL is passed as an argument
if [[ -z "$1" ]]; then
    echo "No URL provided as an argument. Usage: ./script.sh <video_url>"
    exit 1
fi

VIDEO_URL="$1"

# Download the video with a shortened filename (using video ID)
echo "Downloading video from $VIDEO_URL..."
yt-dlp -o "$OUTPUT_DIR/%(id)s.%(ext)s" "$VIDEO_URL"

if [[ $? -eq 0 ]]; then
    echo "Video downloaded successfully to $OUTPUT_DIR."
else
    echo "Failed to download the video. Please check the URL and try again."
    exit 1
fi
