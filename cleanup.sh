#!/usr/bin/env bash


find . -name "*.pyc" -exec rm {} \;
find . -name "__pycache__" -exec rm -rf {} \;
find . -name ".cache" -exec rm {} \;