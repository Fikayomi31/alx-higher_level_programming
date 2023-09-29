#!/bin/bash
# Script that take in a url and display all HTTP method the server will accept
curl -sIX OPTIONS "$1" | grep -i 'allow' | cut -d ' ' -f 2-
