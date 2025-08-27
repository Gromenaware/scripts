#!/bin/bash

# Check if the input file is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 input.pdf"
    exit 1
fi

# Input PDF file
input_pdf="$1"

# Check if the file exists
if [ ! -f "$input_pdf" ]; then
    echo "Error: File '$input_pdf' not found."
    exit 1
fi

# Create an output directory
output_dir="${input_pdf%.pdf}_pages"
mkdir -p "$output_dir"

# Get the number of pages in the PDF
total_pages=$(pdftk "$input_pdf" dump_data | grep NumberOfPages | awk '{print $2}')

# Split each page into a separate PDF
echo "Splitting '$input_pdf' into separate pages..."
for ((i=1; i<=total_pages; i++)); do
    output_file="$output_dir/page_$i.pdf"
    pdftk "$input_pdf" cat "$i" output "$output_file"
    echo "Created $output_file"
done

echo "All pages have been split and saved in '$output_dir'."
