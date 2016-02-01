#!/usr/bin/env bash

# Build the current documentation.
./bin/doc_build.sh

# Make sure a clean environment is present.
rm -rfv ./BUILD/gh_pages

# Create the clone
git clone https://github.com/neoinsanity/hola_mundo.git -b gh-pages ./BUILD/gh_pages

# This is just to output state of the pulled branch
cd ./BUILD/gh_pages
git rm -rf .
git status

# Update with latest docs for the documentation built.
cp -r ../../BUILD/doc/build/. .

# The jekyall support needs to be turned off on gh-pages for proper display.
echo "Disable jekyll support." > '.nojekyll'

# Now commit and push the changes.
git add .
git commit -a -m "Document Update"
git status
git push origin gh-pages

# Returned to root directory.
cd -
