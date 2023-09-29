#!/bin/bash
# Script that takes a url send a POST request to the pass url
curl -s POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
