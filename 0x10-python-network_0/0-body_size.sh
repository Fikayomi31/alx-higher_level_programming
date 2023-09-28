#!/bin/bash
# Script display size of body content
curl -sI "$1" | wc -c
