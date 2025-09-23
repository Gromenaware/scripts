#!/bin/bash

# Directory to save downloaded images
OUTPUT_DIR="./downloads"
mkdir -p "$OUTPUT_DIR"

# Instagram Full Image Downloader
# Usage: ./image-instagram-downloader.sh <instagram_image_url>

if [ $# -ne 1 ]; then
    echo "Usage: $0 <instagram_image_url>"
    exit 1
fi

URL="$1"

# Fetch HTML content of the Instagram post
HTML_DATA=$(curl -s "$URL")

if [ -z "$HTML_DATA" ]; then
    echo "Could not fetch HTML data."
    exit 2
fi

# Extract JSON data containing the full-resolution image URL
JSON_DATA=$(echo "$HTML_DATA" | grep -oE '<script type="application/ld\+json">[^<]+' | sed 's/<script type="application\/ld+json">//')

if [ -z "$JSON_DATA" ]; then
    echo "Could not find JSON data. Falling back to thumbnail."
    # Extract thumbnail image URL
    ENCODED_IMG_URL=$(echo "$HTML_DATA" | awk -F'<meta property="og:image" content="' '{print $2}' | awk -F'"' '{print $1}')
    FULL_IMG_URL=$(echo "$ENCODED_IMG_URL" | sed 's/&amp;/\&/g')
else
    # Parse JSON data to extract full-resolution image URL
    FULL_IMG_URL=$(echo "$JSON_DATA" | grep -oE '"url":"https:[^"]+' | sed 's/"url":"//')
fi

if [ -z "$FULL_IMG_URL" ]; then
    echo "Could not find full image URL."
    exit 3
fi

echo "Extracted Full Image URL: $FULL_IMG_URL"

# Download the image
FILENAME=$(basename "$FULL_IMG_URL" | cut -d'?' -f1)
curl -L -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" "$FULL_IMG_URL" -o "$OUTPUT_DIR/$FILENAME"

# Check if the file is a valid image
FILE_TYPE=$(file "$OUTPUT_DIR/$FILENAME" | grep -oE 'image|HTML')

if [[ "$FILE_TYPE" == "HTML" ]]; then
    echo "Downloaded file is not an image. Please check the extracted URL."
    exit 4
fi

echo "Downloaded: $OUTPUT_DIR/$FILENAME"