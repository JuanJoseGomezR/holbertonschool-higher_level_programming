#!/bin/bash
# status coed
curl -so /dev/null --head -w "%{http_code}" "$1"
