#!/bin/bash

# Check if exactly one argument (URL) is provided
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 URL"
  exit 1
fi

# Define the URL from the argument
url="$1"

# Use curl to get the response and pipe its size (excluding headers) to wc -c
response_size=$(curl -s -o /dev/null -w "%{size_download}" "$url")

# Display the body size in bytes
echo "$response_size bytes"
