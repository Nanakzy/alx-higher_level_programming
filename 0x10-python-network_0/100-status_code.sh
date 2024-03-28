#!/bin/bash
# This script sends a request to a URL passed as an argument and displays only the status code of the response
status_code=$(curl -s -o /dev/null -w "%{http_code}" "$1")
echo -n "$status_code"
