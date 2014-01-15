#!/usr/bin/env bash -x
###########################################################
### Script to execute unit tests.
###########################################################
#
# This script is to be run from the project root directory with the command:
#   <project_root>$ bin/run_test.sh
#
# The command will create an html coverage report in the directory
# <project_root>/BUILD/COVERAGE_REPORT.
#

# Remove pyc files that may cause false results.
find . -type f -iname \*.pyc -delete

# Remove the current coverage collection file
rm -f .coverage
rm -rf BUILD/COVERAGE_REPORT

# Execute the tests as per the given config.
nosetests -c bin/nose.cfg
