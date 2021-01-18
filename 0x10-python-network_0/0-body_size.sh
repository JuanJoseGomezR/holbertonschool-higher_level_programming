#!/bin/bash
# Displays size in bytes
curl -s "$1" | wc -c
