#!/bin/bash

if [ "$EUID" -ne 0 ]; then
    echo "Please run this script with sudo privileges."
    exit 1
fi

echo "This script is developed by Ben (@randomappleboi) in October, 2023."

echo "Installing dependencies..."
apt update
apt install -y deborphan python3 python3-tk python3-pil.imagetk

echo "Launching 'apt.py'..."
python3 apt.py

