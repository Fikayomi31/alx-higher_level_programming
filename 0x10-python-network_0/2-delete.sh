#!/bin/bash
# Script that send a delete request to the Url passed as the 1st argument
curl -sX DELETE "$1"
