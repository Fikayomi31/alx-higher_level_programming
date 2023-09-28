#!/bin/bash
# Script to display size of body content from a url
curl -sI "$1" | grep -i 'content-length' | cut -d ' ' -f2

