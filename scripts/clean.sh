#!/bin/bash

echo "Cleaning up logs and output directories..."

# Remove logs directory
if [ -d "logs" ]; then
    echo "Removing logs directory..."
    rm -rf logs
fi

# Remove output directory
if [ -d "output" ]; then
    echo "Removing output directory..."
    rm -rf output
fi

# Remove links.md
if [ -f "links.md" ]; then
    echo "Removing links.md..."
    rm links.md
fi

echo
echo "Cleanup complete!"
echo "- Removed logs directory"
echo "- Removed output directory"
echo 