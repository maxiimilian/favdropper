#!/bin/env bash
cd "${0%/*}"
PYTHON=~/.virtualenvs/FavDropper/bin/python3
SCRIPT=./favdropper.py

$PYTHON $SCRIPT
