#!/bin/bash
# takes in a URL, sends request to the URL displays size of the response body
curl -s "$1" | wc -c
