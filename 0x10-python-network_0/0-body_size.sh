#!/bin/bash
# Displays size in bytes

curl "$1" | wc -c
