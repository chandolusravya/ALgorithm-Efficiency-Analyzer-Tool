#!/bin/bash

#run main.py using the arguments passed to this script in virtual environment
source venv/bin/activate
python3 main.py $1 $2 $3 $4 $5 $6 $7 $8 $9
deactivate
