#!/bin/bash
# Script to display size of body content from a url
curl -sI "$1" | wc -c
