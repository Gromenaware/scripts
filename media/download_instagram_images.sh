#!/bin/bash

# Script to download images from an Instagram post
# Requires: curl, jq

# Function to display usage
function usage() {
    echo "Usage: $0 <instagram_post_url>"
    exit 1
}

# Check if URL is provided
if [ $# -ne 1 ]; then
    usage
fi

# Instagram post URL
POST_URL=$1

# Fetch the HTML of the Instagram post
echo "Fetching post data..."
HTML=$(curl -s -L "$POST_URL")

# Extract image URLs from the HTML
echo "Extracting image URLs..."
IMAGE_URLS=$(echo "$HTML" | sed -n 's/.*"display_url":"\([^"]*\)".*/\1/p')

# Check if any image URLs were found
if [ -z "$IMAGE_URLS" ]; then
    echo "Failed to extract image URLs. Make sure the URL is valid and public."
    exit 1
fi

# Create a directory to save images
SAVE_DIR="instagram_images"
mkdir -p "$SAVE_DIR"

# Download each image
echo "Downloading images..."
COUNT=1
for URL in $IMAGE_URLS; do
    FILE_NAME="$SAVE_DIR/image_$COUNT.jpg"
    curl -s -o "$FILE_NAME" "$URL"
    echo "Downloaded: $FILE_NAME"
    ((COUNT++))
done

echo "All images downloaded to $SAVE_DIR."