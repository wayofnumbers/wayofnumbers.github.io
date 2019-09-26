#!/usr/bin/env bash

# pelican content -s publishconf.py

# ghp-import output -b master
 
git add .
git commit -m "fix"
git push origin dev
