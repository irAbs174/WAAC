#!/bin/bash

# Create virtual environment & activate environment
python3 -m venv env && source env/bin/activate

# install requirements.txt
pip3 install -r requirements.txt

# Run server
fastapi dev app/backend/server.py