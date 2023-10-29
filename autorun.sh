#!/bin/bash

# Define your Django project directory and Git repository URL

repo_url="https://github.com/kinderasteroid/Sangeeth-Portfolio"

# Clone the Git repository
echo "Cloning the Git repository..."
git clone https://github.com/kinderasteroid/Sangeeth-Portfolio

# Change to the project directory
cd /Sangeeth-Portfolio

# Create a virtual environment (optional but recommended)
echo "Creating a virtual environment..."
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install Django and project requirements
echo "Installing Django and project requirements..."
pip install -r requirements.txt

# Run database migrations (adjust this if needed)
echo "Applying database migrations..."
python manage.py migrate

# Start the Django development server
echo "Starting the Django development server..."
python manage.py runserver
