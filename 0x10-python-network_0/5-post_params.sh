#!/bin/bash
# POST request to the passed URL
curl -sX POST --data "email=hr@holbertonschool.com" --data "subject=I will always be here for PLD" "$1"
