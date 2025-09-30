#!/bin/bash

# Add Jupyter to PATH
export PATH="/Users/madhugarudala/Library/Python/3.9/bin:$PATH"

# Start Jupyter notebook server
echo "Starting Jupyter notebook server..."
echo "The notebook will open in your default web browser."
echo "To stop the server, press Ctrl+C in this terminal."
echo ""

jupyter notebook

