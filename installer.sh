#!/bin/bash

# Check Python version
pyver=$(python --version 2>&1 | awk '{print $2}')
required_pyver="3.11.7"

if [ "$pyver" = "$required_pyver" ]; then
    echo "Found Python $required_pyver"
else
    echo "Python $required_pyver is required."
    echo "Attempting to install Python $required_pyver using apt..."
    sudo apt-get update
    # Try to install Python. Replace 'python3.11' with the specific package if available.
    # Note: As of my last update, Python 3.11.7 might not be directly available via apt
    sudo apt-get install -y python3.11
    if [ $? -eq 0 ]; then
        echo "Python $required_pyver installed successfully."
    else
        echo "Failed to install Python $required_pyver. Please install it manually from https://www.python.org/downloads/"
        exit 1
    fi
fi

# Check for default values in appsettings.json
defaultsFound=0

if grep -q "\"PAT\": \"your_personal_access_token_here\"" appsettings.json; then
    echo "Make sure PAT is updated from the default value."
    defaultsFound=1
fi

if grep -q "\"Organization\": \"organization\"" appsettings.json; then
    echo "Make sure Organization is updated from the default value."
    defaultsFound=1
fi

if grep -q "\"Project\": \"project\"" appsettings.json; then
    echo "Make sure Project is updated from the default value."
    defaultsFound=1
fi

if grep -q "\"Repo\": \"repo\"" appsettings.json; then
    echo "Make sure Repo is updated from the default value."
    defaultsFound=1
fi

if [ "$defaultsFound" -eq 1 ]; then
    echo "One or more default values are not updated in appsettings.json. Please update them before proceeding."
    exit 1
fi

# Install GitPython
echo "Installing GitPython..."
python -m pip install GitPython

echo "Done."