#!/usr/bin/env bash

###########################################################
### Script to make it easier to live as a developer.
###
### The script will add the ./bin directory to your session
### path, so that development scripts can be run by simply
### typing out the command. The script will also activate
### virtualenv.
###
### This script needs to change your current running bash
### session. To do so you need to source execute the
### script. Do this with either of the two following
### commands at the prompt.
###
###   PROJECT_ROOT> . bin/enable_dev.sh
###
### or
###
###   PROJECT_ROOT> source bin/enable_dev.sh
###
###########################################################

# if necessary, setup the dev bin scripts
DEV_BIN="./bin"
if [ -d "$DEV_BIN" ] && [[ ! $PATH =~ (^|:)$DEV_BIN(:|$) ]]
then
  echo "Adding './bin' to path to ease use of dev scripts."
  PATH=$PATH:$DEV_BIN
fi

# enable the virtual environment
source venv/bin/activate
