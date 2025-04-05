#!/bin/bash

clear

echo "Cleaning up logs and content directories..."

# Remove logs directory
if [ -d "logs" ]; then
    echo "Removing logs directory..."
    rm -rf logs
fi

# Remove content directory
if [ -d "content" ]; then
    echo "Removing content directory..."
    rm -rf content
fi

# Remove links.md
if [ -f "links.md" ]; then
    echo "Removing links.md..."
    rm links.md
fi

echo
echo "Cleanup complete!"
echo "- Removed logs directory"
echo "- Removed content directory"
echo 