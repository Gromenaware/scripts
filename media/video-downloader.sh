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

# Prompt for the video URL
read -p "Enter the video URL: " VIDEO_URL

# Validate the URL
if [[ -z "$VIDEO_URL" ]]; then
    echo "No URL entered. Exiting."
    exit 1
fi

# Download the video
echo "Downloading video from $VIDEO_URL..."
yt-dlp -o "$OUTPUT_DIR/%(title)s.%(ext)s" "$VIDEO_URL"

if [[ $? -eq 0 ]]; then
    echo "Video downloaded successfully to $OUTPUT_DIR."
else
    echo "Failed to download the video. Please check the URL and try again."
    exit 1
fi
