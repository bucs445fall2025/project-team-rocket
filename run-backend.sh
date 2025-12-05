#!/bin/bash

# Navigate to the project root directory
cd "$(dirname "$0")" || exit 1

echo "Starting Internship Hub Backend..."
echo "=================================="

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Creating one..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Check if requirements are installed
echo "Checking dependencies..."
pip install -q -r backend/requirements.txt

# Check if MySQL is running
echo "Checking MySQL connection..."
if ! mysql -u ihub_user -pihub_password -e "SELECT 1" &> /dev/null; then
    echo ""
    echo "⚠️  WARNING: Cannot connect to MySQL!"
    echo "Please make sure:"
    echo "  1. MySQL is running"
    echo "  2. Database 'internship_hub' exists"
    echo "  3. User 'ihub_user' exists with password 'ihub_password'"
    echo ""
    echo "See SETUP.md for database setup instructions."
    echo ""
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Run the Flask application
echo "Starting Flask server on http://127.0.0.1:5001..."
echo "Press Ctrl+C to stop the server"
echo "=================================="
python app.py
