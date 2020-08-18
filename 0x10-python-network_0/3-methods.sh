#!/bin/bash
# Script to display methods HTTP server
curl -sI "$1" | grep Allow | cut --complement -d' ' -f1
