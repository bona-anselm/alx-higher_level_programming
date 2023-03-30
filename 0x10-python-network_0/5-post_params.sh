#!/bin/bash
# Script that shows the Content-Length from a HTTP request
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
