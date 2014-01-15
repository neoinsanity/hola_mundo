#!/usr/bin/env bash -x

###########################################################
##### Create virtualenv for development.
# Virtaulenv needs to be installed for this to work.
# If you don't have virtualenv installed please visit
# https://pypi.python.org/pypi/virtualenv
# for instructions on installing virutalenv.
###########################################################

# Create the virtual environment
virtualenv venv

echo
echo "------------------------------------------------"
echo "- Virtual environment created in directory 'venv'"
echo "------------------------------------------------"

# Activate the virtual environment
echo
echo "------------------------------------------------"
echo "----- Activating virtual env with command. -----"

source venv/bin/activate

echo "------------------------------------------------"
echo

###########################################################
##### Install the windmills package in development mode.
###########################################################
echo
echo "------------------------------------------------"
echo "------ Setting up development environment ------"
echo "------------------------------------------------"

python setup.py develop

###########################################################
##### Install development related packages.
###########################################################
echo
echo "------------------------------------------------"
echo "------- Installing development packages --------"
echo "------------------------------------------------"
echo
pip install -r bin/dev_requirements.txt
