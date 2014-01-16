#!/usr/bin/env bash -x

#==================================================
### Script to clean up any build collateral.
#==================================================

# Remove the code coverage data file created by
# the test exectution script.
echo 'Removing coverage report.'
rm -f .coverage

# Remove the BUILD directory which will get filled
# with build collateral.
echo 'Removing the BUILD directory.'
rm -rf BUILD
