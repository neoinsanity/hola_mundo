#!/usr/bin/env bash
#
############################################################
###### Create development.
## This is a Poetry managed project.
## Poetry installation is required. See:
## https://python-poetry.org/docs/ for installation and
## usage of poetry tool.
############################################################

echo "---------------------------------------------------"
echo "--- Installing project development environment. ---"
echo "---------------------------------------------------"
echo
poetry install --with test,doc
