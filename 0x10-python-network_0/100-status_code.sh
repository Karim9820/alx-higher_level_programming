#!/bin/bash
# sends a request to a URL as an argument, displays only the response status code
curl -s -o /dev/null -w "%{http_code}" "$1"
