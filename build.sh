#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Install dependencies
echo "Installing dependencies..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# Create staticfiles directory if it doesn't exist
mkdir -p staticfiles

# Copy static files directly
echo "Copying static files..."
cp -r static/* staticfiles/

# Collect static files
echo "Collecting Static Files..."
python3 manage.py collectstatic --noinput --clear

# Apply database migrations
echo "Making Migrations..."
python3 manage.py makemigrations --noinput

echo "Applying Migrations..."
python3 manage.py migrate --noinput