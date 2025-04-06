#!/usr/bin/env bash
mkdir -p BUILD/doc/build
sphinx-build -a -b html ./doc BUILD/doc/build/
