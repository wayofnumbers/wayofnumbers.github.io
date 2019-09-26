#!/usr/bin/env bash

pelican content -s publishconf.py
 
git add .
git commit -m "fix"
git push origin dev
