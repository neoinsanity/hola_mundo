#!/usr/bin/env bash

# Create the clone.
git clone https://github.com/neoinsanity/hola_mundo.git ./BUILD/gh_pages

# Change into the work directory.
ls ./BUILD/gh_pages
cd ./BUILD/gh_pages

# Initialize the gh_pages orphan branch.
git checkout --orphan gh-pages
git rm -rfv
rm -v '.gitignore'
echo "My Page" > index.html
git add index.html
git commit -a -m "First pages commit"
git push origin gh-pages

# Jump back to the root directory.
cd -

# Clean up behind the initialization.
rm -rfv ./BUILD/gh_pages
ls ./BUILD/gh_pages
