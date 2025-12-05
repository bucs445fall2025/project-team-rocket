#!/bin/bash

# Navigate to the frontend directory
cd "$(dirname "$0")/frontend" || exit 1

echo "Starting Internship Hub Frontend..."
echo "==================================="

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "node_modules not found. Installing dependencies..."
    npm install
else
    echo "Dependencies found. Skipping npm install..."
fi

# Start the React application
echo "Starting React development server..."
echo "Should open at http://localhost:3000"
echo "Press Ctrl+C to stop the server"
echo "==================================="
npm start
