#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument, and displays the body of the response

# Check if the file exists and is readable
if [ ! -r "$2" ]; then
    echo "File not found or not readable: $2"
    exit 1
fi

# Check if the file contains valid JSON
if ! jq . "$2" >/dev/null 2>&1; then
    echo "Not a valid JSON: $2"
    exit 2
fi

# Send POST request with the contents of the file and display the response body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
