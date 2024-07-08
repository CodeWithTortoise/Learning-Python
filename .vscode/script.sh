#!/bin/bash

# Path to your extensions.json file
EXTENSIONS_FILE="./extension.json"

# Check if extensions.json exists
if [ ! -f "$EXTENSIONS_FILE" ]; then
    echo "Error: extensions.json not found."
    exit 1
fi

# Read extensions.json and install each extension
EXTENSIONS=$(jq -r '.extensions | .[]' "$EXTENSIONS_FILE")

for EXTENSION in $EXTENSIONS
do
    echo "Installing extension: $EXTENSION"
    code --install-extension $EXTENSION --force # Use --force to avoid confirmation prompt
done

echo "All extensions installed."
