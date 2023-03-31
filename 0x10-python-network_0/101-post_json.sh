#!/bin/bash
# sends JSON POST request to a URL as the first argument, displays the response body
curl -s -o /dev/null -w "%{http_code}" "$1"
