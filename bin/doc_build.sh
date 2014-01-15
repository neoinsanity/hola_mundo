#!/usr/bin/env bash -x
mkdir -p BUILD/doc/build
sphinx-build -b html ./doc BUILD/doc/build/
