#!/bin/bash
# Script display size of body content
curl -sI $1 | grep -i 'content-lenght' | cut -d ' ' -f2
